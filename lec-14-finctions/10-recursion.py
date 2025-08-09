#5*4*3*2*1(a function caLL ITSELF inside itself until the problem is solved)
def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)

res = factorial(5)
print(res)