"""
------------------------------------------
@File       : 6.command_pattern_stock.py
@CreatedOn  : 2022/7/26 10:07
------------------------------------------
    命令模式：股票交易案例
"""
from abc import ABCMeta, abstractmethod


class Order(metaclass=ABCMeta):
    """Command"""

    @abstractmethod
    def execute(self):
        pass


class BuyStockOrder(Order):
    """ConcreteCommand"""

    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


class SellStockOrder(Order):
    """ConcreteCommand"""

    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


class StockTrade:
    """Receiver"""

    @staticmethod
    def buy():
        print("You will buy stocks")
 
    @staticmethod
    def sell():
        print("You will sell stocks")


class Agent:
    """Invoker"""

    def __init__(self):
        self.__order_queue = []

    def place_order(self, order):
        self.__order_queue.append(order)
        order.execute()


def main():
    # Client
    stock = StockTrade()
    buy_stock = BuyStockOrder(stock)
    sell_stock = SellStockOrder(stock)

    # Invoker
    agent = Agent()
    agent.place_order(buy_stock)
    agent.place_order(sell_stock)


if __name__ == '__main__':
    main()
