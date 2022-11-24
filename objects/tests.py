import unittest

class ObjectTests(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_business_manager(self):
        from BusinessManager import BusinessManager
        b = BusinessManager()
        self.assertIsNotNone(b)

if __name__ == '__main__':
    unittest.main()
