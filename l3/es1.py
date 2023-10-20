import math
import random as rand
import statistics as stat


print(math.factorial(39))

print(math.e)

list1 = [math.e, 2, 3, 10]
for i in list1:
    print(math.log(1500, i))

print(rand.random())

print(rand.uniform(3.5, 13.5))

print(rand.uniform(5, 50))

print(rand.uniform(6, 60))

list1 = [1, 1, 2, 3, 3, 3, 3, 4] 
list2 = [1, 2, 3, 4, 5, 6, 7, 8]

stat.mode(list1)
stat.mean(list2)
