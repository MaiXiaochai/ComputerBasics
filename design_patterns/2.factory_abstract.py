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
        该方法提供两个抽象方法：create_ceg_pizza()和create_non_veg_pizza()。他们需要通过ConcreteFactory实现。
        我们创造建了两个具体的工厂：IndiaPizzaFactory和USPizzaFactory
"""
from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_veg_pizza(self):
        pass

    @abstractmethod
    def create_non_veg_pizza(self):
        pass

