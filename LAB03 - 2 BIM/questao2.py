class Cake:

    def __init__(self):

        self.massflavor = None
        self.fillingsflavor = None
        self.toppingfillings = None
        self.cakecover = None
        self.topdecoration = None

    def applymass(self, massflavor):

        self.massflavor = massflavor

    def applyfillingsflavor(self, fillingsflavor):

        self.fillingsflavor = fillingsflavor

    def applytoppingfillings(self, toppingfillings):

        self.toppingfillings = toppingfillings

    def applycakecover(self, cakecover):

        self.cakecover = cakecover

    def applytopdecoration(self, topdecoration):

        self.topdecoration = topdecoration

class Builder:

    def __init__(self, cakesize, theme, id):

        self.cakesize = cakesize
        self.theme = theme
        self.id = id

    def pickmass(self):

        pass

    def pickfillings(self):

        pass

    def picktoppings(self):

        pass

    def pickcakecover(self):

        pass

    def picktopdec(self):

        pass

class CelebrationCakeBuilder(Builder):

    def __init__(self, cakesize, theme, id):

        super().__init__(cakesize, theme, id)

    def pickmass(self):

        if self.cakesize == 'Big':

            massflavor = "Coconut."

            return massflavor

        if self.cakesize == 'Medium':

            massflavor = "Apple."

            return massflavor

        if self.cakesize == 'Small':

            massflavor = "Passion Fruit."

            return massflavor

    def pickfillings(self):
        
        if self.cakesize == 'Big':

            fillingsflavor = "Cookie and Cream."

            return fillingsflavor

        if self.cakesize == 'Medium':

            fillingsflavor = "Raspberry."

            return fillingsflavor

        if self.cakesize == 'Small':

            fillingsflavor = "Cranberry."

            return fillingsflavor

    def picktoppings(self):
        
        if self.cakesize == 'Big':

            toppingfillings = "Summer Fruits."

            return toppingfillings

        if self.cakesize == 'Medium':

            toppingfillings = "Fall Fruits."

            return toppingfillings

        if self.cakesize == 'Small':

            toppingfillings = "Winter Fruits."

            return toppingfillings

    def pickcakecover(self):
        
        if self.cakesize == 'Big':

            cakecover = "Chocolate."

            return cakecover

        if self.cakesize == 'Medium':

            cakecover = "Orange."

            return cakecover

        if self.cakesize == 'Small':

            cakecover = "Pear."

            return cakecover

    def picktopdec(self):
        
        if self.theme == 1:

            topdecoration = "Company Anniversary."

            return topdecoration

        if self.theme == 2:

            topdecoration = "Gender Reveal Party."

            return topdecoration

        if self.theme == 3:

            topdecoration = "Birthday Party."

            return topdecoration

class WeddingCakeBuilder(Builder):

    def __init__(self, cakesize, theme, id):

        super().__init__(cakesize, theme, id)

    def pickmass(self):

        if self.cakesize == 'Big':

            massflavor = "Vanilla."

            return massflavor

        if self.cakesize == 'Medium':

            massflavor = "Chocolate."

            return massflavor

        if self.cakesize == 'Small':

            massflavor = "Strawberry."

            return massflavor

    def pickfillings(self):
        
        if self.cakesize == 'Big':

            fillingsflavor = "Coconut."

            return fillingsflavor

        if self.cakesize == 'Medium':

            fillingsflavor = "Pineapple."

            return fillingsflavor

        if self.cakesize == 'Small':

            fillingsflavor = "Kiwi."

            return fillingsflavor

    def picktoppings(self):
        
        if self.cakesize == 'Big':

            toppingfillings = "Oreo and Cream."

            return toppingfillings

        if self.cakesize == 'Medium':

            toppingfillings = "KitKat and Fudge."

            return toppingfillings

        if self.cakesize == 'Small':

            toppingfillings = "Pieces of Chocolate."

            return toppingfillings

    def pickcakecover(self):
        
        if self.cakesize == 'Big':

            cakecover = "Vanilla."

            return cakecover

        if self.cakesize == 'Medium':

            cakecover = "Apple."

            return cakecover

        if self.cakesize == 'Small':

            cakecover = "Banana."

            return cakecover

    def picktopdec(self):
        
        if self.theme == 1:

            topdecoration = "Classic Fiance."

            return topdecoration

        if self.theme == 2:

            topdecoration = "Modern Fiance."

            return topdecoration

        if self.theme == 3:

            topdecoration = "Futuristic Fiance."

            return topdecoration

class InformalCelebrationCakeBuilder(Builder):

    def __init__(self, cakesize, theme, id):

        super().__init__(cakesize, theme, id)

    def pickmass(self):

        if self.cakesize == 'Big':

            massflavor = "Pear."

            return massflavor

        if self.cakesize == 'Medium':

            massflavor = "Star Fruit."

            return massflavor

        if self.cakesize == 'Small':

            massflavor = "Blueberry."

            return massflavor

    def pickfillings(self):
        
        if self.cakesize == 'Big':

            fillingsflavor = "Pineapple and Coconut."

            return fillingsflavor

        if self.cakesize == 'Medium':

            fillingsflavor = "Plum."

            return fillingsflavor

        if self.cakesize == 'Small':

            fillingsflavor = "Peach."

            return fillingsflavor

    def picktoppings(self):
        
        if self.cakesize == 'Big':

            toppingfillings = "Wipped Cream."

            return toppingfillings

        if self.cakesize == 'Medium':

            toppingfillings = "Strawberry Slices."

            return toppingfillings

        if self.cakesize == 'Small':

            toppingfillings = "Confetti."

            return toppingfillings

    def pickcakecover(self):
        
        if self.cakesize == 'Big':

            cakecover = "Sparkling Stars."

            return cakecover

        if self.cakesize == 'Medium':

            cakecover = "Blueberry."

            return cakecover

        if self.cakesize == 'Small':

            cakecover = "Red Velvet."

            return cakecover

    def picktopdec(self):
        
        if self.theme == 1:

            topdecoration = "Home Alone."

            return topdecoration

        if self.theme == 2:

            topdecoration = "Spiderman."

            return topdecoration

        if self.theme == 3:

            topdecoration = "Anime."

            return topdecoration

class Manager:

    def __init__(self, assignedbuilder, typecake):

        self.assignedbuilder = assignedbuilder
        self.typecake = typecake

    def pickacake(self):

        cake = Cake()

        mass = self.assignedbuilder.pickmass()
        cake.applymass(mass)
        
        fillings = self.assignedbuilder.pickfillings()
        cake.applyfillingsflavor(fillings)

        toppings = self.assignedbuilder.picktoppings()
        cake.applytoppingfillings(toppings)

        cakecover = self.assignedbuilder.pickcakecover()
        cake.applycakecover(cakecover)

        topdec = self.assignedbuilder.picktopdec()
        cake.applytopdecoration(topdec)

        print('Order', self.assignedbuilder.id, ':', self.assignedbuilder.cakesize, self.typecake, 'Cake. Chosen theme:', self.assignedbuilder.theme)
        print('Mass:', cake.massflavor)
        print('Filling:', cake.fillingsflavor)
        print('Toppings:', cake.toppingfillings)
        print('Cake Cover:', cake.cakecover)
        print('Theme:', cake.topdecoration)

manager1 = Manager(CelebrationCakeBuilder('Big', 1, 12345), 'Celebration')
manager1.pickacake()

maneger2 = Manager(WeddingCakeBuilder('Small', 2, 234567), 'Wedding')
maneger2.pickacake()









