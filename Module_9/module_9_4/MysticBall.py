import random
from typing import TypeVar
Collections = TypeVar('A', list, tuple, set)


class MysticBall:
    def __init__(self, *words: Collections):
        self.words = tuple([element for element in words])

    def __call__(self):
        return random.choice(self.words)

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())