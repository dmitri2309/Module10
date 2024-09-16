from threading import Thread
import time

class Knight(Thread):

    def __init__(self, name_, power):
        self.name_ = name_
        self.power = power
        super().__init__()

    def run(self):
        print(f'{self.name_} на нас напали!')
        days = 0
        warriors = 100
        while warriors > 0:
            time.sleep(1)
            warriors -= self.power
            days += 1
            print(f'{self.name_} сражается {days} день (дня), осталось {warriors} воинов')
        print(f'{self.name_} одержал победу спустя {days} дней (дня)')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)


threads = []
threads.append(first_knight)
threads.append(second_knight)

for knight in threads:
    knight.start()

for knight in threads:
    knight.join()
print('Все битвы закончились')