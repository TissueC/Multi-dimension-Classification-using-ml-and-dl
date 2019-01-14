# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x1=np.load('log_material_x.npy')
y1=np.load('log_material_y.npy')

x2=np.load('log_bio_x.npy')
y2=np.load('log_bio_y.npy')

x3=np.load('log_stage_x.npy')
y3=np.load('log_stage_y.npy')

# x4=np.load('log_state_x.npy')
# y4=np.load('log_state_y.npy')

x1=list(x1)
x2=list(x2)
x3=list(x3)
# x4=list(x4)
y1=list(y1)
y2=list(y2)
y3=list(y3)
# y4=list(y4)



plt.title('LR Result Analysis',fontsize='xx-large')
plt.xlabel('iteration',fontsize='xx-large')
plt.ylabel('accurate',fontsize='xx-large')

plt.plot(np.linspace(0,50,10000),np.ones(10000),linestyle='--',color='black')
plt.plot(x1,y1,color='blue',label='material')

plt.plot(x2,y2,color='red',label='biosource type')
plt.plot(x3,y3,color='green',label='disease stage')
# plt.plot(x4,y4,color='black',label='disease state')
plt.legend(loc='lower right', fontsize='xx-large',frameon=False)

plt.xticks(fontsize='xx-large')
plt.yticks(fontsize='xx-large')

plt.savefig('log.jpg')

