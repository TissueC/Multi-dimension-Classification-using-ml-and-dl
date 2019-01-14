# -*- coding: utf-8 -*-

import numpy as np
from sklearn.linear_model import LogisticRegression as LR
import random

    #train
output_option=3
if __name__ == '__main__':
    train_data_list=np.load('../train_data.npy')
    test_data_list=np.load('../test_data.npy')
    train_class_list=np.load('../train_class.npy')
    test_class_list=np.load('../test_class.npy')
    print("training")
    acc_list=list()
    iteration=list()
    for k in range(1,50):
           clf = LR(solver='sag',
                    max_iter=k, 
                    random_state=1,
                    multi_class='auto')
           clf.fit(train_data_list,train_class_list)
           predict_y=clf.predict(test_data_list)
           
           wrong=0
           right=0
           for i in range (len(test_data_list)):
                  if predict_y[i]==test_class_list[i]:
                         right+=1
                  else:
                         wrong+=1
           acc=float(right)/len(test_data_list)
           iteration.append(k)
           acc_list.append(acc)
    acc_list=np.array(acc_list)
    iteration=np.array(iteration)
if(output_option==1):
       np.save('log_material_x.npy',iteration)
       np.save('log_material_y.npy',acc_list)
if(output_option==2):
       np.save('log_bio_x.npy',iteration)
       np.save('log_bio_y.npy',acc_list)
if(output_option==3):
       np.save('log_stage_x.npy',iteration)
       np.save('log_stage_y.npy',acc_list)
if(output_option==4):
       np.save('log_state_x.npy',iteration)
       np.save('log_state_y.npy',acc_list)