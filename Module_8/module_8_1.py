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
