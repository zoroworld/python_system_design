# Subject (Notifier) (publisher)
class Notifier:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def display(self):
        for i in range(len(self.subscribers)):
            print(i, self.subscribers[i].name)

    def notify(self, message):
        for sub in self.subscribers:
            sub.update(message)