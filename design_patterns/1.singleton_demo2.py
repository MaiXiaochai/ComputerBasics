"""
------------------------------------------
@File       : 1.singleton_demo2.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2022/5/7 15:37
------------------------------------------
    单例模式(经典单例)：基础设施运行状态监控服务

    HealthCheck类，为单例。
    我们还要维护一个被监控的服务器列表。当一个服务器从这个列表中删除时，监控软件将从被监控的服务器列表中将其删除。
    使用add_server()方法将服务器添加到基础设施中，以进行运行状态检查。
    首先，通过迭代对这些服务器的运行状态进行检查。

    之后，change_server()方法会删除最后一个服务器，并向计划进行运行状态检查的基础设施中添加一个新服务器。
    因此，当运行状态检查进行第二次迭代时，它会使用修改后的服务器列表。

    综上，运行状态检查的工作必须由统一规格对象来完成
"""


class HealthCheck:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)

        return cls._instance

    def __init__(self):
        self.servers = []

    def add_server(self):
        for i in range(1, 5):
            self.servers.append(f"server {i}")

    def change_server(self):
        if self.servers:
            self.servers.pop()

        self.servers.append("auto add server")


def main():
    hc1 = HealthCheck()
    hc2 = HealthCheck()

    hc1.add_server()
    print("Schedule health check for servers (1) ..")
    for i in range(4):
        print(f"Checking: {hc1.servers[i]}")

    hc2.add_server()
    print("Schedule health check for servers (2) ..")
    for i in range(4):
        print(f"Checking: {hc2.servers[i]}")


if __name__ == '__main__':
    main()
