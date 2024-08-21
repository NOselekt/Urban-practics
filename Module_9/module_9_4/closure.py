
def get_advanced_writer(file_name: str):
    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            print(*data_set, file=file, sep='\n')
    return write_everything


try:
    write = get_advanced_writer('example.txt')
    write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
except TypeError:
    print('Введённые данные неверного типа, живите с этим')