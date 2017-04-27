#!/usr/bin/python

from numpy import *

dt=10e-3
n=100
ts=arange(0,n)*dt

for i,t in enumerate(ts):
    print("%.3f %i"%(t,i))
