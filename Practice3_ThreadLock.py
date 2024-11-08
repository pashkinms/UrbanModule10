import threading
import time
from random import randint

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.transaction_number = 100

    def deposit(self):
        counter = 0
        while counter < self.transaction_number:
            request = randint(50,500)
            if self.lock.locked() and self.balance >= 500:
                self.lock.release()
            self.balance += request
            print(f'Пополнение: {request}. Текущий баланс: {self.balance}')
            time.sleep(0.001)
            counter += 1

    def take(self):
        counter = 0
        while counter < self.transaction_number:
            request = randint(50, 500)
            print(f'Запрос на: {request}')
            if request <= self.balance:
                self.balance -= request
                print(f'Снятие: {request}. Текущий баланс: {self.balance}')
            else:
                print(f'Запрос отклонен. Недостаточно средств.')
                self.lock.acquire()
            time.sleep(0.001)
            counter += 1




bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')