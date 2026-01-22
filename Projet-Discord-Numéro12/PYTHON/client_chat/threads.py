import threading
import pickle
import time
import queue
from loguru import logger
try:
    from common_messages import HBMessage, TextMessage
except ImportError:
    from .common_messages import HBMessage, TextMessage # Si exécuté en tant que module

class SendMessage(threading.Thread):
    """Thread qui s'occupe d'envoyer les messages texte (SendMessage.java)"""
    def __init__(self, client_socket):
        super().__init__()
        self.client_socket = client_socket

    def run(self):
        # Le premier message envoyé sert de pseudonyme selon le document
        pseudo = input("Entrez votre pseudonyme : ")
        self.client_socket.send(pickle.dumps(TextMessage(pseudo)))
        
        while True:
            msg_text = input()
            try:
                self.client_socket.send(pickle.dumps(TextMessage(msg_text)))
                if msg_text == "exit":
                    break
            except Exception as e:
                logger.error(f"Erreur d'envoi : {e}")
                break

class ReceiveMessage(threading.Thread):
    """Thread qui reçoit et affiche les TextMessages (ReceiveMessage.java)"""
    def __init__(self, client_socket):
        super().__init__()
        self.client_socket = client_socket

    def run(self):
        while True:
            try:
                data = self.client_socket.recv(4096)
                if not data: break
                
                message = pickle.loads(data)
                if isinstance(message, TextMessage):
                    print(f"\n{message.get_msg()}")
            except:
                break

class HeartbeatAgent(threading.Thread):
    """Thread qui envoie un HBMessage périodiquement (HeartbeatAgent.java)"""
    def __init__(self, client_socket):
        super().__init__()
        self.client_socket = client_socket
        self.daemon = True # S'arrête si le programme principal s'arrête

    def run(self):
        while True:
            try:
                self.client_socket.send(pickle.dumps(HBMessage()))
                time.sleep(5) # DEFAULT_SAMPLING_PERIOD
            except:
                break

class HeartbeatListener(threading.Thread):
    """Thread qui évalue l'état du serveur (HeartbeatListener.java)"""
    # Note : Dans une version simple, il surveille l'activité du socket
    def __init__(self):
        super().__init__()
        self.daemon = True

    def run(self):
        # Logique simplifiée pour respecter le flux du document
        # En Python, si ReceiveMessage échoue, on considère souvent la panne serveur
        pass