from Client.Client import Client

if __name__ == '__main__':
    client = Client("127.0.0.1", 1883)
    client.test_sending(2)
    client2 = Client("127.0.0.1", 8883)
    client2.test_sending(2)
