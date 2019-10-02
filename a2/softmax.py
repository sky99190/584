# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 09:23:06 2019

@author: gzha
"""
import numpy as np
def softmax(x):
    ndim=x.ndim
    maxValueInRow=np.max(x,axis=ndim-1)
    numerator=np.exp(x-maxValueInRow)
    denominator=np.sum(numerator,axis=ndim-1)
    y=numerator/denominator
    return y

testArray=np.array([1,2,3,4,5])
testMatrix=np.matrix([[1,3,4],[2,6,8],[9,10,11]])
print(softmax(testArray))
print(softmax(testMatrix))