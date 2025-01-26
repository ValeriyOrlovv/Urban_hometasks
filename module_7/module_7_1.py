from pprint import pprint
from unicodedata import category


class Product:

    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.categoty}'


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        pprint(file.read())
        file.close()

    def add(self, *products):
        existing_products = {}
        file1 = open(self.__file_name, 'r')
        for line in file1:
            name, weight, category = line.strip.split(', ')
            weight = float(weight)
            existing_products[(name, category)] = weight
            file1.close()
        file2 = open(self.__file_name, 'a'):
        for product in products:
        key = (product.name, product.category)
        if key in existing_products:
            file2.write()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

s1.add(p1, p2, p3)

print(s1.get_products())
