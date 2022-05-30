class Client:
    def __init__(self):
        self._channelDict = {}

    def publish(self, message, channel):
        if channel not in self._channelDict:
            return "Error"
        channel.publish(message)

    def subscribe_to_channel(self, channel):
        self._channelDict[channel.get_id()] = channel
        channel.subscribe_to_channel(self)

    def unsubscribe_from_channel(self, channel):
        self._channelDict.pop(channel.get_id())
        channel.unsubscribe_from_channel(self)

    def get_channel_dict(self):
        return self._channelDict
