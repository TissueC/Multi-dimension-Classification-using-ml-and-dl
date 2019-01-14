# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 20:23:57 2019

@author: Administrator
"""
import numpy as np
from sklearn.decomposition import PCA
if __name__ == '__main__':

    sourcefile = '../microarray.original.txt'
    f = open(sourcefile,'r')
    f.readline()

    print ("Now reading data...")

    ######test######

    # num = 0
    # for i in range(0,22283):
    #     line = f.readline()
    #     line = line[:-1].split('\t')
    #     # line = map(string.atof,line[1:])
    #     if string.atof(line[1])>=5:
    #         num+=1
    ######test######

    num = 0
    data = []
    for i in range(0,22283):
        line = f.readline()
        line = line[:-1].split('\t')
        #if float(line[1])<10:
            #continue
        num+=1
        line = line[1:]
        line = list(map(float,line))
        data.append(line)

    f.close()

    print ("Data has been read successfully.")
    print ("The dimension is "+str(num))


    data = np.array(data).T
    print ("Now reducing dimension...")
    pca=PCA(n_components=0.9)
    pca.fit(data)
    lowDData=pca.transform(data)
    print ("Finished, the new dimension is :"+str(len(lowDData[0])))

    print ("Start writing new data...")
    destfile = '../data_dimRed_full.txt'
    f = open(destfile,'w')
    for i in range(0,len(lowDData)):
        for j in range(0,len(lowDData[i])):
            f.write(str(lowDData[i][j])+'\t')
        f.write('\n')

    print ("Finished the whole work.")

    # testArray = np.array([[4,3,2],[3,2,1],[2,0,0]])
    # lowd,res = pca(testArray)
    # print res
