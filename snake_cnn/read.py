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
    print "begin to read data"
    f = open(url,"r")  
    lines = f.readlines()
    print len(lines)
    num=len(lines)/(height+1)
    print num

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
        y_train.append(int(line))

    x_train=np.asarray(arr2)
    x_train=x_train.astype('float32')
    x_train /= 3
    print x_train
    y_train=np.asarray(y_train)
    print y_train
    return x_train,y_train
#dd,ll=load_data()
#print ll[1]

