import threading


class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        if name:
            self.__name = name
        else:
            raise NameError('У рыцаря должно быть имя!')
        if power > 0:
            self.__power = power
        else:
            raise NameError('У рыцаря должна быть сила больше нуля!')


    def run(self):
        print(f'{self.__name}, На нас напали!')
        day = 0
        for i in range(0, 100, self.__power):
            day += 1
            print(f'{self.__name} сражается {day}-й день. Осталось врагов: {100 - i}')
        print(f'{self.__name} одержал победу на {day}-й день!')
