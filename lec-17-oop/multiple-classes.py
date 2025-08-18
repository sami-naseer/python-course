# class Battery:
#     def battery_info(self,timing):
#         self.timimg=timing

# class Engine(self,type):
#     def engine_info(self,engine_type):
#     super().battery_info(timing,type)
    
        
# class ElectricCarTwo(battery,engine,car):

class Car:
    def car_info(self,a,b):
        # self.a=a
        # self.b=b
        return a+b

class Battery:
    def battery_info(self):
        print("this is battery")
        
class Engine:
    def engine_info(self):
        return "this is engine"

class Run(Car,Battery,Engine):
    def which_car_running(self,a,b):
        car_info_return = super().car_info(a,b)
        print("car info value",car_info_return)

obj_of_run=Run()
obj_of_run.which_car_running(4,4)