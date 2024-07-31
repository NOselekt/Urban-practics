class Vehicle:
    __COLOR_VARIANTS = ['red', 'blue', 'black', 'white', 'grey', 'green', 'purple', 'pink']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'The model: {self.__model}'

    def get_engine_power(self):
        return f'The engine power: {self.__engine_power}'

    def get_color(self):
        return f'The colour: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_engine_power())
        print(self.get_color())
        print(f'The owner: {self.owner}')

    def set_color(self, new_color):
        new_color = new_color.lower()
        if new_color in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f'You can\'t change the colour to {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
