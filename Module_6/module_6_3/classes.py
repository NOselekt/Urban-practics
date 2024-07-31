class Horse:

    def __init__(self):
        super().__init__()
        self._x_distance = 0
        self.__sound = 'Frrr'

    def run(self, dx):
        self._x_distance += dx


class Eagle:

    def __init__(self):
        self._y_distance = 0
        self.__sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy):
        self._y_distance += dy

    def sound(self):
        return self.__sound

class Pegasus(Horse, Eagle):

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_position(self):
        return (self._x_distance, self._y_distance)

    def voice(self):
        return self.sound()

