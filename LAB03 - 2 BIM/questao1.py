import abc

class AbstractFcatory(abc.ABC):

    def __init__(self, cakesize, theme, id):

       self.cakesize = cakesize
       self.theme = theme
       self.id = id
    
    @abc.abstractmethod
    def massflavor(self):

        pass

    @abc.abstractmethod
    def fillingsflavor(self):

        pass

    @abc.abstractmethod
    def toppingsfillings(self):

        pass

    @abc.abstractmethod
    def cakecoverflavor(self):

        pass

    @abc.abstractmethod
    def topdecoration(self):

        pass

class WeddingFactory(AbstractFcatory):

    def __init__(self, cakesize, theme, id):

        super().__init__(cakesize, theme, id)
        
        print('Order', id, ':', cakesize, 'Wedding Cake. Chosen theme:', theme)

    def massflavor(self):

        return Wedding_massflavor(self.cakesize)

    def fillingsflavor(self):

        return Wedding_fillingsflavor(self.cakesize)
    
    def toppingsfillings(self):

        return Wedding_toppingfillings(self.cakesize)
    
    def cakecoverflavor(self):

        return Wedding_cakecoverflavor(self.cakesize)

    def topdecoration(self):

        return Wedding_topdecoration(self.theme)

class CelebrationFactory(AbstractFcatory):

    def __init__(self, cakesize, theme, id):

        super().__init__(cakesize, theme, id)

        print('Order', id, ':', cakesize, 'Celebration Cake. Chosen theme:', theme)

    def massflavor(self):

        return Celebration_massflavor(self.cakesize)

    def fillingsflavor(self):

        return Celebration_fillingsflavor(self.cakesize)
    
    def toppingsfillings(self):

        return Celebration_toppingfillings(self.cakesize)
    
    def cakecoverflavor(self):

        return Celebration_cakecoverflavor(self.cakesize)

    def topdecoration(self):

        return Celebration_topdecoration(self.theme)    

class InformalCelebrationFactory(AbstractFcatory):

    def __init__(self, cakesize, theme, id):

        super().__init__(cakesize, theme, id)

        print('Order', id, ':', cakesize, 'Informal Celebration Cake. Chosen theme:', theme)

    def massflavor(self):

        return InformalCelebration_massflavor(self.cakesize)

    def fillingsflavor(self):

        return InformalCelebration_fillingsflavor(self.cakesize)
    
    def toppingsfillings(self):

        return InformalCelebration_toppingfillings(self.cakesize)
    
    def cakecoverflavor(self):

        return InformalCelebration_cakecoverflavor(self.cakesize)

    def topdecoration(self):

        return InformalCelebration_topdecoration(self.theme)

class MassFlavourAbstractProduct(abc.ABC):

    def __init__(self, cakesize):

        self.cakesize = cakesize
    
    @abc.abstractmethod
    def mass(self):

        pass

class FillingsFlavorAbstractProduct(abc.ABC):

    def __init__(self, cakesize):

        self.cakesize = cakesize

    @abc.abstractmethod
    def fillings(self):

        pass

class ToppingsfillingsAbstractProduct(abc.ABC):

    def __init__(self, cakesize):

        self.cakesize = cakesize

    @abc.abstractmethod
    def toppings(self):

        pass

class CakeCoverAbstractProduct(abc.ABC):

    def __init__(self, cakesize):

        self.cakesize = cakesize

    @abc.abstractmethod
    def cakecover(self):

        pass

class TopDecorationAbstractProduct(abc.ABC):

    def __init__(self, theme):

        self.theme = theme

    @abc.abstractmethod
    def topdec(self):

        pass

class Wedding_massflavor(MassFlavourAbstractProduct):

    def __init__(self, cakesize):

        super().__init__(cakesize)

    def mass(self):

        if self.cakesize == 'Big':

            print('Mass: Vanilla.')

        if self.cakesize == 'Medium':

            print('Mass: Chocolate.')

        if self.cakesize == 'Small':

            print('Mass: Strawberry.')

class Wedding_fillingsflavor(FillingsFlavorAbstractProduct):

    def __init__(self, cakesize):

        super().__init__(cakesize)

    def fillings(self):

        if self.cakesize == 'Big':

            print('Fillings: Coconut.')

        if self.cakesize == 'Medium':

            print('Fillings: Pineapple.')

        if self.cakesize == 'Small':

            print('Fillings: Kiwi.')

class Wedding_toppingfillings(ToppingsfillingsAbstractProduct):

    def __init__(self, cakesize):

        super().__init__(cakesize)

    def toppings(self):

        if self.cakesize == 'Big':

            print('Topping: Oreo and Cream.')

        if self.cakesize == 'Medium':

            print('Toppings: KitKat and Fudge.')

        if self.cakesize == 'Small':

            print('Topping: Pieces of Chocolate.')

class Wedding_cakecoverflavor(CakeCoverAbstractProduct):

    def __init__(self, cakesize):

        super().__init__(cakesize)

    def cakecover(self):

        if self.cakesize == 'Big':

            print('Cake Cover: Vanilla.')

        if self.cakesize == 'Medium':

            print('Cake Cover: Apple.')

        if self.cakesize == 'Small':

            print('Cake Cover: Banana.')

