# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re
import random
from sklearn.feature_extraction.text import TfidfVectorizer

def checkTitle_pg1661(a):
    if type(a)!=str:
        return
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
    if a[0:2] in bank or a[0:13]=="ADVENTURE IV.":
        #print(a)
        return 1
    else:
        return 0

def checkTitle_pg280540(a):
    if type(a)!=str:
        return
    bank=set()
    bank.add('PART ')
    bank.add('Book ')
    bank.add('Chapter ')
    if a[0:8] in bank or a[0:5] in bank:
        #print(a)
        return 1
    else:
        return 0
    
def checkTitle_pg31100(a):
    if type(a)!=str:
        return
    bank=set()
    bank.add('Chapter ')
    bank.add('CHAPTER ')
    
    if a[0:9] in bank :
        #print(a)
        return 1
    else:
        return 0
    
def pg1661():
    fp=open('data/pg1661.txt','r',encoding='utf8');#读文件内容
    start="To Sherlock Holmes she is always THE woman. I have seldom heard\n"
    end="End of the Project Gutenberg EBook of The Adventures of Sherlock Holmes, by \n"
    line=fp.readline()
    while line!=start:
        line=fp.readline()
        
    p=[]
    pAll=''
    while line and line!=end:
        data=line.strip('\n')
        line=fp.readline()
        while line!='\n':
            line=line.strip('\n')
            line=re.sub(r'[^\w\s]','',line)
            data=data+' '+line
            line=fp.readline()
        p.append(data)
        pAll=pAll+' '+data
        while line=='\n' or line.strip()=='' or checkTitle_pg1661(line)==1:
            line=fp.readline()
    fp.close()
    
    return p,pAll
    
def pg31100():
    fp=open('data/pg31100.txt','r',encoding='utf8');#读文件内容
    start="Sir Walter Elliot, of Kellynch Hall, in Somersetshire, was a man who,\n"
    end="End of the Project Gutenberg EBook of The Complete Works of Jane Austen,\n"
    line=fp.readline()
    while line!=start:
        
        line=fp.readline()
        
    p=[]
    pAll=''
    while line and line!=end:
        data=line.strip('\n')
        line=fp.readline()
        while line!='\n':
            line=line.strip('\n')
            line=re.sub(r'[^\w\s]','',line)
            data=data+' '+line
            line=fp.readline()
        p.append(data)
        pAll=pAll+' '+data
        while line=='\n' or line.strip()=='' or checkTitle_pg31100(line)==1:
            line=fp.readline()
    fp.close()
    return p,pAll
    
    
    
def pg280540():
    fp=open('data/28054-0.txt','r',encoding='utf8');#读文件内容
    start="Alexey Fyodorovitch Karamazov was the third son of Fyodor Pavlovitch\n"
    end="***END OF THE PROJECT GUTENBERG EBOOK THE BROTHERS KARAMAZOV***\n"
    line=fp.readline()
    while line!=start:
        
        line=fp.readline()
        
    p=[]
    pAll=''
    while line and line!=end:
        data=line.strip('\n')
        line=fp.readline()
        while line!='\n':
            line=line.strip('\n')
            line=re.sub(r'[^\w\s]','',line)
            data=data+' '+line
            line=fp.readline()
        p.append(data)
        pAll=pAll+' '+data
        while line=='\n' or line.strip()=='' or checkTitle_pg280540(line)==1:
            line=fp.readline()
    fp.close()
    return p,pAll
    
p1,p1All=pg1661()
p2,p2All=pg31100()
p3,p3All=pg280540()

p1s=random.shuffle(random.shuffle(p1))
p2s=random.shuffle(random.shuffle(p2))
p3s=random.shuffle(random.shuffle(p3))
vectorizer = TfidfVectorizer()
matrix = vectorizer.fit_transform([p1All,p2All,p3All])
print(matrix)