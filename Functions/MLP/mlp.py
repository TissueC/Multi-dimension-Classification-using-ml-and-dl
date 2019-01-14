# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 15:37:47 2019

@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPClassifier as MLP

    #train
if __name__ == '__main__':
    train_data_list=np.load('../train_data.npy')
    test_data_list=np.load('../test_data.npy')
    train_class_list=np.load('../train_class.npy')
    test_class_list=np.load('../test_class.npy')
    print("training")
    clf = MLP(solver='adam', 
              alpha=0.1,
              hidden_layer_sizes=(256,256),
              activation='tanh',
              random_state=1,
              max_iter=400,
              verbose=1)
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
    print('mlp: ',acc)

        
        