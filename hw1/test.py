# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:49:50 2019

@author: gzha
"""
import re

#s = re.sub(r'[^\w\s]','',s)
a=' a b '
print(a.strip())
print(a[:10])

from sklearn.feature_extraction.text import TfidfVectorizer

corpus = ["welcome to stackoverflow my friend", 
          "my friend, don't worry, you can get help from stackoverflow"]
vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform(corpus)
print(matrix)
d=[re.sub(r'[^\w\s]','',corpus[0]),re.sub(r'[^\w\s]','',corpus[1])]
print(d)
print(vectorizer.fit_transform(d))

bank=set()
bank.add('I.')
bank.add('V.')
bank.add('X.')
bank.add('IV')
bank.add('VI')
bank.add('IX')
bank.add('XI')
bank.add('II')
bank.add('VI')
bank.add('XI')
bank.add('VI')
#print(bank)
c='VIII. THE ADVENTURE OF THE SPECKLED BAND'
#print(c[0:2])
#print(c[0:2] in bank)
#print(len("Book "))