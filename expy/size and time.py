import sys
from timeit import default_timer as timer

mylist = list()
mytuple = tuple()
mydict = dict()
myset = set()

print("Sizes\n")
print(f'List = {sys.getsizeof(mylist)} bytes')
print(f'Tuple = {sys.getsizeof(mytuple)} bytes')
print(f'Dictionary = {sys.getsizeof(mydict)} bytes')
print(f'Set = {sys.getsizeof(myset)} bytes')

print("\n\nTime\n")
startml = timer()
print(f'List: {mylist}')
stopml = timer()
print(f'{stopml-startml}\n')

startmt = timer()
print(f'Tuple: {mytuple}')
stopmt = timer()
print(f'{stopmt-startmt}\n')

startmd = timer()
print(f'Dictionary: {mydict}')
stopmd = timer()
print(f'{stopmd-startmd}\n')

startms = timer()
print(f'Set: {myset}')
stopms = timer()
print(stopms-startms)
