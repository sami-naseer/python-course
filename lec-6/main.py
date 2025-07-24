import os
import sys 
import copy

cwd=os.getcwd()
refc=sys.getrefcount(cwd)
# print(refc)

a=2
b=5
a += 5 # a = a + 5
# print("a = ",a)

h1=[1,2,3]
h2=h1[:]
h2[0]=55
# print(h1 )
# print(h2)

l1 = [1,[55,44,[3,[6,88]]],3,["a","b"]]
l2=copy.copy(l1)
l2[0]=55
# print(l1)
# print(l2)
# l3=copy.deepcopy(l1)
# print(l3)

h1=[1,2,3]
h2=h1[:]
print(h1==h2)
print(h1 is h2)


x,y,z=10,20,30
x>y>z # x>y and y > z => 0/TFalse and 0/False => 0