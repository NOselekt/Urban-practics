#1

def print_params(a = 256, b = '512', c = False):
    print(a, b , c)

print_params(128, '256', True)
print_params(128, True)
print_params(c = True)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

#2

values_list = [64, 128.64, '256']
values_dict = {'a': 64, 'b': 128.64, 'c': '256'}

print_params(*values_list)
print_params(**values_dict)

#3

values_list_2 = ['32', 64.16]
print_params(*values_list_2, 42)