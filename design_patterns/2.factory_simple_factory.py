"""
------------------------------------------
@File       : 2.factory_simple_factory.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2022/5/9 14:36
------------------------------------------
    工厂模式

    这里以玩具制造公司为例。假设公司里的一台机器正在制造玩具车。现在CEO迫切要求需要根据市场的需求来制造玩偶。此时，工厂模式就派上大用场了。
    这种情况下，
        机器成为了接口
        CEO是客户端 -- 只关心要制造的对象（玩具）和创建对象的接口（机器）

    简单工厂模式：
        客户端类使用的是Factory类，该类具有create_type()方法。
        当客户端使用类型参数调用create_type()方法是，Factory会根据传入的参数，返回Product1或Product2

        这里用动物叫声的代码来进一步理解简单工厂模式

"""
from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!")


class Cat(Animal):
    def do_say(self):
        print("Meow Meow!")


class ForestFactory:
    """
        forest factory 定义
        简单工厂模式（对很多人来说，简单工厂本身并不是一种模式）
    """

    @staticmethod
    def make_sound(object_type):
        animals = {
            'dog': Dog,
            'cat': Cat
        }
        return animals.get(object_type.lower())().do_say()


if __name__ == '__main__':
    # client code
    ff = ForestFactory()

    animal = input("Which animal should make_sound Dog or Cat?\n")
    ff.make_sound(animal)
