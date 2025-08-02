score= int(input("Enter your score:"))#type casting 

if 90 <= score <= 100:
    print("your grade is A")
elif 80 <= score <= 89:
    print("your grade is B")
elif 70 <= score <= 79:
    print("your grade is C")
elif 60 <= score <= 69:
    print("your grade is D")
elif 60 > score >= 1:
    print("you are fail")
else :
    print("Please enter grade between 1-100")
