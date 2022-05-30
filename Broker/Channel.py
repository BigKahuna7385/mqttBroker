import hashlib


class Channel:
    def __init__(self, topic):
        self._topic = topic
        self._subscribers = []
        self._id = hashlib.md5(_topic)

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.pop(subscriber)

    def publish(self, message):
        for subscriber in _subscribers:
            self._send_message(subscriber, message)

    def _send_message(self, subscriber, message):
        print(message)

    def get_id(self):
        return self._id
