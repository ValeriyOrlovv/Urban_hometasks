from threading import Thread
from time import sleep


class Knight(Thread):

    enemies = 100
    days = 0
    
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies != 0:
            self.enemies -= self.power
            self.days += 1
            sleep(1)
        print(f'{self.name} сражается {self.days}..., осталось {self.enemies} воинов.')
            



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()
