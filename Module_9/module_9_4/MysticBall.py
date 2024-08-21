import random

class MysticBall:
    def __init__(self, *words: str):
        if any(not isinstance(element) for element in words):
            raise TypeError
        else:
            self.words = tuple([element for element in words])

    def __call__(self):
        return random.choice(self.words)

try:
    first_ball = MysticBall('Да', 'Нет', 'Наверное')
    print(first_ball())
    print(first_ball())
    print(first_ball())
except TypeError:
    print('Введённые данные неверного типа, живите с этим')