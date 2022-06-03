from Client.Broker import Broker
from Client.Channel import Channel
from Client.Client import Client
from multiprocessing import Process

if __name__ == '__main__':
    channel_a = Channel("a/b")
    broker_a = Broker("127.0.0.1", 1883)
    client_a = Client(broker_a)
    client_a.open_socket()
    channel_a.subscribe_to_channel(client_a)

    channel_b = Channel("a/b")
    broker_b = Broker("127.0.0.1", 8883)
    client_b = Client(broker_b)
    client_b.open_socket()
    channel_b.subscribe_to_channel(client_b)

    listen_b = Process(target=client_b.listen)
    listen_b.start()

    channel_a.publish(client_a, "Dies ist ein Test")
    listen_a = Process(target=client_a.listen)
    listen_a.start()

    listen_b.join()
    channel_b.publish(client_b, "Dies ist eine Test Antwort")
    listen_a.join()

    channel_a.unsubscribe_from_channel(client_a)
    client_a.close_socket()

    channel_b.unsubscribe_from_channel(client_b)
    client_b.close_socket()