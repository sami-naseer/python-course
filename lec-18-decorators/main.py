# def my_decorator(func):
#     def wrapper():
#         result=func()
#         return result
#     return wrapper

# @my_decorator
# def say_hello():
#     print("Hi Sami")

# say_hello()
import time

def my_decorator(func):
    def wrapper(*arg):
        start=time.time()
        result=func(*arg)
        end=time.time()
        print(f"{func.__name__} ran in {(end-start)} seconds")
        return result
    return wrapper

@my_decorator
def say_hello(n):
    time.sleep(n)
    print("Hi Sami")

say_hello(3)

@my_decorator
def say_he(n):
    time.sleep(n)
    print("Hi Sami")

say_he(1)

@my_decorator
def say_hell(n):
    time.sleep(n)
    print("Hi Sami")

say_hell(5)