# Create a dictionary of 3 fruits with their colors. Add one more fruit later.
# Loop through the dictionary and print all keys and values.
# Try creating a dictionary from a list of days with a default value of "Available".

#Question one adding new item in dictionary later
myfruits={
    "apple":"green",
    "bnana":"yellow",
    "orange":"orange"
}

# myfruits["grapes"]="Black"
# print(myfruits)

#Question 2 loops
# for medicine in myfruits:
    # print(myfruits)
    
#creaTING DICTIONARY FROM A LIST and use a default value
newlistt=["sunday","monday","tuesday"]
default_value="days"
updatedd_list=dict.fromkeys(newlistt,default_value)
print(updatedd_list)
