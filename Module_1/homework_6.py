my_dict = {'Python': 1, 'Java': 3, 'C#': 3, 'C++': 5}
print('Dictionary:', my_dict)
print('Existing', my_dict['Python'])
print('Non-existent:', my_dict.get('PHP'))
my_dict.update({'PHP': 2, 'Pascal': 0})
print('Deleted value:', my_dict.pop('Python'))
print('New dictionary:', my_dict)

my_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 5, 7}
print('Set:', my_set)
my_set.update({11, 13})
my_set.discard(0)
print('New set:', my_set)