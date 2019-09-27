# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 18:55:10 2019

@author: dahaynes
"""
stringList = []
f = open(r"c:\work\items_inner.txt", "w")
for i in range(1,12):
    stringList.append(str(i))
    f.write("\n".join(stringList))

f.close()


f = open(r"c:\work\items_simple.txt", "w")
for i in range(1,12):
    f.write("%s\n" % (i))
    #f.write(str(i)+ "\n" )

f.close()


with open(r"c:\work\test1.txt" 'r') as fin, open(r"c:\work\test3.txt" ,'w') as fout:
    fin.read()
    fout.write()

    
    