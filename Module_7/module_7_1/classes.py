class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        result = f'{self.name}, {self.weight}, {self.category}'
        return result


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        result = file.read()
        file.close()
        return result

    def add(self, *products):
        file_for_read = open(self.__file_name, 'r')
        file_viscera = file_for_read.read()
        # сначала считываем, что уже есть в файле
        # это необходимо, так как будем не просто добавлять в файл продукты, но и редактировать знаки препинания,
        # то есть понадобится перезаписывать файл
        file_viscera = file_viscera.replace('.', '')
        file_for_read.close()
        # убираем точку в конце, чтобы добавить новые продукты через запятую
        for product in products:
        # проходимся по списку продуктов
            if product.name not in file_viscera:
                file_viscera += f'{product.name}, '
                # добавляем продукт не сразу в файл, а сначала в отдельную переменную, куда уже записали изначальный файл
            else:
                print(f'{product.name} is already in the magazine.')

        if file_viscera[-2:] == ', ':
            file_for_write = open(self.__file_name, 'w')
            file_for_write.write(file_viscera[:-2] + '.')
            file_for_write.close()
        # в конце, если мы хоть что-то добавили в изначальное содержимое файла, то надо его отредактировать
        # однако тогда у нас на конце будет ", ". провереяем наличие этой подстроки: если она есть, значит мы что-то
        # добавили, тогда перезаписываем файл с добавленным продкутом и ставим точку в конце вместо запятой с пробелом
