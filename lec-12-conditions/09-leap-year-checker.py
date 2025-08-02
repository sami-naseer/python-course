year=int(input("enter the year"))

# 4,100,400 - 4 
# 4, !100

if( year % 4 == 0 and year % 100!= 0) or year % 400== 0:
    print("it is a leap year")
else:
    print("not a leap year")