"""
------------------------------------------
@File       : 1.singleton_demo1.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2022/5/7 15:20
------------------------------------------
    单例模式用例：数据库应用

    完整的、对数据库进行多种兑取和写入操作的云服务，分解为多个服务，每个服务执行不同的数据库操作。
    针对UI(Web应用程序)上的操作将导致调用API，最终产生相应的DB操作。
    很明显，跨越不同服务的共享资源时数据库本身。因此，有如下设计要求

        1.数据库中操作的一致性，即一个操作不应与其它操作发生冲突
        2.优化数据库的各种操作，以提高内存和CPU效率
"""
import sqlite3


class MetaSingleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)

        return cls.__instances[cls]


class DataBase(metaclass=MetaSingleton):
    connection = None

    def __init__(self):
        self.cursor = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlit3")
            self.cursor = self.connection.cursor()

        return self.cursor


def main():
    db1 = DataBase().connect()
    db2 = DataBase().connect()

    print(f"DataBase Object DB1: ", db1)
    print(f"DataBase Object DB2: ", db2)


if __name__ == '__main__':
    main()
