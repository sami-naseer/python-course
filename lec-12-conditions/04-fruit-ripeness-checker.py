#ledder if
fruit=input("enter fruit name: ")
color=input("enter color of fruit: ")

if color == "green":
    print(fruit," is unripe")
elif color == "yellow" or color == "red" or color == "purple":
    print(fruit," is ripe")
elif color == "brown":
    print(fruit," is overripe")
else:
    print("color should be green,red\\purple\\yellow or brown")

