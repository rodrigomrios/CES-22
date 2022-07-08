class Livraria:

    def __init__(self):

        self.books = []
        self.authors = []
        self.procucts = []
        self.clients = []

    def insertbook(self, book):

        self.books.append(book)

    def insertauthors(self, author):

        self.authors.append(author)

    def insertprocucts(self, product):

        self.procucts.append(product)

    def switchbook(self, old, new):

        self.books.remove(old)
        self.books.append(new)

    def switchauthors(self, old, new):

        self.authors.remove(old)
        self.authors.append(new)

    def switchprocucts(self, old, new):

        self.procucts.remove(old)
        self.procucts.append(new)
    
    def searchauthor(self, author):

        if author in self.authors:

            return author.tittlesavailable

        return print('This author is not available')

    def removebooks(self, book):

        self.books.remove(book)

    def removeauthors(self, author):

        self.authors.remove(author)

    def removeprocucts(self, product):

        self.procucts.remove(product)

    def insertclient(self, client):

        self.clients.append(client)

    def switchclient(self, old, new):

        self.clients.remove(old)
        self.clients.append(new)

    def revomeclient(self, client):

        self.clients.remove(client)

    def searchclient(self, client):

        if client in self.clients:

            return print('This client data are:', client.name, client.email, client.purchases)
        
        return print('This client in not available')

    def insertpurchase(self, client, purchase):

        client.purchases.append(purchase)

    def switchpurchase(self, client, old, new):

        client.purchases.remove(old)
        client.purchase.append(new)

    def searchpurchase(self, client, purchase):

        if purchase in client.purchases:

            return print('Purchase data are:', purchase.book, purchase.id, purchase.price)

        return('This purchase is not available')

    def removepurchase(self, client, purchase):

        client.purchases.remove(purchase)

class Book:

    def __init__(self, title, author, genre, edition, publicompany, pricesell, pricebuy):

        self.title = title
        self.author = author
        self.genre = genre
        self.etion = edition
        self.publicompany = publicompany
        self.pricesell = pricesell
        self.pricebuy = pricebuy
        self.taxgenrebuysell = self.genre.tax * (pricesell - pricebuy)
        self.price = self.pricesell + self.taxgenrebuysell

class Author:

    def __init__(self, name, email):
        
        self.name = name
        self.email = email
        self.titlespublished = []
        self.titlesavailable = []

    def insertpublished(self, title):

        return self.titlespublished.append(title)

    def insertavailable(self, title):

        return self.titlesavailable.append(title)

class Genre:

    def __init__(self, genre, tax):

        self.genre = genre
        self.tax = tax

    def switchtax(self, newtax):

        self.tax = newtax    
    
class Client:

    def __init__(self, name, email):

        self.nome = name
        self.email = email
        self.purchases = []
        
class Purchase:

    def __init__(self, book, id):

        self.book = book
        self.id = id
        self.price = book.price

class Cafeteria:

    def __init__(self):

        self.itens = []

    def insertitem(self, coffe):

        self.itens.append(coffe)

    def switchitem(self, old, new):

        self.itens.remove(old)
        self.itens.append(new)

    def removeitem(self, item):

        self.itens.remove(item)

    def searchitem(self, item):

        if item in self.itens:

            return print('Item data are:', item.name, item.flavor, item.id, item.price)

        return print('This item is not available')

class Coffe:

    def __init__(self, name, flavor, pricesell, tax, id):

        self.name = name
        self.flavor = flavor
        self.pricesell = pricesell
        self.tax = tax
        self.id = id
        self.price = self.pricesell * (1 + self.tax)

class Donut:

    def __init__(self, name, flavor, pricesell, id, tax):

        self.name = name
        self.flavor = flavor
        self.pricesell = pricesell
        self.id = id
        self.tax = tax
        self.price = self.pricesell * (1 + self.tax)
