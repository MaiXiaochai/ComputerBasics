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

    def execute(self):
        pass


class ConcreteCommand(Command):
    def execute(self):
        self.recv.action()
