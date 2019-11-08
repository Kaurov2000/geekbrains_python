from functools import reduce

def multiply(a,b):
    return a * b

my_list = [x for x in range(100,1001) if x % 2 == 0]
print(reduce(multiply, my_list))