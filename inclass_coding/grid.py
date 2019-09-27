# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 17:57:49 2019

@author: dahaynes
"""


myGrid = [[1,1,3,3],\
          [2,4,6,8]]

newlist = []
mySum = 0
myCounter = 0
myColValue = 0



for k, row in enumerate(myGrid):
    print(row)
    theRowSum = sum(row)
    
    for j, r in enumerate(row):
        newlist.append(r)
        mySum = mySum + r
        if j == 0: 
            myColValue += r
        #mySum += r
