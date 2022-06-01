import hashlib

from Client.Message import Message


class Channel:
    def __init__(self, broker, topic):
        self._topic = topic
        self._broker = broker
        self._id = hashlib.md5(self._topic.encode())
        self._client_list = []

    def subscribe_to_channel(self, client):
        self._client_list.append(client)
        message = Message("SUBSCRIBE", {"topic": self._topic})
        send_message(self._topic, message.build(""), self._broker)

    def unsubscribe_from_channel(self, client):
        self._client_list.pop(self._find_index_of(client))
        message = Message("UNSUBSCRIBE", {"topic": self._topic})
        send_message(self._topic, message.build(""), self._broker)

    def publish(self, message):
        message = Message("PUBLISH", message)
        send_message(self._topic, message.build(self._topic), self._broker)

    def get_client_list(self):
        return self._client_list

    def get_id(self):
        return self._id

    def _find_index_of(self, client):
        return self._client_list.index(client)


def send_message(topic, message, broker):
    print(topic.encode() + message)
