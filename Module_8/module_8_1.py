def add_everything_up(*summands):
    result = summands[0]

    for summand in summands[1:]:
        try:
            result += summand
        except TypeError:
            result = str(result) + str(summand)

    return result

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))