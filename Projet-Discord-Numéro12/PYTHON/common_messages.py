import time

class HBMessage:
    """Classe pour le mécanisme HeartBeat (équivalent HBMessage.java)"""
    def __init__(self):
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return self.timestamp

class TextMessage:
    """Classe pour les messages de chat (équivalent TextMessage.java)"""
    def __init__(self, msg=""):
        self.msg = msg

    def get_msg(self):
        return self.msg