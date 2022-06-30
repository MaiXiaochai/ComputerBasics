"""
------------------------------------------
@File       : 4.proxy_pattern2.py
@CreatedOn  : 2022/6/30 14:23
------------------------------------------
    代理模式《精通Python设计模式》中案例代码
        虚拟代理：用于懒初始化，讲一个大计算量对象的创建延迟到真正需要的时候进行
"""


class LazyProperty:
    """
        用作装饰器，当修饰某个特性时，LazyProperty惰性地（首次使用时）加载特性，而不是立即进行。
    """

    def __init__(self, method):
        """
            method：         实际方法的别名
            method_name:    该方法名称的别名
        """
        self.method = method
        self.method_name = method.__name__

