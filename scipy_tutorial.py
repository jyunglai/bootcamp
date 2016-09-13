import scipy.special as sspec
import numpy as np

#Error function
print(sspec.erf)

my_ar = np.ones([2,3])
print(sspec.erf(my_ar))

#Generate a list of random numbers
x = np.random.random(10000) #Generate 10,000 random numbers

print(x)

#Evaluate random numbers
def my_sum(x):
    """Summation"""
    x_sum = 0
    for num in x:
        x_sum += num
    return x_sum

print(my_sum(x))

#print(%timeit my_sum(x))