class Wedding_topdecoration(TopDecorationAbstractProduct):

    def __init__(self, theme):

        super().__init__(theme)

    def topdec(self):

        if self.theme == 1:

            print('Theme: Classic Fiance.')

        if self.theme == 2:

            print('Theme: Modern Fiance.')

        if self.theme == 3:

            print('Theme: Futuristic Fiance.')

class Celebration_massflavor(MassFlavourAbstractProduct):

    def __init__(self, cakesize):

        super().__init__(cakesize)

    def mass(self):

        if self.cakesize == 'Big':

            print('Mass: Coconut.')

        if self.cakesize == 'Medium':

            print('Mass: Apple.')

        if self.cakesize == 'Small':

            print('Mass: Passion Fruit.')

class Celebration_fillingsflavor(FillingsFlavorAbstractProduct):

    def __init__(self, cakesize):

        super().__init__(cakesize)

    def fillings(self):

        if self.cakesize == 'Big':

            print('Fillings: Cookie and Cream.')

        if self.cakesize == 'Medium':

            print('Fillings: Raspberry.')

        if self.cakesize == 'Small':

            print('Fillings: Cranberry.')

class Celebration_toppingfillings(ToppingsfillingsAbstractProduct):

    def __init__(self, cakesize):

        super().__init__(cakesize)

    def toppings(self):

        if self.cakesize == 'Big':

            print('Topping: Summer Fruits.')

        if self.cakesize == 'Medium':

            print('Toppings: Fall Fruits.')

        if self.cakesize == 'Small':

            print('Topping: Winter Fruits.')

class Celebration_cakecoverflavor(CakeCoverAbstractProduct):

    def __init__(self, cakesize):

        super().__init__(cakesize)

    def cakecover(self):

        if self.cakesize == 'Big':

            print('Cake Cover: Chocolate.')

        if self.cakesize == 'Medium':

            print('Cake Cover: Orange.')

        if self.cakesize == 'Small':

            print('Cake Cover: Pear.')

class Celebration_topdecoration(TopDecorationAbstractProduct):

    def __init__(self, theme):

        super().__init__(theme)

    def topdec(self):

        if self.theme == 1:

            print('Theme: Company Anniversary.')

        if self.theme == 2:

            print('Theme: Gender Reveal Party.')

        if self.theme == 3:

            print('Theme: Birthday Party.')

class InformalCelebration_massflavor(MassFlavourAbstractProduct):

    def __init__(self, cakesize):

        super().__init__(cakesize)

    def mass(self):

        if self.cakesize == 'Big':

            print('Mass: Pear.')

        if self.cakesize == 'Medium':

            print('Mass: Star Fruit.')

        if self.cakesize == 'Small':

            print('Mass: Blueberry.')

class InformalCelebration_fillingsflavor(FillingsFlavorAbstractProduct):

    def __init__(self, cakesize):

        super().__init__(cakesize)

    def fillings(self):

        if self.cakesize == 'Big':

            print('Fillings: Pinapple and Coconut.')

        if self.cakesize == 'Medium':

            print('Fillings: Plum.')

        if self.cakesize == 'Small':

            print('Fillings: Peach.')

class InformalCelebration_toppingfillings(ToppingsfillingsAbstractProduct):

    def __init__(self, cakesize):

        super().__init__(cakesize)

    def toppings(self):

        if self.cakesize == 'Big':

            print('Topping: Wipped Cream.')

        if self.cakesize == 'Medium':

            print('Toppings: Strawberry Slices.')

        if self.cakesize == 'Small':

            print('Topping: Confetti.')

class InformalCelebration_cakecoverflavor(CakeCoverAbstractProduct):

    def __init__(self, cakesize):

        super().__init__(cakesize)

    def cakecover(self):

        if self.cakesize == 'Big':

            print('Cake Cover: Sparkling Stars.')

        if self.cakesize == 'Medium':

            print('Cake Cover: Blueberry.')

        if self.cakesize == 'Small':

            print('Cake Cover: Red Velvet.')

class InformalCelebration_topdecoration(TopDecorationAbstractProduct):

    def __init__(self, theme):

        super().__init__(theme)

    def topdec(self):

        if self.theme == 1:

            print('Theme: Home Alone.')

        if self.theme == 2:

            print('Theme: Spiderman.')

        if self.theme == 3:

            print('Theme: Anime.')

factory1 = CelebrationFactory('Big', 1, 12345)
p1 = factory1.massflavor()
p1.mass()
p2 = factory1.fillingsflavor()
p2.fillings()
p3 = factory1.toppingsfillings()
p3.toppings()
p4 = factory1.cakecoverflavor()
p4.cakecover()
p5 = factory1.topdecoration()
p5.topdec()

factory2 = WeddingFactory('Small', 2, 234567)
p6 = factory2.massflavor()
p6.mass()
p7 = factory2.fillingsflavor()
p7.fillings()
p8 = factory2.toppingsfillings()
p8.toppings()
p9 = factory2.cakecoverflavor()
p9.cakecover()
p10 = factory2.topdecoration()
p10.topdec()




        
        
