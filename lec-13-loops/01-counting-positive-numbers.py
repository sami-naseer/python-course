numbers=[0,1,5,-8,9,-17,3,4,6,-7]
positive_count=0

for num in numbers:
    if num >=0:
        positive_count -= 1 #positive_count = positive_count + 1
print("there are ",positive_count," positive integers in list")   