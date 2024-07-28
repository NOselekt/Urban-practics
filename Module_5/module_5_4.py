from module_5_1.House import House

h1 = House('RC Elbrus', 10)
print(House.houses_history)
h2 = House('RC Acacia', 20)
print(House.houses_history)
h3 = House('RC Matryoshki', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)