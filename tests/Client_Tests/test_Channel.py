from unittest import TestCase
from unittest.mock import Mock

from Client.Channel import Channel


class TestChannel(TestCase):
    def test_subscribe_to_channel(self):
        broker = Mock()
        channel = Channel(broker, "catfacts")
        client = Mock()
        channel.subscribe_to_channel(client)

        test_list = channel.get_client_list()
        self.assertEqual(test_list[0], client)

        channel.unsubscribe_from_channel(client)
        test_list = channel.get_client_list()
        self.assertEqual(len(test_list), 0)


