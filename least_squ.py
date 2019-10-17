#!/usr/bin/env python

# Creat drilling_time and cost files based on the new target files from RMS and platform position file 
## Written by Tao Feng

import optparse
import math
import os, sys
import re
import pandas as pd
import numpy as np
import datetime

df=pd.read_csv('pres1.txt', sep='\s+', names=['x', 'y'])
dxt=df.as_matrix(columns=['x'])
dyt=df.as_matrix(columns=['y'])
print dxt.T
print dyt.T
dx=dxt.T
dy=dyt.T

dx=np.array([2667.4,2686.2, 2683.4, 2680.1, 2676.6, 2672.1, 2669.6, 2668.8, 2665.9, 2664.2,2663.2])
dy=np.array([210.16, 211.6,  211.31, 210.98, 210.82, 210.43, 210.29, 210.23, 210.05, 211.35, 209.87])

x=np.array([2710.4, 2733.4])
y=np.array([214, 216.32])
print x


A=np.vstack([x,np.ones(len(x))]).T
m,c =np.linalg.lstsq(A,y, rcond=None)[0]


dA=np.vstack([dx,np.ones(len(dx))]).T
dm,dc =np.linalg.lstsq(dA,dy, rcond=None)[0]


p=m*2672+c

dp=dm*2672+dc
print p
print dp
