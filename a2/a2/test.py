# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 17:51:22 2019

@author: gzha
"""
import numpy as np
def normalizeRows(x):
    dem=np.sqrt(np.sum(np.power(x,2),axis=1))
    print(dem)
    y=x/dem
    return y

def normalizeRows2(x):
    """ Row normalization function

    Implement a function that normalizes each row of a matrix to have
    unit length.
    """
    N = x.shape[0]
    x =x/ np.sqrt(np.sum(x**2, axis=1)).reshape((N,1)) 
    return x
testArray=np.array([1,2,3,4,5])
testMatrix=np.matrix([[1,3,4],[2,6,8],[9,10,11]])
#print(normalizeRows(testArray))
print(normalizeRows(testMatrix))
print(normalizeRows2(testMatrix))
print(np.sum(np.power(normalizeRows(testMatrix),2),axis=1))