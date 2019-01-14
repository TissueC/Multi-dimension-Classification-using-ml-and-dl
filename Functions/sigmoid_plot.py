# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 02:10:33 2019

@author: Administrator
"""
import numpy as np
import matplotlib.pyplot as plt

x=list()
y=list()
for i in np.linspace(-6,6,1000):
       x.append(i)
       y.append(1/(1+np.exp(-i)))
x=np.array(x)
y=np.array(y)
plt.xlabel('x')
plt.ylabel('y')
plt.plot(np.linspace(-6,6,1000), 0.5*np.ones(1000), color='black')
plt.yticks(np.arange(0,1, 0.1))
plt.plot(x,y)