tup=("sami","ammad","saran","ammad")
print(tup)
print(tup[0])
print(tup[-1])#for last item 
print(tup[:])#for last item 

# tup[0]="ali" #so tuples ka ye clear ho gya ki ye change nahi ho skta after creation
print(len(tup)) 

tup2=("sun","mon")
all_tup=tup+tup2#concetenate
print(all_tup)

if "ammadd" in tup:#for checking that item is present or not
    print("ammad exist")
    
print(tup.count("ammad")) # check krna ki koli cheez kitni mrtaba repeat hui hy 

x,y,z,p=tup #collection of variables ko hum single single variables ko assign kr dein(tuple unpacking)
# x = tup[0]
# y = tup[1]
# z = tup[2]
print(x)
print(y)
print(z)

print(type(tup))
print(type(x))
