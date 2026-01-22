import socket
from loguru import logger
from server_chat.threads import MessageReceptor

PORT_NUMBER = 1234
HOST = '0.0.0.0'

def main():
    list_client = {}  # Équivalent de la Hashtable (MessageReceptor: Pseudonyme)
    
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT_NUMBER))
        server_socket.listen()
        logger.info(f"Le socket de connexion a été créé au port {PORT_NUMBER}")
    except Exception as e:
        logger.error(f"Échoué à créer un socket de connexion : {e}")
        return

    numero_client = 0
    while True:
        try:
            client_socket, address = server_socket.accept()
            
            # Créer un thread MessageReceptor pour le nouveau client
            new_receptor = MessageReceptor(client_socket, list_client)
            list_client[new_receptor] = ""  # Le pseudo sera rempli après validation
            
            new_receptor.start()
            logger.info(f"Client {numero_client} se connecte !")
            numero_client += 1
        except Exception as e:
            logger.error(f"Erreur lors de l'acceptation d'un client : {e}")

if __name__ == "__main__":
    main()