
class Client:
    def __init__(self):
        _channelDict = {}

        def publish(message, channel):
            if channel not in _channelDict:
                return "Error"
            channel.publish(message)

        def subscribe_to_channel(channel):
            _channelDict[channel.get_id()] = channel
            channel.subscribe(self)

        def unsubscribe_from_channel(channel):
            _channelDict.pop(channel.get_id())
            channel.unsuscribe(self)
