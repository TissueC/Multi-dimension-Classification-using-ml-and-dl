


import numpy as np
import matplotlib.pyplot as plt


f=open('acc_alpha.txt','r')
data=f.readlines()
x1=np.linspace(0.01,0.11551724137931035,35)
y1=list()
for line in data:
       line=eval(line.strip('\n'))
       y1.append(line)
y1=np.array(y1)



plt.title('MLP accuracy rate vs L2 penalty',fontsize='xx-large')
plt.xlabel('L2 penalty',fontsize='xx-large')
plt.ylabel('accuracy',fontsize='xx-large')

plt.plot(x1[2:],y1[2:],color='black')
# plt.plot(x2,y2,color='red',label='logistic')
# plt.plot(x3,y3,color='green',label='tanh')
# plt.plot(x4,y4,color='orange',label='relu')
plt.legend(fontsize='xx-large')

#plt.ylim(0,0.1)
plt.xticks(fontsize='xx-large')
plt.yticks(fontsize='xx-large')