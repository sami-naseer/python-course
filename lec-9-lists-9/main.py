lists=["sami","ammad","saran"]
# lists[1:2]="mushahid"
lists[1:2]=["mushahid","monday"]
lists[1:2]=[]
print(lists)

for item in lists:
    # if item == "sami":
    if "ali" in item:
        print(item)
    print("i run for ",item)
    
#using range
y=range(0,10)
print(list(y))

#list comprehension
arr=[item**2 for item in range(10)]
print(arr)

arr1=[item**3 for item in range(3,11)]
print(arr1)

