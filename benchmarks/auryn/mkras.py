#!/usr/bin/python
from numpy  import *
import pylab as pl
import scipy.misc


dt = 0.05 


img = scipy.misc.imread("auryn_logo_small.png")
jitter = random.rand(*img.shape)/3*dt

n = img.shape[0]
grid = dt*img.shape[1]
print("# neurons %i, temporal resolution %fs, time grid %fs"%(n, dt, grid))
pl.imshow(img)
pl.show()

for j in xrange(img.shape[1]):
    for i in xrange(img.shape[0]):
        time = dt*j+jitter[i,j]
        if img[i,j]>0.0 and time<grid:
            print("%f %i"%(time,n-i))
