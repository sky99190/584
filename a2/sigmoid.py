# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:39:06 2019

@author: gzha
"""

import numpy as np
def sigmoid(x):
    denominator=1+np.exp(-x)
    y=1/denominator
    return y

def sigmoid_gradient(sig):
    return sig-pow(sig,2)


testArray=np.array([1,2,3,4,5])
testMatrix=np.matrix([[1,3,4],[2,6,8],[9,10,11]])
print(sigmoid(testArray))
print(sigmoid(testMatrix))