# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 17:44:45 2018

@author: Lidor
"""

from math import sqrt
from math import acos
from math import degrees

class Vector:
    """Represents a vector.
       Attributes: vec - tuple of coordinates"""
    def __init__(self, c_list):
        "Constructor: receives coordinates list, saves them as tuple"
        self.vec=tuple(c_list)
    
    def __repr__(self):
        "Returns vector as string"
        res='('
        for i in range(len(self.vec)-1):
            res+=str(self.vec[i])+','
        res+=str(self.vec[i+1])+')'
        return res
    
    def __len__(self):
        "Returns vector's length, as string"
        return len(self.vec)
    
    def __eq__(self, other):
        "Returns True if length of 2 vectors equal and same coordinates. Else, returns False"
        return self.__len__()==other.__len__() and self.vec==other.vec
    
    def __add__(self, other):
        "Returns new vector, which is sum of other vector and this vector"
        if self.__len__() != other.__len__():
            return None
        coord_list=[]
        for i in range(self.__len__()):
            coord_list.append(self.vec[i] + other.vec[i])
        return Vector(coord_list)
    
    def __neg__(self):
        "Returns neg. vector of this vector"
        list1=[]
        for i in range(self.__len__()):
            list1.append(self.vec[i]*(-1))
        return Vector(list1)
    
    def __sub__(self, other):
        "Returns subtraction vector"
        if self.__len__() != other.__len__():
            return None
        res_vector=self.__add__(other.__neg__())
        return res_vector
  
    def __mul__(self, other):
        "Multiplies 2 vectors, or a vector and a scalar"
        if type(other)==type(self):
            if self.__len__() != other.__len__():
                return None
            sum1=0
            for i in range(self.__len__()):
                sum1+=self.vec[i] * other.vec[i]
            return sum1
        if type(other)==type(1) or type(other)==type(1.0):
            list1=[]
            for i in range(self.__len__()):
                list1.append(self.vec[i]*other)
            return Vector(list1)
    
    def __rmul__(self, other):
        "Multiplies scalar by vector"
        return self.__mul__(other)
    
    def __getitem__(self, i):
        "Returns coordinate in i'th place"
        return self.vec[i]
    
    def norm(self):
        "Returns the vector's normal"
        return sqrt(self.__mul__(self))
    
    def angle(self, other):
        "Returns angle between 2 vectors, by degrees"
        return degrees(acos((self.__mul__(other)/(self.norm()*other.norm()))))