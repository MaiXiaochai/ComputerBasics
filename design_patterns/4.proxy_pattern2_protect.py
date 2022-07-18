"""
------------------------------------------
@File       : 4.proxy_pattern2_protect.py
@CreatedOn  : 2022/7/15 14:23
------------------------------------------
    实现一个简单的保护代理来查看核添加用户，功能如下
        查看用户列表：这一操作不需要特殊权限
        添加新用户：这一操作要求客户端提供一个特殊的密码
"""


class SensitiveInfo:
    """
        包含我们希望保护的信息
    """

    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    def read(self):
        print(f'There are {len(self.users)} users:{self.users}')

    def add(self, user):
        self.users.append(user)
        print(f'Added user {user}')


class Info:
    """ SensitiveInfo的保护代理"""

    def __init__(self):
        """
            以下self.secret保存了明文密码，这里是为了简化。现实中，永远不要执行以下操作
                在源代码中存储密码
                以明文形式存储密码
                使用一种弱（例如，MD5）或自定义加密形式
        """
        self.protected = SensitiveInfo()
        self.secret = '0xdeadbeef'

    def read(self):
        self.protected.read()

    def add(self, user):
        sec = input('what is the secret?')
        self.protected.add(user) if sec == self.secret else print("That's wrong!")


def main():
    info = Info()

    while True:
        print('\n1.read list \n2.add user \n3.quit\n')
        key = input('choose option: ')

        if key == '1':
            info.read()

        elif key == '2':
            name = input('input username: ')
            info.add(name)

        elif key == 3:
            exit()


if __name__ == '__main__':
    main()
