class Broker:
    def __init__(self):
        _bWithAuth = False
        _userList = []
        _channelDict = {}

        def get_channel_dict():
            return _channelDict

        def get_user_list():
            return _userList

        def add_user(User):
            _userList.append(User)

        def remove_user(User):
            _userList.append(User)

        def add_channel(Channel):
            _channelDict[Channel.getName()] = Channel

        def remove_channel(Channel):
            _channelDict.pop(Channel.getName())
