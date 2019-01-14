# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

    #train
output_option=4
if __name__ == '__main__':
    y=list()
    x=list()
    f=open('verbose.txt','r')
    lines=f.readlines()
    i=1
    for line in lines:
           x.append(i)
           i+=1
           line=line.strip('\n').split('= ')
           y.append(eval(line[1]))
    x=np.array(x)
    y=np.array(y)
    
    f.close()
    
if(output_option==1):
       np.save('mlp_material_x.npy',x)
       np.save('mlp_material_y.npy',y)
if(output_option==2):
       np.save('mlp_bio_x.npy',x)
       np.save('mlp_bio_y.npy',y)
if(output_option==3):
       np.save('mlp_stage_x.npy',x)
       np.save('mlp_stage_y.npy',y)
if(output_option==4):
       np.save('mlp_state_x.npy',x)
       np.save('mlp_state_y.npy',y)