original_string="ami ur rehman"

for strr in original_string:
    if original_string.count(strr)==1:
        print("The first non-repeated character is: ",strr)
        break
