"""
------------------------------------------
@File       : 6.command_pattern.py
@CreatedOn  : 2022/7/25 10:22
------------------------------------------
    命令设计模式
        应用：程序安装向导
             打印机后台处理程序

    代码案例：
        开发一个安装向导，或者更常见的安装程序。
        通常，安装意味着需要根据用户做出的选择来复制或移动文件系统中的文件。
        创建 Wizard对象，然后使用preferences()方法存储用户在向导的各个步骤做出的选择。
        在向导 中点击Finish按钮时，就会调用execute()方法，之后，execute()方法将会根据首选项来开始安装
"""


class Wizard:
    """
        wizard 向导程序；男巫
    """

    def __init__(self, src, root_dir):
        self.choices = []
        self.root_dir = root_dir
        self.src = src

    def preferences(self, command):
        self.choices.append(command)

    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print(f"Copying binaries --, {self.src} to {self.root_dir}")

            else:
                print("No Operation")


def main():
    """Client Code"""
    wizard = Wizard('python3.5.gzip', '/usr/bin')
    # Users chooses to install Python only
    wizard.preferences({'python': True})
    wizard.preferences({'java': False})
    wizard.execute()


if __name__ == '__main__':
    main()
