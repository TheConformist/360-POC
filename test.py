import random
from itertools import permutations
items = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
for ran in permutations(items):
    x = "".join(list(ran))
    print(x)
    print(type(x))