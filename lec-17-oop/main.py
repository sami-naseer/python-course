class Car:#class name
    def __init__(self,brand,model):#constructor
        self.mybrand=brand#attribute/variables
        self.mymodel=model
        
    def sum(a,b):#methods/function class ky andr ky functions ko methods kaha jata hy or variables ko attribute kaha jata hy
        print( a+b)
        
#my_car is object which store instance(adress) of class
my_car = Car("toyota","corola")#
print(my_car.mybrand)#here we call attribute of constructor
print(my_car.mymodel)