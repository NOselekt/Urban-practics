import random
import threading
import time


class Bank:
    def __init__(self):
        self.__balance = 0
        self.__lock = threading.Lock()

    def get_balance(self):
        return self.__balance

    def deposit(self):
        for i in range(100):
            if self.__balance >= 500 and self.__lock.locked():
                self.__lock.release()
            value = random.randint(50, 500)
            self.__balance += value
            print(f'Пополнение: {value}. Баланс: {self.__balance}')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            value = random.randint(50, 500)
            print(f'Запрос на {value}')
            if value <= self.__balance:
                self.__balance -= value
                print(f'Снятие: {value}. Баланс: {self.__balance}')
            else:
                print('Запрос отклонён, недостаточно средств.')
                self.__lock.acquire()