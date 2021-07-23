# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 16:23:44 2020

@author: Lidor
"""

tuples = [(0,1,2),
          (3,4,5),
          (6,7,8)]

for t in tuples:
    for i in range(2):
        print(str(t[i]) + " ",end=" ")
    print(str(t[2]))