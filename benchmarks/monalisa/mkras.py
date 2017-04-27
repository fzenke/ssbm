#!/usr/bin/python
from numpy  import *
import pylab as pl
import scipy.misc


dt = 0.10 

imgc = scipy.misc.imread("mona-lisa.png")
img  = imgc.mean(2)
jitter = random.rand(*img.shape)/3*dt

n = img.shape[0]
print("# neurons %i, temporal resolution %fs, time grid %fs"%(n, dt, dt*img.shape[1]))
pl.imshow(img)
pl.show()

for j in xrange(img.shape[1]):
    for i in xrange(img.shape[0]):
        if img[i,j]==0.0:
            print("%f %i"%(dt*j+jitter[i,j],n-i))
