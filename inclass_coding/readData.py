# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:30:02 2019

@author: dahaynes
"""

import csv
f = open(r"c:\work\data.txt")
data = f.read()

fin = open(r"c:\work\data.txt")
data = csv.reader(fin, delimiter= ",")