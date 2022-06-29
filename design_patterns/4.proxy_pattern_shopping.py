"""
------------------------------------------
@File       : 4.proxy_pattern_shopping.py
@CreatedOn  : 2022/6/29 11:26
------------------------------------------
    代理模式：刷借记卡买东西的案例

    主题是由代理和真实主题实现的接口。
    在这里，主题是PayMent类，他是一个抽象基类，代表一类接口。
    付款具有一个do_pay()方法，该方法需要借助代理和真实主题来实现。
    Bank代表真实主题，代理使用 set_card()方法将借记卡详细信息发送给银行

    DebitCard类充当真实主题（银行）的代理
"""

from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    """主题"""

    @abstractmethod
    def do_pay(self):
        pass


class Bank(Payment):
    """真实主题"""

    def __init__(self):
        self.card = None
        self.account = None

    def __get_account(self):
        """
           用于获取借记卡的相信信息，为了简单起见，我们强制使用与账号相同的借记卡号
        """
        self.account = self.card
        return self.account

    def __has_funds(self):
        """用于查看账户持有人在账户中是否有足够的资金来付款"""
        print(f"Bank: Checking if Account {self.__get_account()} has enough funds")
        return True

    def set_card(self, card):
        self.card = card

    def do_pay(self):
        """
            实际上负责根据可用资金向商家付款
            merchant：零售商
        """
        if self.__has_funds():
            print(f"Bank: Paying the merchant")
            return True

        else:
            print("Bank: Sorry, not enough funds!")
            return False


class DebitCard(Payment):
    """Bank的代理"""

    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input("Proxy: Punch in Card Number: ")
        self.bank.set_card(card)

        return self.bank.do_pay()


class You:
    def __init__(self):
        print("You: Lets buy the shirt")
        self.debit_card = DebitCard()
        self.is_purchased = None

    def make_payment(self):
        self.is_purchased = self.debit_card.do_pay()

    def __del__(self):
        """ Denim, 牛仔布的"""
        if self.is_purchased:
            print("You: Wow! Denim shirt is Mine :-")

        else:
            print("You: I should earn more :(")


if __name__ == '__main__':
    you = You()
    you.make_payment()
