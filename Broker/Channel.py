import hashlib

from Broker.CommunicationRepository import CommunicationRepository


class Channel:
    def __init__(self, topic):
        self._topic = topic
        self._subscribers = []
        self._communication_repository = CommunicationRepository()
        self._id = hashlib.md5(self._topic)

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.pop(subscriber)

    def publish(self, origin, message):
        for subscriber in self._subscribers:
            if subscriber is origin:
                continue
            self._communication_repository.message_queues[subscriber].put(message)
            self._communication_repository.output_sockets.append(subscriber)

    def get_id(self):
        return self._id
