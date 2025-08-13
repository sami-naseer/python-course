total=0

vehicle= input("vehicle type Car/bike: ")

if vehicle=="car":
    while True:
        part=input("break,headlight,wheel: ")
        if part=="break":
            total +=200
            print(f"Price 200, Total Bill {total}")
        elif part=="headlight":
            total+=300
            print(f"Price 300, Total Bill {total}")
        elif part=="wheel":
            total+=400
            print(f"Price 400, Total Bill {total}")
        else:
            print(f"Thanks for comming your total bill is {total}")
            break
if vehicle=="bike":
    while True:
        part=input("break,headlight,wheel")
        if part=="break":
            total +=100
            print(f"Price 100, Total Bill {total}")
        elif part=="headlight":
            total+=200
            print(f"Price 200, Total Bill {total}")
        elif part=="wheel":
            total+=300
            print(f"Price 300, Total Bill {total}")
        else:
            print(f"Thanks for comming your total bill is {total}")
            break
else:
    print(f"program is going to terminate")
