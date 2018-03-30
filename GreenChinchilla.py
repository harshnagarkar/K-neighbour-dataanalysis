# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 11:40:42 2018
Green Chinchilla
Harsh Nagarkar
Challenge 4
"""
#importing libraries
from __future__ import division
import matplotlib.pyplot as mplot
import pandas as pd
import math
import numpy as np

#pandas extracting data
data = pd.read_csv('data.csv',header=None)
outline = pd.read_csv('us_outline.csv',header=None)

#distance calculation function along with color
def dcal(a,b):
	return [math.sqrt(math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2)),b[2]]

#asking user for input
k = raw_input("Enter the k value:- \n")
k = int(k)

#iniating lists of values for ease of calculation
datay=data.iloc[:,0:1].values 
datax=data.iloc[:,1:2].values
color=data.iloc[:,2:3].values
listdis = outline.iloc[:,0:2].values

#initaiting counters
distance=[]
px =[]
py=[]
pc = []
datalength = len(datax)

#x values
for i in range(0,120):
    #y values
    for j in  range(0,194):
        #distance calculatoin
        for n in range(datalength):
          distance.append(dcal([datax[n],datay[n]],[i,j,color[n]]))
          distance[-1][-1]=distance[-1][-1][0]
          
          #sorting data
        distance=sorted(distance)
        distance = distance[0:k]
        
        #getting colots
        d,c = zip(*distance)
        #averaging
        col = np.mean(c)
        distance = []
        #appending to list
        px.append(j)
        py.append(i)
        pc.append(col)
        
        #plotting outline
mplot.plot(outline.iloc[:,0:1].values,outline.iloc[:,1:2].values,c='#000000')
           #plotting x, y and color values
mplot.scatter(px, py, c=pc, marker = 's', cmap="viridis")

#displaying graph
mplot.show