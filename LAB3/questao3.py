class Produto():

    def __init__(self, name,  price, code, store):

        self.price = price
        self.name = name
        self.code = code
        self.store = store
    
    def printmessageinit(self):
        
        return print('O produto:', self.name, ',cujo preco e:', self.price, ',de codigo:', self.code, ',vendido em:', self.store)

class Celular(Produto):
    def __init__(self, name,  price, code, store, type):

        super().__init__(name,  price, code, store)
        self.type = type
    
    def printmessagefinal(self):
        
         Celular.printmessageinit(self)
         print('E um:', self.type)

C1 = Celular('Iphone 13 Pro Max', 10.200, 123456789, 'Apple', 'Smartphone')

C1.printmessagefinal()
