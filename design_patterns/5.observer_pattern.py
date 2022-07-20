"""
------------------------------------------
@File       : 5.observer_pattern.py
@CreatedOn  : 2022/7/18 14:20
------------------------------------------
    观察者模式
"""


class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notify_all(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


class Observer1:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, f":: Got {args} from {subject}")


class Observer2:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, f":: Got {args} from {subject}")


def main():
    subject = Subject()
    observer1 = Observer1(subject)
    observer2 = Observer2(subject)
    subject.notify_all('notification')


if __name__ == '__main__':
    main()
