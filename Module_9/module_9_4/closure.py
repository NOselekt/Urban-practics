import pickle

def get_advanced_writer(file_name: str):
    def write_everything(*data_set):
        with open(file_name, 'a') as file:
            print(*data_set, file=file, sep='')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])