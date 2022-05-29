class Broker:
    def __init__(self):
        _bWithAuth = False
        _userList = []
        _channelDict = {}

        def get_channel_dict():
            return _channelDict

        def get_user_list():
            return _userList

        def add_user(user):
            _userList.append(user)

        def remove_user(user):
            _userList.append(user)

        def add_channel(channel):
            _channelDict[channel.get_id()] = channel

        def remove_channel(channel):
            _channelDict.pop(channel.get_id())
