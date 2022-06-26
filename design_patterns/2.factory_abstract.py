"""
------------------------------------------
@File       : 2.factory_abstract.py
@CreatedOn  : 2022/5/11 21:44
------------------------------------------
    抽象工厂模式
        提供一个借口来创建一系列相关对象而无需指定/公开其具体类的接口
        该模式能够提供其它工厂的对象，在其内部创建其它对象
        不仅确保客户端与对象的创建相互隔离，同时还确保客户端能够使用创建的对象。但是，客户端只能通过借口访问对象

    这里以披萨店举例
        披萨店有印式披萨和美式披萨。我们先创建一个抽象基类 PizzaFactory。

        该方法提供两个抽象方法：create_ceg_pizza()和 create_non_veg_pizza()。他们需要通过ConcreteFactory实现。
        我们创造建了两个具体的工厂：IndiaPizzaFactory和 USPizzaFactory。

        然后让我们定义AbstractProducts。创建两个抽象基类: VegPizza和 NonVegPizza（AbstractProduct和 AnotherAbstractProduct）。
        他们都定义了自己的方法：prepare()和 serve()。
        这里的想法是：
            素食披萨饼：  配有适当的外皮、蔬菜和调味料
            非素食披萨饼：在素食披萨饼上面搭配非素食食材

    小结：
        1) 抽象工厂模式，在抽象的实现中用了其它的抽象的实现
        2) 印度人写的Python设计模式-第二版，这个抽象工厂模式代码写的很烂，还得让我自己改正，怎么写书的，无语
        3) 2022-06-24 PM
"""
from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_veg_pizza(self):
        """蔬菜披萨"""
        pass

    @abstractmethod
    def create_non_veg_pizza(self):
        """非蔬菜披萨"""
        pass


class IndianPizzaFactory(PizzaFactory):

    def create_veg_pizza(self):
        return DeluxVeggiePizza()

    def create_non_veg_pizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):

    def create_veg_pizza(self):
        return MexicanVegPizza()

    def create_non_veg_pizza(self):
        return HamPizza()


class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self):
        pass


class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self):
        pass


class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)


class ChickenPizza(NonVegPizza):
    def serve(self):
        print(type(self).__name__, "is served with Chicken on", VegPizza.__name__)


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print("Prepare ", type(self).__name__)


class HamPizza(NonVegPizza):
    def serve(self):
        print(type(self).__name__, "is served with Ham on ", VegPizza.__name__)


class PizzaStore:

    def __init__(self):
        self.veg_pizza = None
        self.non_veg_pizza = None
        self.factory = None

    def make_pizza(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.non_veg_pizza = self.factory.create_non_veg_pizza()
            self.veg_pizza = self.factory.create_veg_pizza()
            self.veg_pizza.prepare()
            self.non_veg_pizza.serve()
            print()


if __name__ == '__main__':
    pizza = PizzaStore()
    pizza.make_pizza()
