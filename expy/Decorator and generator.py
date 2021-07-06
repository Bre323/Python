#DECORATOR

from functools import wraps

def start_end_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        re = func(*args, **kwargs)
        print('End')
        return re
    return wrapper

@start_end_decorator
def add5(x):
    return x + 5
 
re = add5(10)
print(re)
print(add5.__name__, '\n')


# GENERATOR

from sys import getsizeof

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstngen(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(firstn(10)))
print(sum(firstngen(10)))

#Tamanhos das duas funções (1000 elementos)
print(f'firstn = {getsizeof(firstn(1000))} bytes')
print(f'firstngen = {getsizeof(firstngen(1000))} bytes')
