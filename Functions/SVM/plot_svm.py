# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 04:24:03 2019

@author: Administrator
"""

import numpy as np
import matplotlib.pyplot as plt

x1=np.load('svm_material_x.npy')
y1=np.load('svm_material_y.npy')

x2=np.load('svm_bio_x.npy')
y2=np.load('svm_bio_y.npy')

x3=np.load('svm_stage_x.npy')
y3=np.load('svm_stage_y.npy')

x4=np.load('svm_state_x.npy')
y4=np.load('svm_state_y.npy')

x1=list(x1)
x2=list(x2)
x3=list(x3)
x4=list(x4)
y1=list(y1)
y2=list(y2)
y3=list(y3)
y4=list(y4)



plt.title('SVM Result Analysis',fontsize='xx-large')
plt.xlabel('iteration',fontsize='xx-large')
plt.ylabel('accuracy',fontsize='xx-large')

plt.plot(np.linspace(0,150,10000),np.ones(10000),linestyle='--',color='black')

plt.plot(x1,y1,color='blue',label='Material Type')
plt.plot(x2,y2,color='red',label='BioSource Type')
plt.plot(x3,y3,color='green',label='Disease Stage')
plt.plot(x4,y4,color='orange',label='Disease State')

plt.xticks(fontsize='xx-large')
plt.yticks(fontsize='xx-large')
plt.legend(loc='lower right', fontsize='xx-large',frameon=False)

plt.savefig('svm.jpg')

