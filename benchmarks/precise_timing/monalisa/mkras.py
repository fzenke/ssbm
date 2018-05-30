#!/usr/bin/python3
from numpy  import *
import matplotlib.pyplot as plt
import scipy.misc


dt = 0.10 

imgc = scipy.misc.imread("mona-lisa.png")
img  = imgc.mean(2)
jitter = random.rand(*img.shape)*dt

n = img.shape[0]
print("# neurons %i, temporal resolution %fs, time grid %fs"%(n, dt, dt*img.shape[1]))
plt.imshow(img)
plt.show()

for j in range(img.shape[1]):
    for i in range(img.shape[0]):
        if img[i,j]==0.0:
            print("%f %i"%(dt*j+jitter[i,j],n-i))
