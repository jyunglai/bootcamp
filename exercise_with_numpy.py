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
