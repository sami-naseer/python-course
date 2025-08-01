age= int(input("Enter your age:"))#type casting 
users_day= input("Enter day:")

ticket_base_price=8
discount=2

def day_checker(day):
    if day=="wednesday" or day == "Wednesday":
        print("inside func if")
        return True
    else:
        print("inside func else")
        return False

if 1 <= age <=17:
    if day_checker(users_day):
        print("ticket price is $",ticket_base_price - discount)
    else:
        print("ticket price is $",ticket_base_price)
elif 18 <= age <=100:
    if day_checker(users_day):
        print("inside  elif")
        print("ticket price is $",(ticket_base_price - discount) + 4)
    else:
        print("inside  elif else")
        print("ticket price is $",ticket_base_price+4)
else:
    print("Please enter age between 1-100")
    ticket_base_price=8