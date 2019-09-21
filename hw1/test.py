# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:49:50 2019

@author: gzha
"""
import re
import numpy as np
#s = re.sub(r'[^\w\s]','',s)
a=' a b '
print(a.strip())
print(a[:10])

from sklearn.feature_extraction.text import TfidfVectorizer
'''
corpus = ["welcome to stackoverflow my friend", 
          "my friend, don't worry, you can get help from stackoverflow"]
vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(corpus)
print(matrix)
d=[re.sub(r'[^\w\s]','',corpus[0]),re.sub(r'[^\w\s]','',corpus[1])]
print(d)
print(vectorizer.fit_transform(d))
'''

vectorizer = TfidfVectorizer()
x_t=['This is an apple', 'This is a car','this is not a car']
x_e=['This is a not a apple']
print(x_t+x_e)
vectorizer.fit(x_t)
tfidf_t=vectorizer.transform(x_t)
tfidf_e=vectorizer.transform(x_e)
print(vectorizer.get_feature_names())
print(tfidf_t.toarray())
print(tfidf_e.toarray())
x=[[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7],[7,8,9,10],[9,10,11,12]]
y=[[1,0],[1,0],[1,0],[0,1],[1,1],[0,0]]
w=[[1,1],[1,1],[1,1],[1,0],[1,1],[0,1]]

x=np.array(x)
y=np.array(y)
print(y+w)
i=10
print("gd iteration on class ",i)
print(np.dot(x,y))
print(y[:,1])
print(y.shape)
randI=np.random.permutation(6)
y=y[randI,:]
print(y)
