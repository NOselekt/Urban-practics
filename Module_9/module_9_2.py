first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [length for length in list(map(len, first_strings)) if length > 5]
second_result = [(word_1, word_2) for word_1 in first_strings for word_2 in second_strings if len(word_1) == len(word_2)]
third_result = {string: len(string) for string in (first_strings + second_strings) if not len(string) % 2}

print(first_result)
print(second_result)
print(third_result)