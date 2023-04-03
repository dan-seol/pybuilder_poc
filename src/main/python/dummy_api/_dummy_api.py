class DummyApi():

    def __init__(self, hostname, username, password):
        self._hostname = hostname
        self._username = username
        self._password = password

    def say_hello(self, name):
        return f'Hello, {name}! You are on {self._hostname} as a user {self._username}'


class DummyApiTwo():

    def __init__(self, hostname, username, password):
        self._hostname = hostname
        self._username = username
        self._password = password

    def say_bye(self, name):
        return f'Bye, {name}! You were on {self._hostname} as a user {self._username}'
