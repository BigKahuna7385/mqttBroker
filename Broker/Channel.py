import hashlib

from Broker.CommunicationRepository import CommunicationRepository
from Broker.Subscriber import Subscriber


class Channel:
    def __init__(self, topic: str):
        self._topic = topic
        self._subscribers = []
        self._communication_repository = CommunicationRepository()
        self._id = hashlib.md5(self._topic).hexdigest()

    def subscribe(self, subscriber: Subscriber):
        self._subscribers.append(subscriber)
        print(f"Subscribed to {self._topic}")

    def unsubscribe(self, subscriber: Subscriber):
        for old_subscriber in self._subscribers:
            if old_subscriber.get_client_id() == subscriber.get_client_id():
                self._subscribers.pop(self._subscribers.index(old_subscriber))
                print(f"Unsubscribed from {self._topic}")

    def publish(self, origin: Subscriber, message: bytes):
        print(f"Message: {message}")
        for subscriber in self._subscribers:
            if subscriber is origin:
                continue
            self._communication_repository.message_queues[subscriber.get_client_id()].put(message)
            self._communication_repository.output_sockets.append(subscriber.get_socket())

    def get_id(self) -> str:
        return self._id
