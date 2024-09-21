import threading
from random import randint
import time


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            dep_amount = randint(50, 500)
            self.balance += dep_amount
            print(f'Пополнение: {dep_amount}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            take_amount = randint(50, 500)
            print(f'Запрос на {take_amount}')
            if self.balance >= take_amount:
                self.balance -= take_amount
                print(f'Снятие {take_amount}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонен, недостаточно средств')
                self.lock.acquire()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
