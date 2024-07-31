class Living_Being:
    def __init__(self, name):
        self._alive = True
        self._name = name

    def is_alive(self):
        return self._alive

    def death(self):
        self._alive = False

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

class Animal(Living_Being):

    def __init__(self, name):
        self._alive = True
        self.fed = False
        self._name = name

    def eat(self, food):
        if food.is_edible():
            print(f'{self._name} have eaten {food.get_name()}')
            self.fed = True
        else:
            print(f'{self._name} didn\'t eat {food.get_name()} and died')
            self.death()

class Plant(Living_Being):

    def __init__(self, name):
        self._alive = True
        self._edible = False
        self._name = name

    def is_edible(self):
        return self._edible

class Mammal(Animal):
    pass

class Predator(Animal):
    pass

class Flower(Plant):
    pass

class Fruit(Plant):

    def __init__(self, name):
        self._alive = True
        self._edible = True
        self._name = name

