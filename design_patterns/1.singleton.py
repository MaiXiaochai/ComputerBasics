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

    todo:
    super的含义和用法：https://www.runoob.com/w3cnote/python-super-detail-intro.html
"""


class Singleton:
    def __new__(cls, *args, **kwargs) -> object:
        if not hasattr(cls, 'instance'):
            instance_obj = super().__new__(cls, *args, **kwargs)
            setattr(cls, 'instance', instance_obj)

        return getattr(cls, 'instance')


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    print(f"s1 is s2: {s1 is s2}")
