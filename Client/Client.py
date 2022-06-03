import logging
import socket
import time

import Broker.Broker
from Client import Channel
from Client.Message import Message

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)


class Client:
    def __init__(self, broker: Broker):
        self._server_socket = None
        self._broker = broker
        self._channelDict = {}

    def publish(self, message: Message, channel: Channel):
        if channel not in self._channelDict:
            return "Error"
        channel.publish(message)

    def subscribe_to_channel(self, channel: Channel):
        self._channelDict[channel.get_id()] = channel
        channel.subscribe_to_channel(self)

    def unsubscribe_from_channel(self, channel: Channel):
        self._channelDict.pop(channel.get_id())
        channel.unsubscribe_from_channel(self)

    def get_channel_dict(self) -> dict:
        return self._channelDict

    def open_socket(self):
        self._server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server_socket.connect((self._broker.get_ip_address(), self._broker.get_port()))

    def send(self, message: Message):
        self._server_socket.send(message)
        logging.info(f"Send {message}")
        time.sleep(0.3)

    def listen(self):
        data = self._server_socket.recv(1024)
        print(data)
        logging.info(f"Received: {data}")

    def close_socket(self):
        self._server_socket.close()
        logging.info("Closed Socket")
