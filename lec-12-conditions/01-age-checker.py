age= int(input("Enter your age:"))#type casting 

if 1 <= age < 13:
    print("you are child")
# elif age>12 and age<19:
elif 12 < age <= 19:
    print("you are teenager")
elif 20 <= age <= 59:
    print("you are adult")
elif  60 <= age <=100:
    print("you are senior")
else:
    print("Please enter age between 1-100")
