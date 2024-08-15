def custom_write(file_name: str, strings: list):
    file = open(file_name, 'r', encoding='utf-8')
    file_viscera = file.read()
    file.close()

    file = open(file_name, 'a', encoding='utf-8')
    if file_viscera:
        file.write('\n')

    string_positions = {}

    for string in strings:
        file_viscera += string + '\n'
        string_positions[(file_viscera.count('\n'), file.tell())] = string
        file.write(string + '\n')

    file.close()

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


