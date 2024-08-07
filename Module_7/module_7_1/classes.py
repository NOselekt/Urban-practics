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
        file_viscera = file_viscera.replace('.', '')
        file_for_read.close()
        for product in products:
            if product.name not in file_viscera:
                file_viscera += f'{product.name}, '
            else:
                print(f'{product.name} is already in the magazine.')
        if file_viscera[-2:] == ', ':
            file_for_write = open(self.__file_name, 'w')
            file_for_write.write(file_viscera[:-2] + '.')
            file_for_write.close()
