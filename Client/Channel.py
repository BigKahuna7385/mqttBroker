import hashlib

from Client.Message import Message


class Channel:
    def __init__(self, topic):
        self._topic = topic
        self._id = hashlib.md5(self._topic.encode())
        self._client_list = []

    def subscribe_to_channel(self, client):
        self._client_list.append(client)
        message = Message("SUBSCRIBE", "")
        client.send(message.build(self._topic))

    def unsubscribe_from_channel(self, client):
        self._client_list.pop(self._find_index_of(client))
        message = Message("UNSUBSCRIBE", "")
        client.send(message.build(self._topic))

    def publish(self, client, message):
        message = Message("PUBLISH", message)
        client.send(message.build(self._topic))

    def get_client_list(self):
        return self._client_list

    def get_id(self):
        return self._id

    def _find_index_of(self, client):
        return self._client_list.index(client)
