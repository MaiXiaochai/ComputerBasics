"""
------------------------------------------
@File       : 4.proxy_pattern2.py
@CreatedOn  : 2022/6/30 14:23
------------------------------------------
    代理模式《精通Python设计模式》中案例代码
        虚拟代理：用于懒初始化，将一个大计算量对象的创建延迟到真正需要的时候进行
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

    def __get__(self, obj, cls):
        if not obj:
            return None

        value = self.method(obj)
        setattr(obj, self.method_name, value)

        return value


class Test:
    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    @LazyProperty
    def resource(self):
        # 注意：__get__访问方法的重写使得resource()方法可以当做一个变量（可以使用t.resource代替t.resource()）
        print(f"Initializing self._resource which is: {self._resource}")
        self._resource = tuple(range(5))  # 假设这一行的计算成本比较大

        return self._resource


def main():
    """
    foo
    bar
    Initializing self._resource which is: None
    (0, 1, 2, 3, 4)
    (0, 1, 2, 3, 4)
    """
    t = Test()
    print(t.x)
    print(t.y)

    print(t.resource)
    print(t.resource)


if __name__ == '__main__':
    main()
