import numpy as np
import scipy.special
import matplotlib.pyplot as plt
import seaborn as sns

#Problem 3:2 Data Collapse
#Part a - Load 3 data sets
wt_lac = np.loadtxt('data/wt_lac.csv', delimiter=',', skiprows=3)
q18m_lac = np.loadtxt('data/q18m_lac.csv', delimiter=',', skiprows=3)
q18a_lac = np.loadtxt('data/q18a_lac.csv', delimiter=',', skiprows=3)
