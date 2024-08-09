def add_everything_up(*summands):
    if isinstance(summands[0], int):
        result = 0
    else:
        result = ''

    for summand in summands:
        try:
            result += summand
        except TypeError:
            result = str(result) + str(summand)

    return result


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

'''
def add_everything_up(*summands):
    if isinstance(summands[0], int):
        result = 0
    else:
        result = ''

    length = len(summands)

    try:
        for i in range(length):
            result += summands[i]
    except TypeError:
        result = str(result)
        for j in range(i, length):
            result += str(summands[j])

    return result

Лучше оптимизация (?) XD, но не намного
При двух миллионах простеньких аргументов разница - 3 секунды)
'''



print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))