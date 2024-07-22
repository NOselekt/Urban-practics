immutable_var = 25, 25.0, 'na', 'de', 'b', True
print(immutable_var)

'''
immutable_var[0] = 1 - TypeError: 'tuple' object does not support item assignment
Кортеж - неизменяемый тип данных, попытка поменять его элементы вызовет ошибку.
'''

mutable_list = [25, 25.0, 'na', 'de', 'b', False]

print(mutable_list)

mutable_list[-1] = True

print(mutable_list)