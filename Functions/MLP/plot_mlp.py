# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x1=np.load('mlp_material_x.npy')
y1=np.load('mlp_material_y.npy')

x2=np.load('mlp_bio_x.npy')
y2=np.load('mlp_bio_y.npy')

x3=np.load('mlp_stage_x.npy')
y3=np.load('mlp_stage_y.npy')

x4=np.load('mlp_state_x.npy')
y4=np.load('mlp_state_y.npy')

x1=list(x1)
x2=list(x2)
x3=list(x3)
x4=list(x4)
y1=list(y1)
y2=list(y2)
y3=list(y3)
y4=list(y4)


plt.title('MLP result in Characteristics [DiseaseStage]',fontsize='xx-large')
plt.xlabel('iteration',fontsize='xx-large')
plt.ylabel('loss',fontsize='xx-large')

plt.plot(x1,y1,color='blue',label='identity')
plt.plot(x2,y2,color='red',label='logistic')
plt.plot(x3,y3,color='green',label='tanh')
plt.plot(x4,y4,color='orange',label='relu')
plt.legend(fontsize='xx-large')


plt.ylim(0,0.1)
plt.xticks(fontsize='xx-large')
plt.yticks(fontsize='xx-large')


