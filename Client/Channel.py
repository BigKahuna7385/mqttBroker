import hashlib


class Channel:
    def __init__(self, broker, topic):
        _topic = topic
        _broker = broker
        _id = hashlib.md5(_topic)

        def subscribe_to_channel(client):
            print("Subscribed to " + _topic)

        def unsubscribe_from_channel(client):
            print("Unsubscribed from " + _topic)

        def publish(message):
            print("Published :" + message)
