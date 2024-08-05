from math import pi, sqrt

class Figure:
    _sides_count = 0

    def __is_valid_color(self, colors):
        if len(colors) == 3 and all(0 <= color <= 255 for color in colors):
            return True
        return False

    def __is_valid_sides(self, *sides):
        if len(sides) == self._sides_count and all(side > 0 for side in sides):
            return True
        return False

    def __init__(self, colors, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides = [side for side in sides]
        else:
            self.__sides = [1 for i in range(self._sides_count)]
        if self.__is_valid_color(colors):
            self.__color = tuple(color for color in colors)
        filled = True

    def get_color(self):
        return self.__color

    def set_color(self, new_colors):
        if self.__is_valid_color(new_colors):
            self.__color = tuple(color for color in new_colors)

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = [side for side in new_sides]

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    _sides_count = 1
    def __init__(self, colors, *sides):
        super().__init__(colors, *sides)
        self.__radius = len(self) / 2 / pi

    def get_square(self):
        return pi * self.__radius ** 2

class Triangle(Figure):
    _sides_count = 3

    def __init__(self, colors, *sides):
        super().__init__(colors, *sides)
        self.__height_1 = 2 * self.get_square() / self.get_sides()[0]

    def get_square(self):
        return sqrt(len(self) * (len(self) - self.get_sides()[0]) * \
                                   (len(self) - self.get_sides()[1]) * (len(self) - self.get_sides()[2]))


class Cube(Figure):
    _sides_count = 12

    def __init__(self, colors, side):
        super().__init__(colors, side)
        self.set_sides(*((side,)*self._sides_count))

    def get_volume(self):
        return self.get_sides()[0]**3