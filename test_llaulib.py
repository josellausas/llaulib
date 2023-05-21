import unittest
import environ
import os
from unittest import mock

from llaulib.chato import Chato
from llaulib.chato import Notapi

env = environ.Env(
    DEBUG=(bool, True),
    SLACK_TOKEN = (str, 'unknown_key'),
    SLACK_NAME = (str, 'llausys-nameless'),
    NOTION_TOKEN = (str, 'unknown_token'),
)
environ.Env.read_env()
mockEnv = {
    "NOTION_TOKEN": "unknown_token",
    "NOTION_DB": "unknown_db"
}

class TestLlauLibNotapi(unittest.TestCase):
    @mock.patch.dict(os.environ, mockEnv, clear=True)
    def test_napi(self):
        self.assertIsNotNone(Notapi)
    
    @mock.patch.dict(os.environ, mockEnv, clear=True)
    def test_is_domain_live(self):
        self.assertTrue(Notapi.is_domain_live('llau.systems'))

if __name__ == '__main__':
    unittest.main()