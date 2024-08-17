from os.path import exists

def custom_write(file_name: str, strings: list):
    strings_count = 0
    if exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            strings_count = file.read().count('\n')
    with open(file_name, 'a', encoding='utf-8') as file:
        string_positions = {}

        for string in strings:
            strings_count += 1
            string_positions[(strings_count, file.tell())] = string
            file.write(string + '\n')

    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)


