from classes import Predator, Mammal, Flower, Fruit


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.get_name())
print(p1.get_name())

print(a1.is_alive())
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.is_alive())
print(a2.fed)