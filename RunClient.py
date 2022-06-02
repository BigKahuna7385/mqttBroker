from Client.Broker import Broker
from Client.Channel import Channel
from Client.Client import Client

if __name__ == '__main__':
    channel = Channel("a/b")
    broker = Broker("127.0.0.1", 1883)
    client = Client(broker)
    client.open_socket()
    channel.subscribe_to_channel(client)
    channel.publish(client, "Dies ist ein Test")
    channel.unsubscribe_from_channel(client)
    client.close_socket()
