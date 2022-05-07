"""
------------------------------------------
@File       : 1.singleton.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2022/4/29 11:25
------------------------------------------
    单例模式：确保类有且仅有一个特定类型的对象，并提供全局访问点，控制共享资源的并行访问
    应用场景：
        + 日志记录
        + 数据库操作
        + 打印机后台处理程序


    super的含义和用法：https://www.runoob.com/w3cnote/python-super-detail-intro.html
"""


class Singleton:
    """
        1.单例模式
    """

    def __new__(cls, *args, **kwargs) -> object:
        if not hasattr(cls, 'instance'):
            instance_obj = super().__new__(cls, *args, **kwargs)
            setattr(cls, 'instance', instance_obj)

        return getattr(cls, 'instance')


class SingletonLazy:
    """
        2.单例模式中，懒汉式实例化
    """
    __instance = None

    def __init__(self):
        if not SingletonLazy.__instance:
            print("__init__ method called ..")

        else:
            print(f"Instance already created: ", self.get_instance())

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = SingletonLazy()

        return cls.__instance

    @staticmethod
    def demo2():
        pass


"""
    3.模块级别的单例:
        默认情况下，所有的模块都是单例，这是由 Python的导入行为所决定的:
        1. 检查一个Python模块是否已经导入
        2.  如果已经导入，则返回该模块的对象。如果没有导入，则导入该模块，并实例化
"""


class MonostateSingleton:
    """
        4.单状态单例, 让实例共享相同的状态
        将实例的__dict__用公用的类的dict类型变量存储
    """
    __shared_state = dict()

    def __init__(self):
        self.__dict__ = self.__shared_state


class MonostateSingleton2:
    """
        4.2 通过 __new__实现但状态
    """
    __shared_state = dict()

    def __new__(cls, *args, **kwargs):
        obj = super(MonostateSingleton2, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj


class MetaSingleton(type):
    """
        元类实现的单例
        TODO:这种单例的实现还得仔细多看看
    """
    __instance = dict()

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)

        return cls.__instance[cls]


class Logger(metaclass=MetaSingleton):
    pass


def demo_singleton():
    s1 = Singleton()
    s2 = Singleton()
    print(f"s1 is s2: {s1 is s2}")


def demo_lazy():
    s3 = SingletonLazy()
    s3.get_instance()
    s4 = SingletonLazy()


def demo_monostate():
    m = MonostateSingleton()
    m1 = MonostateSingleton()
    m.x = 4

    print(f"'m': {m}")
    print(f"'m1': {m1}")
    print(f"m.__dict__: {m.__dict__}")
    print(f"m1.__dict__: {m1.__dict__}")


def demo_monostate2():
    m = MonostateSingleton()
    m1 = MonostateSingleton()
    m.x = 4

    print(f"'m': {m}")
    print(f"'m1': {m1}")
    print(f"m.__dict__: {m.__dict__}")
    print(f"m1.__dict__: {m1.__dict__}")


def demo_meta_singleton():
    log1 = Logger()
    log2 = Logger()
    print(log1, log2)


def main():
    # demo_singleton()
    # demo_lazy()
    # demo_monostate()
    demo_monostate2()


if __name__ == '__main__':
    main()
