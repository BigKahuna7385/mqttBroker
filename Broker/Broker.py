import logging
import socket as s

import select

from Broker import utils
from Broker.Channel import Channel
from Broker.CommunicationRepository import CommunicationRepository
from Broker.Subscriber import Subscriber
from Utils.MessageParser import MessageParser

logging.basicConfig(format='%(levelname)s - %(asctime)s: %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)


class Broker:
    def __init__(self):
        self._bWithAuth = False
        self._userList = []
        self._channelDict = {}
        self._HOST = "127.0.0.1"
        self._PORTS = (1883, 8883)
        self._communication_repository = CommunicationRepository()
        self._server_sockets = []
        self._create_server_socket(self._HOST, self._PORTS[0])
        self._create_server_socket(self._HOST, self._PORTS[1])
        self._message_parser = MessageParser()
        logging.info("Starting socket service")

    def _create_server_socket(self, host, port):
        logging.info(f"Initializing Server Socket for ips {host} on port {port}")
        server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
        server_socket.setblocking(False)
        server_socket.bind((host, port))
        server_socket.listen()
        logging.info("Finished Serversocket initialization")
        self._server_sockets.append(server_socket)
        self._communication_repository.input_sockets.append(server_socket)
        logging.info("Added Server Socket to input sockets")

    def run_socket_service(self):
        while True:
            readable, writable, exceptional = select.select(self._communication_repository.input_sockets,
                                                            self._communication_repository.output_sockets,
                                                            self._communication_repository.input_sockets)
            for socket in readable:
                if socket in self._server_sockets:
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
        logging.info(f"Accepted client {address} on {socket.getsockname()}")
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
        if data:
            logging.info(f"Received {data} from {socket.getpeername()[0]}, {socket.getpeername()[1]}")
            subscriber = self._get_subscriber(socket.getpeername()[0], socket.getpeername()[1])
            if data:
                header_type = self._message_parser.parse_fixed_header(data)
                logging.info(f"Received header type: {header_type}")
                if header_type == "SUBSCRIBE":
                    self._subscribe_to_channel(data, subscriber)
                elif header_type == "UNSUBSCRIBE":
                    self._unsubscribe_from_channel(data, subscriber)
                elif header_type == "PUBLISH":
                    self._publish(data, subscriber)

                self._communication_repository.message_queues[utils.create_socket_hash(socket)].put(b"Pong")
                self._communication_repository.output_sockets.append(socket)
        if not data:
            logging.info(f"removing socket from input sources: {socket.getpeername()}")
            self._communication_repository.input_sockets.remove(socket)
            try:
                self._communication_repository.output_sockets.remove(socket)
            except ValueError:
                pass
            del self._communication_repository.message_queues[utils.create_socket_hash(socket)]

    def _subscribe_to_channel(self, data, subscriber):
        topic = self._message_parser.parse_topic(data)
        channel = Channel(topic)
        if not channel.get_id() in self._channelDict:
            self.add_channel(channel)
        self._channelDict[channel.get_id()].subscribe(subscriber)

    def _unsubscribe_from_channel(self, data, subscriber):
        topic = self._message_parser.parse_topic(data)
        channel = Channel(topic)
        if channel.get_id() in self._channelDict:
            self._channelDict[channel.get_id()].unsubscribe(subscriber)

    def _publish(self, data, subscriber):
        topic = self._message_parser.parse_topic(data)
        message = self._message_parser.parse_message(data)
        channel = Channel(topic)
        if channel.get_id() in self._channelDict:
            self._channelDict[channel.get_id()].publish(subscriber, message)

    def _get_subscriber(self, ip_address, port):
        new_subscriber = Subscriber(ip_address, port)
        for user in self._userList:
            if new_subscriber.get_client_id() == user.get_client_id():
                return user
        self._userList.append(new_subscriber)
        return new_subscriber
