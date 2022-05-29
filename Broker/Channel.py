import hashlib


class Channel:
    def __init__(self, topic):
        _topic = topic
        _subscribers = []
        _id = hashlib.md5(_topic)

        def subscribe(subscriber):
            _subscribers.append(subscriber)

        def unsubscribe(subscriber):
            _subscribers.pop(subscriber)

        def publish(message):
            for subscriber in _subscribers:
                _send_message(subscriber, message)

        def _send_message(subscriber, message):
            print(message)

