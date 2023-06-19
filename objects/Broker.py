class Broker():
    def __init__(self, name='Default Broker') -> None:
        self._name = name
        self._topics = {}

    def subscribe(self, topic, subscriber):
        if topic not in self._topics.keys():
            # Alloc a new topic
            self._topics[topic] = []
        
        if self.isSubscribed(topic, subscriber):
            return False
        else:    
            self._topics[topic].append(subscriber)
            return True
    
    def unsubscribe(self, topic, subscriber):
        if self.isSubscribed(topic, subscriber):
            self._topics[topic].remove(subscriber)
            return True
        return False
    
    def publish(self, topic='#', msg="Hello World"):
        if topic in self._topics.keys():
            for subscriber in self._topics[topic]:
                subscriber.onMessageReceived(topic, msg)

    def isSubscribed(self, topic, subscriber):
        if topic in self._topics.keys():
            return subscriber in self._topics[topic]
        else:
            return False

b = Broker()
def get_broker():
    return b


class Subscriber():
    def onMessageReceived(self, topic, msg):
        # print(f'Received: #{topic} - $ {msg}!')
        pass