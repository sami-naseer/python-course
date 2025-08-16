#same name but differet beHAVIOUR(polymorphism)

class Car:#class name
    total_car=0
    def __init__(self,brand,model):#constructor
        self.__mybrand=brand#attribute/variables
        self.mymodel=model
        Car.total_car+=1
    
    @property# @ wly sab decorator hoty hein and read only hoty
    def get_brand(self):
        return self.__mybrand
    
    def sum(self, a, b):  # method to sum two numbers
        self.a = a
        self.b = b
        print( self.a + self.b)
        
    def fuel_type(self):
        print("petrol or disel")

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
    
    @staticmethod
    def fuel_type():
        print("electric charge")
        
    # @staticmethod     jab hum staticmethod likh dein gy fr ye independent ho jai ga fr humein self likh ky connect krny ki zrurat nahio hy
    # def fuel_type():
    #     print("electric charge")

class Sami:
    pass      
        
# my_car is object which stores instance (address) of class
my_car = Car("toyota", "corola")#object
my_car.fuel_type()
print(my_car.mybrand)  # print brand attribute
print(my_car.__mybrand)  # mybrand aik private attribute hy is liye hum class sy bahir access nahi kr skty           v
print(my_car.get_brand())
print(my_car.mymodel)  # print model attribute
my_car.sum(12, 4)  # print sum of 12 and 4

electric_car=ElectricCar("Tesla","S3","large")
electric_car.fuel_type()
print(f"this class runs {my_car.total_car} times")
print(electric_car._mybrand)   # print brand of electric car
print(electric_car.mymodel)   # print model of electric car
print(electric_car.battery_size)

print(isinstance(electric_car,Sami))# ye check krta hy ki object inherit huwa hy ya nahi