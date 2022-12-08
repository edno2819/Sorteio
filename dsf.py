import random

a = random.choices(
     population=[['a','b'], ['b','a'], ['c','b']],
     weights=[200, 20, 60],
     k=1
 )

print(a)