from classes import Sedan



vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('crimson')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
