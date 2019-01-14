# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 22:46:52 2019

@author: Administrator
"""
import random
import numpy as np

sourcefile="D:\学习资料\人工智能\Gene_Chip_Data\E-TABM-185.sdrf.txt"

trXX = np.loadtxt('data_dimRed_full.txt')

fy = open(sourcefile,'r')
attr=fy.readline()
attr=attr.strip('\n')
attr=attr.split('\t')
attr_sets=list()
attr_dicts=list()

class_index=7
threshold=0
print("attribute :",attr[class_index])
label_list=list()
trY=list()
index_list=list()
m=0
attr_dict=dict()
for i in range(5896):
        line_y=fy.readline()
        
        line_y=line_y.split('\t')[class_index]
        
        if(line_y=='  '):
               continue
        if(line_y in attr_dict):
               attr_dict[line_y]+=1
        else:
               attr_dict[line_y]=1
        if(attr_dict[line_y])<threshold:
               continue
        #line_y= fy.readline().split('\t')[class_index]
        index_list.append(i)
        if(line_y in label_list):
               line_y=label_list.index(line_y)
        else:
               label_list.append(line_y)
               line_y=len(label_list)-1
        trY.append(line_y)
        
trX=trXX[index_list]
print("valid data has :",len(trX))
print("the label classification :",len(label_list))
trY=np.array(trY)

print("shuffling")
data_class_list = list(zip(trX, trY))  # zip压缩合并，将数据与标签对应压缩
random.shuffle(data_class_list)                     # 将data_class_list乱序
index = int(len(data_class_list) *0.1) + 1   # 训练集和测试集切分的索引值
train_list = data_class_list[index:]                # 训练集
test_list = data_class_list[:index]                 # 测试集
train_data_list, train_class_list = zip(*train_list)  # 训练集解压缩
test_data_list, test_class_list = zip(*test_list)

train_data_list=np.array(train_data_list)
train_class_list=np.array(train_class_list)
test_data_list=np.array(test_data_list)
test_class_list=np.array(test_class_list)

np.save("train_data.npy",train_data_list)
np.save("train_class.npy",train_class_list)
np.save("test_data.npy",test_data_list)
np.save("test_class.npy",test_class_list)


# for i in range(len(attr)):
#        attr_sets.append(set())
# for i in range(len(attr)):
#        attr_dicts.append(dict())
# data=f.readlines()
# for line in data:
#        line=line.strip('\n')
#        line=line.split('\t')
#        for i in range(1,len(attr)):
#               attr_sets[i].add(line[i])
#               if not line[i] in attr_dicts[i]:
#                      attr_dicts[i][line[i]]=1
#               else:
#                      attr_dicts[i][line[i]]=attr_dicts[i][line[i]]+1
 # for key in attr_dicts[7]:
 #        if attr_dicts[7][key]<10:
 #               attr_sets[7].remove(key)



