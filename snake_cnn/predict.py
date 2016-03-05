from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.utils import np_utils
from read import load_data
from cnn import training

model=training()
X_test,Y_test=load_data("test.data")
batch_size = 1
test=[]
test.append(X_test[0])
print("warning:")
print(test)
print("warning2:")
print(X_test)
out=model.predict(X_test,batch_size=batch_size,verbose=1)
print('out=',out)