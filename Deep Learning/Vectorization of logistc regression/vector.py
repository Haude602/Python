#z = w(t)*x + b vectorization of logistic relation function
# in python z = np.dot(w,x) + b
# note use a = np.random.rand(5,1) not a= np.random.rand(5)(rank 1 array)

import numpy as np

import time
a = np.random.rand(100000) #creates million dimensional arrays
b = np.random.rand(100000)
tic = time.time() #measures current time
c = np.dot(a,b)
toc = time.time()
print("vectorized version :"+ str(1000*(toc-tic))+"ms") # print time to calculate in ms(*1000) i.e. faster nad best for ML

c = 0
tic = time.time()
for i in range(100000): #time taken by for loop in non-vectorized form
  c += a[i]*b[i]
toc = time.time()
print(c)
print("for loop:" + str(1000*(toc-tic)) + "ms")