class Car:

    def __init__(self, model: str, vin: int, numbers: str):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers


    def __is_valid_vin(self, vin):
        if isinstance(vin, int):
            if 1000000 <= vin <= 9999999:
                return True
            else:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
        raise IncorrectVinNumber('Vin должен быть числом')

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str):
            if len(numbers) == 6:
                return True
            else:
                raise IncorrectCarNumbers('Неверное количество знаков в номере машины')
        raise IncorrectCarNumbers('Номер машины должен быть строкой')


class IncorrectVinNumber(Exception):
    def __init__(self, message: str = 'Incorrect VIN'):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message: str = 'Incorrect car numbers'):
        self.message = message