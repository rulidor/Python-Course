# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 20:30:40 2018

@author: Lidor
"""

from VectorModule import Vector
from Matrix import Matrix

m1=Matrix([Vector([1,2,3]),Vector([4,5,6])])
m2=Matrix([Vector([7,8,9,10]), Vector([9,10,11,12]), Vector([11,12,13,14])])
print((m1*m2).content)

#list1=[1,2,3]
#print(tuple(list1))
#
#for i in range(10):
#    print(i)
#print('************')
#print(i+1)