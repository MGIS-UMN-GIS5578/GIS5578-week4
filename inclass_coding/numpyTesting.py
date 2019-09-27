# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:47:52 2019

@author: dahaynes
"""

import numpy as np
myListGrid = [[1,4,23,1],[1,45,6,7]]

myGrid = np.array(myListGrid)


row, col = myGrid.shape
oneVar = myGrid.shape
for r in range(row):
    print(myGrid[r,:].sum())
    
for c in range(col):
    print(myGrid[:,c].sum())