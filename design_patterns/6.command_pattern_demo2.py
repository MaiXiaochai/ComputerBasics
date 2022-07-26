"""
------------------------------------------
@File       : 6.command_pattern_demo2.py
@CreatedOn  : 2022/7/25 16:43
------------------------------------------
    命令模式：案例2
"""

from abc import ABCMeta, abstractmethod


class Command(metaclass=ABCMeta):
    def __init__(self, recv):
        self.recv = recv

    @abstractmethod
    def execute(self):
        pass


class ConcreteCommand(Command):
    def execute(self):
        self.recv.action()


class Receiver:
    @staticmethod
    def action():
        print("Receiver Action")


class Invoker:
    def __init__(self):
        self.cmd = None

    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()


def main():
    recv = Receiver()
    cmd = ConcreteCommand(recv)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()


if __name__ == '__main__':
    main()
