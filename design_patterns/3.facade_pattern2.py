"""
------------------------------------------
@File       : 3.facade_pattern2.py
@CreatedOn  : 2022/6/28 15:56
------------------------------------------
    外观（门面）模式，Facade Pattern
    本质：在已有复杂系统之上实现的一个抽象层
    可以将骑车或者摩托车的钥匙视为一个外观，外观是激活一个系统的便捷方式，系统的内部则非常复杂

    《精通Python设计模式》多服务进程方式实现一个操作系统
"""
from enum import Enum
from abc import ABCMeta, abstractmethod

State = Enum('State', 'new running sleeping restart zombie')


class User:
    pass


class Process:
    pass


class File:
    pass


class Server(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self.name = None
        self.state = State.new

    def __str__(self):
        return self.name

    @abstractmethod
    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass


class FileServer(Server):
    def __init__(self):
        self.name = "FileServer"

    def boot(self):
        print(f"booting the {self}")
        self.state = State.running

    def kill(self, restart=True):
        print(f'Killing {self}')
        self.state = State.restart if restart else State.zombie

    @staticmethod
    def create_file(user, name, permissions):
        print(f"trying to create the file '{name}' for user '{user}' with permissions {permissions}")


class ProcessServer(Server):
    def __init__(self):
        self.name = 'ProcessServer'
        self.state = State.new

    def boot(self):
        print(f'booting the {self}')
        self.state = State.running

    def kill(self, restart=True):
        print(f"Killing {self}")
        self.state = State.restart if restart else State.zombie

    @staticmethod
    def create_process(user, name):
        print(f"trying to create the process '{name}' for user '{user}'")


class WindowServer:
    pass


class NetworkServer:
    pass


class OperatingSystem:
    """外观"""

    def __init__(self):
        self.fs = FileServer()
        self.ps = ProcessServer()

    def start(self):
        [i.boot() for i in (self.fs, self.ps)]

    def create_file(self, user, name, permissions):
        return self.fs.create_file(user, name, permissions)

    def create_process(self, user, name):
        return self.ps.create_process(user, name)


def main():
    os = OperatingSystem()
    os.start()
    os.create_file('Tom', 'hello', '-rw-r-r')
    os.create_process('Jerry', 'ls /tmp')


if __name__ == '__main__':
    main()
