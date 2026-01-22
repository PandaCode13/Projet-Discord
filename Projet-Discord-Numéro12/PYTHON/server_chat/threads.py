import threading
import pickle
import queue
import time
from loguru import logger
try:
    from common_messages import HBMessage, TextMessage
except ImportError:
    from .common_messages import HBMessage, TextMessage # Si exécuté en tant que module

class HeartbeatListener(threading.Thread):
    """Thread qui collecte les HBMessages et évalue l'état du client."""
    def __init__(self, hb_queue):
        super().__init__()
        self.hb_queue = hb_queue
        self.running = True

    def run(self):
        while self.running:
            time.sleep(10) # Intervalle de vérification
            if self.hb_queue.empty():
                logger.error("Le client est en panne (aucun Heartbeat reçu)")
                self.running = False
            else:
                # On vide la file pour attendre les prochains battements
                while not self.hb_queue.empty():
                    self.hb_queue.get()

class MessageReceptor(threading.Thread):
    """Gère la réception/envoi et l'unicité du pseudonyme."""
    def __init__(self, client_socket, list_client):
        super().__init__()
        self.client_socket = client_socket
        self.list_client = list_client
        self.hb_queue = queue.Queue()
        self.pseudo = ""

    def run(self):
        # Démarrage du listener de Heartbeat pour ce client
        hb_listener = HeartbeatListener(self.hb_queue)
        hb_listener.start()

        try:
            while True:
                data = self.client_socket.recv(4096)
                if not data: break
                
                message = pickle.loads(data)

                if isinstance(message, HBMessage):
                    self.hb_queue.put(message)
                
                elif isinstance(message, TextMessage):
                    if not self.pseudo:
                        self.handle_login(message.get_msg())
                    elif message.get_msg() == "exit":
                        break
                    else:
                        self.broadcast(f"{self.pseudo} a dit : {message.get_msg()}")
        except Exception as e:
            logger.error(f"Erreur avec le client {self.pseudo}: {e}")
        finally:
            self.client_socket.close()
            hb_listener.running = False
            if self.pseudo in self.list_client.values():
                del self.list_client[self]

    def handle_login(self, pseudo):
        if pseudo in self.list_client.values():
            self.client_socket.send(pickle.dumps(TextMessage("ERREUR: Pseudo déjà pris")))
        else:
            self.pseudo = pseudo
            self.list_client[self] = pseudo
            self.broadcast(f"SYSTEME: {pseudo} a rejoint la salle.")

    def broadcast(self, text):
        msg_obj = TextMessage(text)
        for receptor in self.list_client.keys():
            try:
                receptor.client_socket.send(pickle.dumps(msg_obj))
            except:
                pass