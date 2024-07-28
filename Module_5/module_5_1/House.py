import time

class House:
    name = ''
    number_of_floors = 0
    current_floor = 0
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.current_floor = 1

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('There\'s no such floor!')
            return 1
        if self.current_floor < new_floor:
            for i in range(self.current_floor, new_floor + 1):
                time.sleep(0.5)
                print(i)
            print('')
        elif self.current_floor > new_floor:
            for i in reversed(range(new_floor, self.current_floor + 1)):
                time.sleep(0.5)
                print(i)
            print('')
        else:
            print('You\'re already on this floor.\n')
        self.current_floor = new_floor
        return 0


    #Methods for 2nd exercise
    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'The name: {self.name}, number of floors: {self.number_of_floors}.'

