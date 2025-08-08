mylist=[1,2,3,4]
it=iter(mylist)
# print(it)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
while True:
    try:
        item=next(it)
        print(it)
    except StopIteration:
        break
    
    