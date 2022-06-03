import hashlib

import Client.Client
from Client.Message import Message


class Channel:
    def __init__(self, topic: str):
        self._topic = topic
        self._id = hashlib.md5(self._topic.encode()).hexdigest()
        self._client_list = []

    def subscribe_to_channel(self, client: Client.Client.Client):
        self._client_list.append(client)
        message = Message("SUBSCRIBE", "")
        client.send(message.build(self._topic))

    def unsubscribe_from_channel(self, client: Client.Client.Client):
        self._client_list.pop(self._find_index_of(client))
        message = Message("UNSUBSCRIBE", "")
        client.send(message.build(self._topic))

    def publish(self, client: Client.Client.Client, message: str):
        message = Message("PUBLISH", message)
        client.send(message.build(self._topic))

    def get_client_list(self) -> list:
        return self._client_list

    def get_id(self) -> str:
        return self._id

    def _find_index_of(self, client: Client.Client.Client) -> int:
        return self._client_list.index(client)
