class Broker:
    def __init__(self):
        self._bWithAuth = False
        self._userList = []
        self._channelDict = {}

    def get_channel_dict(self):
        return self._channelDict

    def get_user_list(self):
        return self._userList

    def add_user(self, user):
        self._userList.append(user)

    def remove_user(self, user):
        self._userList.append(user)

    def add_channel(self, channel):
        self._channelDict[channel.get_id()] = channel

    def remove_channel(self, channel):
        self._channelDict.pop(channel.get_id())
