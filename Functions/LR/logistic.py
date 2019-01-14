import numpy as np
from sklearn.linear_model import LogisticRegression as LR
import random

    #train

if __name__ == '__main__':
    train_data_list=np.load('../train_data.npy')
    test_data_list=np.load('../test_data.npy')
    train_class_list=np.load('../train_class.npy')
    test_class_list=np.load('../test_class.npy')
    clf = LR(solver='sag', max_iter=100, random_state=1,multi_class='auto')
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
    print ('log: ',acc)

        
        