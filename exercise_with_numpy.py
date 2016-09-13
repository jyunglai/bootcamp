import numpy as np

#Load data
xa_high = np.loadtxt('data/xa_high_food.csv', comments = '#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments = '#')

def xa_to_diameter(xa):
    """
    Convert an array of cross seciontal areas to diamters
    """
    #Compute diameter from area
    # A = pi * d^2 / 4
    diameter = np.sqrt(xa * 4 / np.pi)

    return diameter

#2 Dimensional arrays
#Example
a = np.array([[6.7, 1.3, 0.6, 0.7],
              [0.1, 5.5, 0.4, 2.4],
              [1.1, 0.8, 4.5, 1.7],
              [0.0, 1.5, 3.4, 7.5]])

b = np.array([1.1, 2.3, 3.3, 3.9])

#Print out row 1 of a
a[1,:]

#Print out coluns 1 and 3 of a
a[:,[1,3]]

#Print out values of entry in a that is greater than 2
a > 2

#Find values larger than 2 and return as an array
a[a > 2]

#Retrieves the diagonal values from a 2 dimensional array (More than 2d?) as an array
np.diag(a)

#Use .shape to check if the array is the same size
ones_array = np.ones(a.shape)
ones_array.shape = a.shape #Returns true

#A x = b ; Use np.linalg.solve to solve a linear matrix equation
np.linalg.solve(a,b)

#Matix multiplication np.dot
np.dot(a,b)

#Transpose np.Transpose

#Inverse np.linalg.inv(_)

#Make 2d array into 1d, np.ravel(_)

#Change the shape of an array np.reshape(_)

def easy_reshape(obj, ncols, order = 'C'):
    """
    Guarantee that reshaping works by defining only one shape parameter
    """

    #reshape
    arr = np.reshape(obj, (ncols, len(obj)/ncols), order)

    return arr
