"""
------------------------------------------
@File       : 5.observer_newspublisher.py
@CreatedOn  : 2022/7/20 13:29
------------------------------------------
    观察者模式——新闻机构例子
"""
from abc import ABCMeta, abstractmethod


class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__last_news = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notify_subscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def add_news(self, news):
        self.__last_news = news

    def get_news(self):
        return self.__last_news


class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


class SMSSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


class AnyOtherSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.get_news())


def main():
    new_publisher = NewsPublisher()

    for subscriber in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        subscriber(new_publisher)

    print(f"\nSubscribers: {new_publisher.subscribers()}")

    new_publisher.add_news("Hello world!")
    new_publisher.notify_subscribers()

    print(f"\nDetached: {type(new_publisher.detach()).__name__}")
    print(f"\nSubscribers: {new_publisher.subscribers()}")

    new_publisher.add_news("My second news!")
    new_publisher.notify_subscribers()


if __name__ == '__main__':
    main()
