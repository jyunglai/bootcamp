#Load data from data files (csv files)

import numpy as np

xa_high = np.loadtxt('data/xa_high_food.csv')
xa_low = np.loadtxt('data/xa_low_food.csv')

print(xa_high, xa_low)

#Conversion
xa_high_converted = xa_high / 1e6
print(xa_high_converted)

#Boolean operation, which ones are larger than 2000
print(xa_high > 2000)

#Will give error
#if xa_high > 2000:
#    print('wow')

#Check if any of these are greater
if (xa_high > 2000).any():
    print('wow')

#Check if all are greater
if (xa_high > 2000).all():
    print('WHOA')
else:
    print('Thought so')

print(np.isclose(1.3, 1.29999999999999))

#Check to see which ones are close to a values
print(np.isclose(xa_high, 1800))

#Can't add 2 arrays that are different shapes
#xa_high + xa_low

xa_low_slice = xa_low[:len(xa_high)]
#Now I can add both arrays together
print(xa_high + xa_low_slice)


#Reverse data
print(xa_high[::-1])
print(xa_high[18:20:2])


#Gives all elements that are greater than 2000 and stores as an array
print(xa_high[xa_high > 2000])

#Gives the indices where the values are greater than 2000
new_data = np.where(xa_high > 2000)

#np uses pass by reference, make sure to use np.copy to make a new copy of the array
xa_high_copy = np.copy(xa_high)
xa_high_copy += 1E9
print(xa_high_copy, xa_high)

#Concatenate array
xa_food_combined = np.concatenate((xa_high, xa_low))
print(len(xa_food_combined) == len(xa_high) + len(xa_low))
