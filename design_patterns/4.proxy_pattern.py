"""
------------------------------------------
@File       : 4.proxy_pattern.py
@CreatedOn  : 2022/6/28 22:39
------------------------------------------
    代理模式
    代码案例：演员和他的经纪人
        当制作公司想要找演员拍电影时，他们通常会与经纪人交流，而不是直接跟演员交流。
        经纪人会根据演员的日程安排和其它合约情况，来答复制作公司该演员是否有空，以及是否对该影片感兴趣。
        在这种情况下，制作公司并不直接找演员交涉，而是通过经纪人作为代理，处理所有与演员有关的调度和片酬问题。
"""


class Actor:
    def __init__(self):
        self.is_busy = False

    def occupied(self):
        self.is_busy = True
        print(f"{type(self).__name__} is occupied with current movie")

    def available(self):
        self.is_busy = False
        print(f"{type(self).__name__} is free for the movie")

    def get_status(self):
        return self.is_busy


class Agent:
    def __init__(self):
        self.actor = None
        self.principal = None

    def work(self):
        self.actor = Actor()
        if self.actor.get_status():
            self.actor.occupied()

        else:
            self.actor.available()


if __name__ == '__main__':
    r = Agent()
    r.work()
