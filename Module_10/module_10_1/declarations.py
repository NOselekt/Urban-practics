from os.path import exists
from typing import Callable
from datetime import datetime
import threading
import time
import random

WORDS_LIST = ['python', 'c++', 'c#', 'java', 'pascal', 'cobol', 'c', 'brainfuck'] #список слов для записи


#создаю подкласс класса Thread, который возвращает значение выполняемой функции
class ReturningThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name, args=args,
                         kwargs=kwargs, daemon=daemon)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, timeout=None):
        super().join(timeout=timeout)
        return self._return


#декоратор для подсчёта времени выполнения функции
def time_record(func: Callable):
    def record(*args):
        start = time.time()
        func(*args)
        finish = time.time()
        return finish - start
    return record

#функция, записывающая слова в файл
@time_record
def write_words(word_count: int, file_name: str):
    word = WORDS_LIST[random.randint(0, len(WORDS_LIST) - 1)] #выбираем случайное слово
    words_counter = 0

    with open(file_name, 'a+') as file:
        for i in range(word_count):
            file.write(word)
            words_counter += 1
            time.sleep(0.1)
            print(f'Какое-то слово №{words_counter}')
    print(f'Завершилась запись в файл {file_name}')
    file.close()
