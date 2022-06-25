class PizzaIngredients:

    def getDescription(self):

        return self.__class__.__name__

    def getTotalCost(self):

        return self.__class__.cost

class Shipping(PizzaIngredients):

    cost = 7.5

class Decorator(PizzaIngredients):

    def __init__(self, pizzaingredents):

        self.component = pizzaingredents

    def getTotalCost(self):

        return self.component.getTotalCost() + PizzaIngredients.getTotalCost(self)

    def getDescription(self):

        return self.component.getDescription() + " " + PizzaIngredients.getDescription(self)

class Sauce(Decorator):

    cost = 1.95

    def __init__(self, pizzaingredients):

        Decorator.__init__(self, pizzaingredients)

class Cheese(Decorator):

    cost = 2.5

    def __init__(self, pizzaingredients):

        Decorator.__init__(self, pizzaingredients)

class Sausage(Decorator):

    cost = 2.25

    def __init__(self, pizzaingredients):

        Decorator.__init__(self, pizzaingredients)

class Corn(Decorator):

    cost = 1.8

    def __init__(self, pizzaingredients):
        
        Decorator.__init__(self, pizzaingredients)

class Peas(Decorator):

    cost = 1.40

    def __init__(self, pizzaingredients):
        
        Decorator.__init__(self, pizzaingredients)

class Ham(Decorator):

    cost = 2.2

    def __init__(self, pizzaingredients):
        
        Decorator.__init__(self, pizzaingredients)

class Chicken(Decorator):

    cost = 2.5

    def __init__(self, pizzaingredients):
        
        Decorator.__init__(self, pizzaingredients)

class Onion(Decorator):

    cost = 0.5

    def __init__(self, pizzaingredients):
        
        Decorator.__init__(self, pizzaingredients)

class Garlic(Decorator):

    cost = 0.8

    def __init__(self, pizzaingredients):
        
        Decorator.__init__(self, pizzaingredients)

class Tomato(Decorator):

    cost = 1

    def __init__(self, pizzaingredients):
        
        Decorator.__init__(self, pizzaingredients)

class Bacon(Decorator):

    cost = 2.8

    def __init__(self, pizzaingredients):
        
        Decorator.__init__(self, pizzaingredients)

class Basil(Decorator):

    cost = 1.1

    def __init__(self, pizzaingredients):
        
        Decorator.__init__(self, pizzaingredients)

class Strawberry(Decorator):

    cost = 2

    def __init__(self, pizzaingredients):
        
        Decorator.__init__(self, pizzaingredients)

class Chocolate(Decorator):

    cost = 2.1

    def __init__(self, pizzaingredients):
        
        Decorator.__init__(self, pizzaingredients)

class CondensedMilk(Decorator):

    cost = 3.5

    def __init__(self, pizzaingredients):
        
        Decorator.__init__(self, pizzaingredients)

class MilkCream(Decorator):

    cost = 3

    def __init__(self, pizzaingredients):
        
        Decorator.__init__(self, pizzaingredients)

class Confetti(Decorator):

    cost = 1.7

    def __init__(self, pizzaingredients):
        
        Decorator.__init__(self, pizzaingredients)

class KitKat(Decorator):

    cost = 2.8

    def __init__(self, pizzaingredients):
        
        Decorator.__init__(self, pizzaingredients)

portuguesepizza = Sauce(Cheese(Sausage(Peas(Corn(Ham(Basil(Shipping())))))))
print(portuguesepizza.getDescription() + ": $" + str(portuguesepizza.getTotalCost()))

sweetpizza = Sauce(Cheese(Strawberry(KitKat(CondensedMilk(Confetti(Shipping()))))))
print(sweetpizza.getDescription() + ": $" + str(sweetpizza.getTotalCost()))