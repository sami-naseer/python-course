a=123
b="123"
c={}
d=()

# print(type(int(b))) #converting one data type into another it is called type casting
# print(type(c))
# print(type(d))

# Practice Questions:
# Use Python to calculate 2 ** 1000. What do you observe?
# What’s the difference between math.floor(-3.5) and math.trunc(-3.5)?
# Convert 64 into binary, octal, and hexadecimal using Python.


# notes
# math.floor(x) – Round down to nearest integer(ye na -nus wli value sy choti value dy ga like -2.5 hy tw -3 dy ga)
# math.trunc(x) – Remove decimal (truncate)(ye point or ussy agy wali value ko remove kr dy ga)


from decimal import Decimal
result=Decimal(0.5)+Decimal(0.5)+Decimal(-0.9)
print(result)


