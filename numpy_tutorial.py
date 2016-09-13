import numpy as np

#Creating an array using numpy
my_array = np.array([1,2,3,4,5,90,800,1000])
print(type(my_array))

#Element in the array from a numpy array
print(my_array[5])

#Looking at data type of elements in array
print(my_array.dtype)

#Methods in the array using numpy
print(my_array.shape)

#Convert from 64 bit to 32 bit
my_array = my_array.astype('int32')
print(my_array.astype('int32'), my_array.dtype)

#Convert to float
print(my_array.astype(float), my_array.dtype)

#Find the max and min
print(my_array.max())
print(my_array.min())

#Find the sum and standard deviation
print(my_array.sum())
print(my_array.std())

#Both ways are the same
print(np.max(my_array) == my_array.max())

#Creating arrays with prefiled amounts
n_values = 10
print(np.zeros(n_values))
print(np.ones(n_values))

#Multi-dimensional arrays
array2 = np.array([[1,2], [3,4]])
print(array2)

print(np.shape(array2))

array3 = np.zeros([2,2])
print(array3)

#Create a duplicate array using _like
array4 = np.zeros_like(array3)
print(array4)

my_ar = np.array([1, 2, 3, 4])
print(my_ar)
print(np.exp(my_ar))
print(np.sin(my_ar))
print(np.sqrt(my_ar))

print(np.dot(my_ar, my_ar))
