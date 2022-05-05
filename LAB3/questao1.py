from abc import ABC, abstractmethod


class Produto():

    total_products = 0

    
    def __init__(self, type, price, name, code, method):

        self.type = type
        self.price = price
        self.name = name
        self.code = code
        self.method = method
        Produto.total_products += 1
    
    def description(self):

        print('Product description: Nome:', self.name, 'Type:', self.type, 'Price:', self.price, 'Code:', self.code)
    
    @staticmethod
    def price_classification(price):

        if price > 0 and price <= 20:

            print('The product is cheap')

        if price > 20 and price <= 100:

            print('The product has a acceptable price')

        if price > 100:

            print('The product is expensive')
    
    @classmethod
    def gettotal_products(cls):

        return print(cls.total_products)

class Eletrodomestico(ABC):
    
    def __init__(self, type, price, name, code, method):

        self.type = type
        self.price = price
        self.name = name
        self.code = code
        self.method = method
    
    @abstractmethod
    def get_method(self):
        pass 

    def description(self):
        pass

class Ventilador(Eletrodomestico):

    def get_method(self, mode):

        self.method = self.method + mode

        return print(self.method)
    
    def description(self):

        print('Product description: Nome:', self.name, 'Type:', self.type, 'Price:', self.price, 'Code:', self.code)

p1 = Produto('eletrodomestico', 220, 'ar condicionado', 123456789, 'method') 
p2 = Produto('roupa', 49.50, 'calca', 456789123, 'method')
p3 = Ventilador('eletrodomestico', 60, 'ventilador arno', 478963215, 'method')

p1.description()
p2.description()
p3.description()

Produto.price_classification(102)
Produto.gettotal_products()

p3.get_method('online')