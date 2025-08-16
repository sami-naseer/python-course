class Car:#class name
    def __init__(self,brand,model):#constructor
        self.__mybrand=brand#attribute/variables
        self.mymodel=model
    
    def get_brand(self):
        return self.__mybrand
    
    def sum(self, a, b):  # method to sum two numbers
        self.a = a
        self.b = b
        print( self.a + self.b)

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
        
        
# my_car is object which stores instance (address) of class
my_car = Car("toyota", "corola")#object
# print(my_car.mybrand)  # print brand attribute
# print(my_car.__mybrand)  # mybrand aik private attribute hy is liye hum class sy bahir access nahi kr skty           v
# print(my_car.get_brand())
# print(my_car.mymodel)  # print model attribute
# my_car.sum(12, 4)  # print sum of 12 and 4

# electric_car=ElectricCar("Tesla","S3","large")
# print(electric_car._mybrand)   # print brand of electric car
# print(electric_car.mymodel)   # print model of electric car
# print(electric_car.battery_size)