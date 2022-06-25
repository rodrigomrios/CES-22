import abc

class Engine(abc.ABC):

    @abc.abstractmethod
    def enginedurability(self):

        pass

    @abc.abstractmethod
    def enginepolutionrate(self):

        pass

    @abc.abstractmethod
    def engineautonomy(self):

        pass

class Combustion(Engine):

    def __init__(self, fuel):

        self.fuel = fuel
        self.enginetype = "Conbustion"
        self.durability = self.enginedurability()
        self.polutionrate = self.enginepolutionrate()
        self.autonomy = self.engineautonomy()

    def enginedurability(self):
        
        if self.fuel == 'Gasoline':

            return "100k km."

        if self.fuel == 'Diesel':

            return "400k km."

        if self.fuel == 'Alcohol':

            return "250k km."

    def enginepolutionrate(self):
        
        if self.fuel == 'Gasoline':

            return "High."

        if self.fuel == 'Diesel':

            return "Very High."

        if self.fuel == 'Alcohol':

            return "Medium."

    def engineautonomy(self):
        
        if self.fuel == 'Gasoline':

            return "410 km."

        if self.fuel == 'Diesel':

            return "420 km."

        if self.fuel == 'Alcohol':

            return "287 km."

class Eletric(Engine):

    def __init__(self, fuel):

        self.fuel = fuel
        self.enginetype = "Eletric"
        self.durability = self.enginedurability()
        self.polutionrate = self.enginepolutionrate()
        self.autonomy = self.engineautonomy()

    def enginedurability(self):
        
        return "240k km."

    def enginepolutionrate(self):
        
        return "Low."

    def engineautonomy(self):
        
        return "600 km."

class Hibrid(Engine):

    def __init__(self, fuel):

        self.fuel = fuel
        self.enginetype = "Hibrid"
        self.durability = self.enginedurability()
        self.polutionrate = self.enginepolutionrate()
        self.autonomy = self.engineautonomy()

    def enginedurability(self):
        
        return "350k km."

    def enginepolutionrate(self):
        
        return "Medium."

    def engineautonomy(self):
        
        return "678 km."

class Vehicle(abc.ABC):

    def __init__(self, engine, weight, model):

        self.engine = engine.enginetype
        self.fueltype = engine.fuel
        self.vdurability = engine.durability
        self.vpolutionrate = engine.polutionrate
        self.vautonomy = engine.autonomy
        self.weight = weight
        self.model = model

    @abc.abstractmethod
    def applysize(self):

        pass

    @abc.abstractmethod
    def applynumberwheels(self):

        pass

    @abc.abstractmethod
    def applynumberpassagers(self):

        pass

    @abc.abstractmethod
    def applytrunksize(self):

        pass

    @abc.abstractmethod
    def vehicledata(self):

        pass

class Car(Vehicle):

    def __init__(self, engine, weight, model):

        super().__init__(engine, weight, model)
        self.size = self.applysize()
        self.numberwheels = self.applynumberwheels()
        self.numberpassagners = self.applynumberpassagers()
        self.trunkcapacity = self.applytrunksize()

    def applysize(self):

        if self.weight <= 900:

            return "Small."

        if self.weight > 900 and self.weight <= 2000:

            return "Medium."

        if self.weight > 2000:

            return "Big."
    
    def applynumberwheels(self):
        
        return 4
    
    def applynumberpassagers(self):

        if self.weight <= 900:

            return 5

        if self.weight > 900 and self.weight <= 2000:

            return 7

        if self.weight > 2000:

            return 9
    
    def applytrunksize(self):

        if self.weight <= 900:

            return "Small."

        if self.weight > 900 and self.weight <= 2000:

            return "Medium."

        if self.weight > 2000:

            return "Big."

    def vehicledata(self):
        
        print("Engine:", self.engine)
        print("Fuel:", self.fueltype)
        print("Durability:", self.vdurability)
        print("Polution Rate:", self.vpolutionrate)
        print("Autonomy:", self.vautonomy)
        print("Weight:", self.weight)
        print("Model:", self.model)
        print("Size:", self.size)
        print("Number of Wheels:", self.numberwheels)
        print("Numeber of Passagers:", self.numberpassagners)
        print("Trunk Capacity:", self.trunkcapacity)


class Truck(Vehicle):

    def __init__(self, engine, weight, model):

        super().__init__(engine, weight, model)
        self.size = self.applysize()
        self.numberwheels = self.applynumberwheels()
        self.numberpassagners = self.applynumberpassagers()
        self.trunkcapacity = self.applytrunksize()

    def applysize(self):

        if self.weight <= 3500:

            return "Small."

        if self.weight > 3500 and self.weight <= 6000:

            return "Medium."

        if self.weight > 6000:

            return "Big."
    
    def applynumberwheels(self):
        
        if self.weight <= 3500:

            return 4

        if self.weight > 3500 and self.weight <= 6000:

            return 6

        if self.weight > 6000:

            return 8
    
    def applynumberpassagers(self):

        if self.weight <= 3500:

            return 2

        if self.weight > 3500 and self.weight <= 6000:

            return 4

        if self.weight > 6000:

            return 6
    
    def applytrunksize(self):

        if self.weight <= 3500:

            return "Big."

        if self.weight > 3500 and self.weight <= 6000:

            return "Very Big."

        if self.weight > 6000:

            return "Huge."

    def vehicledata(self):
        
        print("Engine:", self.engine)
        print("Fuel:", self.fueltype)
        print("Durability:", self.vdurability)
        print("Polution Rate:", self.vpolutionrate)
        print("Autonomy:", self.vautonomy)
        print("Weight:", self.weight)
        print("Model:", self.model)
        print("Size:", self.size)
        print("Number of Wheels:", self.numberwheels)
        print("Numeber of Passagers:", self.numberpassagners)
        print("Trunk Capacity:", self.trunkcapacity)


car1 = Car(Combustion('Gasoline'), 1100, 'New.')
car1.vehicledata()

car2 = Car(Eletric('Eletricity'), 3000, 'Old.')
car2.vehicledata()

car3 = Car(Hibrid('Alcohol and Eletricity'), 850, 'New.')
car3.vehicledata()

truck1 = Truck(Combustion('Alcohol'), 2500, 'Old.')
truck1.vehicledata()

truck2 = Truck(Eletric('Eletricity'), 6000, 'New.')
truck2.vehicledata()

truck3 = Truck(Hibrid('Gasoline and Eletricity'), 8000, 'New.')
truck3.vehicledata()
        



