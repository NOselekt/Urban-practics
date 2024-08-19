first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(first_len - second_len) for first_len, second_len in zip(map(len, first), map(len, second))
                if first_len != second_len)
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))

print(list(first_result))
print(list(second_result))