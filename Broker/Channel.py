import hashlib

from Broker.CommunicationRepository import CommunicationRepository


class Channel:
    def __init__(self, topic):
        self._topic = topic
        self._subscribers = []
        self._communication_repository = CommunicationRepository()
        self._id = hashlib.md5(self._topic).hexdigest()

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)
        print(f"Subscribed to {self._topic}")

    def unsubscribe(self, subscriber):
        for old_subscriber in self._subscribers:
            if old_subscriber.get_client_id() == subscriber.get_client_id():
                self._subscribers.pop(self._subscribers.index(old_subscriber))
                print(f"Unsubscribed from {self._topic}")

    def publish(self, origin, message):
        print(f"Message: {message}")
        for subscriber in self._subscribers:
            if subscriber is origin:
                continue
            self._communication_repository.message_queues[subscriber].put(message)
            self._communication_repository.output_sockets.append(subscriber)

    def get_id(self):
        return self._id
