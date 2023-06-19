import unittest
from .Broker import Broker, Subscriber
from .AStar import AStarSearch

class ObjectTests(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_business_manager(self):
        from .BusinessManager import BusinessManager
        b = BusinessManager()
        self.assertIsNotNone(b)

class TestSubscriber(Subscriber):
    def __init__(self) -> None:
        super().__init__()
        self.receivedMsg = ""
    
    def onMessageReceived(self, topic, msg):
        super().onMessageReceived(msg, topic)
        self.receivedMsg = msg


class BrokerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.subscriber = TestSubscriber()
        self.topic = "testTopic"
        self.message = "Hello World"
        self.broker = Broker('testBroker')
        return super().setUp()
    
    def test_is_subscribed(self):
        self.assertFalse(self.broker.isSubscribed(self.topic, self.subscriber))

    def test_subscribe(self):
        self.assertFalse(self.broker.isSubscribed(self.topic, self.subscriber))
        self.assertTrue(self.broker.subscribe(self.topic, self.subscriber))
        self.assertTrue(self.broker.isSubscribed(self.topic, self.subscriber))

    def test_post(self):
        self.assertTrue(self.broker.subscribe(self.topic, self.subscriber))
        self.assertTrue(self.broker.isSubscribed(self.topic, self.subscriber))
        self.assertEqual(self.subscriber.receivedMsg, '')
        self.broker.publish(self.topic, self.message)
        self.assertEqual(self.subscriber.receivedMsg, self.message)

    def test_unsubscribe(self):
        self.assertTrue(self.broker.subscribe(self.topic, self.subscriber))
        self.assertTrue(self.broker.isSubscribed(self.topic, self.subscriber))
        self.assertTrue(self.broker.unsubscribe(self.topic, self.subscriber))
        self.assertFalse(self.broker.isSubscribed(self.topic, self.subscriber))
        self.subscriber.receivedMsg = 'untouched'
        self.broker.publish(self.topic, self.message)
        self.assertEqual(self.subscriber.receivedMsg, 'untouched')

class AStarTests(unittest.TestCase):
    def setUp(self) -> None:
        self.search = AStarSearch()
        self.map = {}
        return super().setUp()
    
    def test_load_map(self):
        self.assertTrue(self.search.load_map(self.map))
        self.assertIsNotNone(self.search.map)
        

if __name__ == '__main__':
    unittest.main()
