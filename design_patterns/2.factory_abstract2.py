"""
------------------------------------------
@File       : 2.factory_abstract2.py
@CreatedOn  : 2022/6/24 17:00
------------------------------------------
    抽象工厂设计模式是抽象方法的一种泛华。
    概括来说，一个抽象工厂是（逻辑上）一组工厂方法，其中的每个工厂方法负责产生不同种类的对象

    优点：
        1）对象的创建更容易追踪
        2）对象创建和使用解耦
        3）提供优化内存占用和应用性能的潜力
        4）能通过改变激活的工厂方法动态地（运行时）改变应用行为
            经典例子:北部公共让用户在使用应用时改变应用的观感（比如，Apple风格和 Windows风格等），

    何时使用工厂方法，何时又该使用抽象工厂？
        1）通常一开始时使用工厂方法，因为它简单。
        2）如果后来发现应用需要许多工厂方法，那么将创建一系列对象的过程合并到一起更合理，从而最终引入抽象工厂

    例子：应用内置彩蛋-小游戏，包含两个，一个面向孩子，一个面向成人
        1）孩子的游戏：游戏名FrogWorld。主人公是一只青蛙，喜欢吃虫子。
        2）每个英雄都需要一个好名字，在程序运行时，由用户给定。
        3）interact_with()用于描述青蛙与障碍物（比如，虫子、迷宫或者其它青蛙）之前的交互

        todo: 两层抽象已完成，正在进行对比中
"""
from abc import ABCMeta, abstractmethod


class CharacterFactory(metaclass=ABCMeta):
    @abstractmethod
    def interact_with(self, obstacle):
        pass


class ObstacleFactory(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def action():
        pass


class Frog(CharacterFactory):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        """
            frog:       青蛙
            encounter:  遇到，遭遇，偶遇，邂逅
        """
        print(f'{self} the Frog encounters {obstacle} and {obstacle.action()}!')


class Bug(ObstacleFactory):
    def __str__(self):
        return 'a bug'

    @staticmethod
    def action():
        return 'eats it'


class FrogWorld:
    """
        FrogWorld是一个抽象工厂，其主要职责是创建游戏的主人公和障碍物。
        区分创建方法并使其名字通用(比如，make_character()和 make_obstacle())，
        这让我们可以动态改变当前激活的工厂(也因此改变了当前激活的游戏)，而无需进行任何代码变更。
        * 在一些静态语言中，抽象工厂是一个抽象类/接口，具备一些空方法，但在Python中，无需如此，因为类型是在运行时检测的。
    """

    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return f"\n\n\t{'Frog World'.center(50, '-')}"

    def make_character(self):
        return Frog(self.player_name)

    @staticmethod
    def make_obstacle():
        return Bug()


class Wizard(CharacterFactory):
    """
        wizard 巫师
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print(f"{self} the Wizard battles against {obstacle} and {obstacle.action}!")


class Ork(ObstacleFactory):
    """
        Ork: 半兽人
    """

    def __str__(self):
        return 'an evil ork'

    @staticmethod
    def action():
        return "kills it"


class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return f"\n\n\t{'Wizard World'.center(50, '-')}"

    def make_character(self):
        return Wizard(self.player_name)

    @staticmethod
    def make_obstacle():
        return Ork()

