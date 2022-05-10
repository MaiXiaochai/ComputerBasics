"""
------------------------------------------
@File       : 2.fatory_method.py
@Author     : maixiaochai
@Email      : maixiaochai@outlook.com
@CreatedOn  : 2022/5/9 16:03
------------------------------------------
    工厂方法模式
        + 定义一个接口来创建对象，但是工厂本省并不负责创建对象，而是将这一任务交由子类来完成，即子类决定了要实例化哪些类

        + Factory方法的创建是通过继承而不是通过实例化来完成的
        + 工厂方法使设计更加具有可定制性。
        + 它可以返回相同的实例或子类，而不是某种类型的对象（就像在简单工厂方法中的那样）

    大概结构：
        + 包含factoryMethod()方法的抽象类Creator
        + factoryMethod()方法负责创建指定类型的对象。
        + ConcreteCreator类提供一个实现Creator抽象类的factoryMethod(),这种方法可以在运行时修改已创建的对象
        + ConcreteCreator创建ConcreteProduct,并确保其创建的对象实现了Product类，同时为Product接口中的所有方法提供相应的实现
        + 简言之，Creator接口的factoryMethod()方法和ConcreteCreator类共同决定了要创建Product的那个子类。
        + 因此，工厂方法模式定义了一个接口来创建对象，但具体实例化哪个类则是由它的子类决定的

    例子：
        假设我们想在不同类型的社交网络上为个人或者公司建立简介。那么，每个简介都有某些特定的组成章节。
        比如，
            在LinkedIn的简介中，有一个章节是关于个人申请的专利或出版作品的。
            在Facebook上，你将在相册中看到最近度假地点的照片区。
        此外，在这两个简介中，都有一个个人信息的区。
        我们要通过将正确的区添加到相应的简介中来创建不同类型的简介。
"""
from abc import ABCMeta, abstractmethod


class Section(metaclass=ABCMeta):
    """
        Creator
        Section抽象基类定义一个区是关于哪方面内容的，尽量保持简洁
    """

    @abstractmethod
    def describe(self):
        """
        factoryMethod()抽象方法
        """
        pass


class PersonalSection(Section):
    def describe(self):
        """实现factoryMethod()方法"""
        print("Personal Section")


class AlbumSection(Section):
    def describe(self):
        print("Album Section")


class PatentSection(Section):
    def describe(self):
        print("Patent Section")


class PublicationSection(Section):
    def describe(self):
        print("Publication Section")


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.sections = []
        self.create_profile()

    @abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections

    def add_section(self, section):
        self.sections.append(section)


class LinkedIn(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(PatentSection())
        self.add_section(PublicationSection())


class FaceBook(Profile):
    def create_profile(self):
        self.add_section(PersonalSection())
        self.add_section(AlbumSection())


if __name__ == '__main__':
    """
        编写决定实例化哪个Creator类的客户端代码，以遍根据指定的选项创建所需的简介
    """
    profile_type = input("Which Profile you'd like to create? [LinkIn or FaceBook]")
    profiles = {
        'linkedin': LinkedIn,
        'facebook': FaceBook
    }
    profile = profiles.get(profile_type.lower())()
    print("Creating Profile ..", type(profile).__name__)
    print("Profile has sections --", profile.get_sections())
