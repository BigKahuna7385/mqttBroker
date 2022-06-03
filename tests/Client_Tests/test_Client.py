import hashlib
from unittest import TestCase
from unittest.mock import Mock

from Client.Channel import Channel
from Client.Client import Client


class TestClient(TestCase):
    def test_subscribe_to_channel(self):
        topic = "cat/facts"
        channel_id = hashlib.md5(topic.encode())
        channel = Mock(get_id=Mock(return_value=channel_id))
        broker = Mock()
        client = Client(broker)
        client.subscribe_to_channel(channel)
        channel_dict = client.get_channel_dict()
        self.assertEqual(channel_dict[channel_id], channel)

        client.unsubscribe_from_channel(channel)
        channel_dict = client.get_channel_dict()
        self.assertEqual(len(channel_dict), 0)
