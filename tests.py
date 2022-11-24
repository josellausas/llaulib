import unittest
import environ
import os
from unittest import mock

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

# TODO: Update the tests to phone home only when CI_PIPELINE is true
class TestLlauLibChato(unittest.TestCase):
    
    def test_chato(self):
        from chato import Chato
        self.assertIsNotNone(Chato.getInstance())

        # Should Post
        Chato.getInstance().enable()
        self.assertTrue(Chato.getInstance().enabled)
        result = Chato.chato('Chato was tested', 'home.tests.test_chato', 'llau-systems')
        self.assertEqual(result, 0) # 0 means SUCCESS
        
        # Should Disable
        Chato.getInstance().disable()
        self.assertFalse(Chato.getInstance().enabled)

class TestLlauLibNotapi(unittest.TestCase):
    @mock.patch.dict(os.environ, mockEnv, clear=True)
    def test_napi(self):
        from chato import Notapi
        self.assertIsNotNone(Notapi)
    
    @mock.patch.dict(os.environ, mockEnv, clear=True)
    def test_is_domain_live(self):
        from chato import Notapi
        self.assertTrue(Notapi.is_domain_live('llau.systems'))

if __name__ == '__main__':
    unittest.main()