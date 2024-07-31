from classes import Pegasus

p1 = Pegasus()

print(p1.get_position())
p1.move(10, 15)
print(p1.get_position())
p1.move(-5, 20)
print(p1.get_position())

print(p1.voice())
