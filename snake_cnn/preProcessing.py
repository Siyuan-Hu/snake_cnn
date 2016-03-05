#coding:utf-8
"""
Author:wepon
Source:https://github.com/wepe
file:data.py
"""

import os
from PIL import Image
import numpy as np
#import six.moves.cPickle as pickle

height=10

def load_data(url):
    up=0
    down=0
    right=0
    left=0

    print "begin to read data"
    f = open(url,"r")  
    lines = f.readlines()
    #print len(lines)
    num=len(lines)/(height+1)
    #print num

    arr2=[]
    y_train=[]
    for i in range(num):
        arr1=[]
        arr=[]
        for j in range(height):
            line=lines[i*(height+1)+j]
            line=line.rstrip('\n')
            arr.append(map(int,line.split()))
        arr1.append(arr)
        arr2.append(arr1)
        line=lines[i*(height+1)+height]

        numDir=int(line)
        if numDir==0:
            up+=1
        if numDir==1:
            right+=1
        if numDir==2:
            down+=1
        if numDir==3:
            left+=1

        y_train.append(int(line))


    x_train=np.asarray(arr2)
    x_train=x_train.astype('float32')
    x_train /= 3
    #print x_train
    y_train=np.asarray(y_train)
    #print y_train

    print up
    print right
    print down
    print left
    return x_train,y_train
dd,ll=load_data("train.data")
#print ll[1]

