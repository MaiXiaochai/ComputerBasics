"""
------------------------------------------
@File       : 3.facade_pattern.py
@CreatedOn  : 2022/6/28 14:31
------------------------------------------
    Facade Pattern，门面模式

    例子：准备一场婚礼
        Eventmanager扮演了门面的角色，并简化了你的工作
        Facade 与 子系统进行交流，代表你为婚礼完成所有的预订和准备工作

    将门面模式与真实世界场景相关联
        EventManager：   简化类接口的门面，通过组合创建子系统的对象，如Hotelier、Caterer，等等

    设计原理：
        最少知识原则：减少对象之间的交互，就像跟亲近的只有某几个朋友那样
            + 在设计系统时，对于创建的每个对象，都应该考察与之交互的类的数量，以及交互的方式
            + 遵循这个原则，就能够避免创建许多彼此机密耦合的类的情况
            + 如果类之间存在大量依赖关系，那么系统就会变得那一维护。如果对系统中的任何一部分进行修改，都可能导致系统的其它部分被无意改变，
              这意味着系统会退化，是应该间距避免的
"""


class Eventmanager:

    def __init__(self):
        """
        folk:       家庭，父老乡亲，家庭成员
        caterer:    宴会负责人
        """
        self.musician = None
        self.carter = None
        self.florist = None
        self.hotelier = None
        print(f"Event manager: Let me talk to the folks\n")

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.book_hotel()

        self.florist = Florist()
        self.florist.set_flower_requirements()

        self.carter = Caterer()
        self.carter.set_cuisine()

        self.musician = Musician()
        self.musician.set_music_type()


class Hotelier:
    def __init__(self):
        print(f"Arranging the Hotel for Marriage? --")

    @staticmethod
    def _is_available():
        print("Is the Hotel free for the event on given day?")
        return True

    def book_hotel(self):
        if self._is_available():
            print("Registered the Booking\n\n")


class Florist:
    def __init__(self):
        print("Flower Decorations for the Event? --")

    @staticmethod
    def set_flower_requirements():
        """
            Carnations， 康乃馨
        """
        print("Carnations, Roses and Lilies would be used for Decorations\n\n")


class Caterer:
    def __init__(self):
        print("Food Arrangements for the Event --")

    @staticmethod
    def set_cuisine():
        """
            Continental，欧式
        """
        print("Chinese & Continental Cuisine to be served\n\n")


class Musician:
    def __init__(self):
        print("Musician Arrangements for the Marriage --")

    @staticmethod
    def set_music_type():
        print("Jazz and Classical will be played\n\n")


class You:
    def __init__(self):
        print("You: Whoa! Marriage Arrangements?!")

    @staticmethod
    def ask_eventmanager():
        print("You: Let's Contact the Event Manager\n\n")
        em = Eventmanager()
        em.arrange()

    def __del__(self):
        print("You: Thanks to Event manager, all preparations done! Phew!")


if __name__ == '__main__':
    you = You()
    you.ask_eventmanager()
