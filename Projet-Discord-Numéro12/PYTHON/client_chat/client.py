import socket
import sys
from loguru import logger
from client_chat.threads import SendMessage, ReceiveMessage, HeartbeatAgent, HeartbeatListener

PORT_NUMBER = 1234
HOST = '127.0.0.1'

def main():
    try:
        # Création du socket client
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT_NUMBER))
        logger.info("Connexion au serveur établie.")
    except Exception as e:
        logger.error(f"Impossible de se connecter au serveur : {e}")
        sys.exit(1)

    # Lancement des threads
    # 1. Thread pour envoyer des messages
    send_thread = SendMessage(client_socket)
    # 2. Thread pour recevoir des messages
    receive_thread = ReceiveMessage(client_socket)
    # 3. Thread pour envoyer des Heartbeats périodiquement
    hb_agent = HeartbeatAgent(client_socket)
    # 4. Thread pour écouter l'état du serveur via les Heartbeats
    hb_listener = HeartbeatListener()

    # Démarrage
    send_thread.start()
    receive_thread.start()
    hb_agent.start()
    hb_listener.start()

if __name__ == "__main__":
    main()