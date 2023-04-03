from unittest import TestCase
from dummy_api import DummyApi


class DummyApiTests(TestCase):
    def test_dummy_api(self):
        dummy_api = DummyApi(hostname='dummyhost', username='dummyuser', password='dummypass')
        self.assertEquals(f'Hello, Aanika! You are on dummyhost as a user dummyuser', dummy_api.say_hello('Aanika'))
