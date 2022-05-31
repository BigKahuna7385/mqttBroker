import hashlib
import logging
import select
import socket as s
from queue import Queue

from Broker import utils
from Broker.CommunicationRepository import CommunicationRepository

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)


class Broker:
    def __init__(self):
        self._bWithAuth = False
        self._userList = []
        self._channelDict = {}
        self._HOST = "127.0.0.1"
        self._PORT = 1883
        self._communication_repository = CommunicationRepository()
        self._create_server_socket(self._HOST, self._PORT)
        logging.info("Starting socket service")

    def _create_server_socket(self, host, port):
        logging.info(f"Initializing Server Socket for ips {self._HOST} on port {self._PORT}")
        self._server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
        self._server_socket.setblocking(False)
        self._server_socket.bind((host, port))
        self._server_socket.listen()
        logging.info("Finished Serversocket initialization")
        self._communication_repository.input_sockets.append(self._server_socket)
        logging.info("Added Server Socket to input sockets")

    def run_socket_service(self):
        while True:
            readable, writable, exceptional = select.select(self._communication_repository.input_sockets,
                                                            self._communication_repository.output_sockets,
                                                            self._communication_repository.input_sockets)
            for socket in readable:
                if socket is self._server_socket:
                    self._accept_client(socket)
                else:
                    self._read_data(socket)
            for socket in writable:
                message = self._communication_repository.message_queues[utils.create_socket_hash(socket)].get()
                # SEND Header and Payload
                socket.send(message)
                logging.info(f"Send message {message}")
                self._communication_repository.output_sockets.remove(socket)

            for socket in exceptional:
                self._communication_repository.input_sockets.remove(socket)
                self._communication_repository.output_sockets.remove(socket)
                socket.close()

    def _accept_client(self, socket):
        connection, address = socket.accept()
        logging.info(f"Accepted client {address}")
        connection.setblocking(False)
        self._communication_repository.add_to_inputs(connection)
        logging.info("Added message queue ini")

    def get_channel_dict(self):
        return self._channelDict

    def get_user_list(self):
        return self._userList

    def add_user(self, user):
        self._userList.append(user)

    def remove_user(self, user):
        self._userList.append(user)

    def add_channel(self, channel):
        self._channelDict[channel.get_id()] = channel

    def remove_channel(self, channel):
        self._channelDict.pop(channel.get_id())

    def _read_data(self, socket):
        data = socket.recv(1024)
        logging.info(f"Received {data} from {socket.getsockname()[0]}, {socket.getsockname()[1]}")
        self._communication_repository.message_queues[utils.create_socket_hash(socket)].put(b"Pong")
        self._communication_repository.output_sockets.append(socket)
