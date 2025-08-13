import math

def circle_matrics(radius):
    area=math.pi*radius**2
    circumference=2*math.pi*radius
    return area, circumference,math.pi

a,c,p=circle_matrics(5)
print("area: ",a)
print("circumference: ",c)
print("pi: ",p)