import hashlib
from unittest import TestCase
from unittest.mock import Mock

from Client.Channel import Channel
from Client.Client import Client


class TestClient(TestCase):
    def test_subscribe_to_channel(self):
        topic = "catfacts"
        channel_id = hashlib.md5(topic.encode())
        channel = Mock(get_id=Mock(return_value=channel_id))
        client = Client()
        client.subscribe_to_channel(channel)
        channel_dict = client.get_channel_dict()
        self.assertEqual(channel_dict[channel_id], channel)

        client.unsubscribe_from_channel(channel)
        channel_dict = client.get_channel_dict()
        self.assertEqual(len(channel_dict), 0)

    def test_subscribe_to_real_channel(self):
        broker = Mock()
        channel = Channel(broker, "catfacts")
        client = Client()
        client.subscribe_to_channel(channel)

        test_list = channel.get_client_list()
        self.assertEqual(test_list[0], client)

        channel_dict = client.get_channel_dict()
        self.assertEqual(channel_dict[channel.get_id()], channel)

        channel.unsubscribe_from_channel(client)
        test_list = channel.get_client_list()
        self.assertEqual(len(test_list), 0)
