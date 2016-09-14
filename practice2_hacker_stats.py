import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import bootcamp_utils

#Create config for mathplotlib rc params
rc = {'lines.linewidth': 2, 'axes.labelsize': 18, 'axes.titlesize': 18}
sns.set(rc=rc)

#Load in the data
bd_1975 = np.loadtxt('data/beak_depth_scandens_1975.csv')
bd_2012 = np.loadtxt('data/beak_depth_scandens_2012.csv')

#Generate ECDF values
def generateECDFValues(data):
    """
    Generates x and y values for the ECDF of the data
    """

    
