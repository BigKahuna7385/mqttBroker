import logging
import socket

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

class Client:
    def __init__(self):
        self._channelDict = {}
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.info("Connecting to server")
        self._server_socket.connect(("127.0.0.1", 1883))
        logging.info("Connected succesfully")

    def test_sending(self):
        self._server_socket.send(b"Ping")
        logging.info("Send: Ping")
        data = self._server_socket.recv(1024)
        logging.info(f"Received: {data}")
        self._server_socket.close()

    def publish(self, message, channel):
        if channel not in self._channelDict:
            return "Error"
        channel.publish(message)

    def subscribe_to_channel(self, channel):
        self._channelDict[channel.get_id()] = channel
        channel.subscribe_to_channel(self)

    def unsubscribe_from_channel(self, channel):
        self._channelDict.pop(channel.get_id())
        channel.unsubscribe_from_channel(self)

    def get_channel_dict(self):
        return self._channelDict
