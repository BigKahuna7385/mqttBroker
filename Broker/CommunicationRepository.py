import hashlib
import logging
import socket as s
from queue import Queue

from Broker import utils

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)

class CommunicationRepository:
    class __CommunicationRepository:
        def __init__(self):
            self.input_sockets = []
            self.output_sockets = []
            self.message_queues = {}

        def add_to_inputs(self, socket: s.socket):
            self.input_sockets.append(socket)
            logging.info(f"adding socket: {socket.getpeername()}")
            hash_value = utils.create_socket_hash(socket)
            self.message_queues[hash_value] = Queue()

    instance = None

    def __init__(self):
        if not CommunicationRepository.instance:
            CommunicationRepository.instance = CommunicationRepository.__CommunicationRepository()

    def __getattr__(self, item):
        return getattr(CommunicationRepository.instance, item)
