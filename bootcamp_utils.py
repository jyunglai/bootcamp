import numpy as np

#Example in creating a module
#bootcamp utils: A collection of statistical functions
#proved useful for 53 students

#Empirical cumulitive distribution function
def ecdf(data):
    '''
    Compute x, y values for an empirical distribution function
    '''

    x = np.sort(data)
    y = np.arange(1, 1+len(x)) / len(x)

    return x, y
