# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 15:20:57 2018

@author: Lidor
"""

from VectorModule import Vector

class Matrix:
    """Represents a matrix.
    Attributes: content - vectors, shape"""
    def __init__(self, vec_list):
        "Constructor: receives vectors list, builds a matrix"
        vector=Vector([1,2])
        if type(vec_list[0]) != type(vector):
            return None
        vec_length=len(vec_list[0])
        new_list=[]
        for v in vec_list:
            if type(v) != type(vector) or len(v) != vec_length:
                return None
            new_list.append(v)
        self.content=tuple(new_list)
        rows=len(self.content)
        columns=len(self.content[0])
        self.shape=(rows, columns)
        
    def __add__(self, other):
        "Add 2 matrix"
        if self.shape[0]!=other.shape[0] or self.shape[1]!=other.shape[1]:
            return None
        new_list=[]
        for i in range(self.shape[0]):
            new_list.append(self.content[i]+other.content[i])
        return Matrix(new_list)
    
    def transpose(self):
        "Transpose matrix"
        vec_list=[]
        for i in range(self.shape[1]):
            list1=[]
            for j in range(self.shape[0]):
                list1.append(self.content[j].__getitem__(i))
            v=Vector(list1)
            vec_list.append(v)
        m=Matrix(vec_list)
        return m
    
    def __mul__(self, other):
        "Multiplies 2 matrix"
        if self.shape[1]!=other.shape[0]:
            return None
        transposed=other.transpose()
        vec_list=[]
        list1=[]
        for i in range(self.shape[0]):
            for j in range(other.shape[1]):
                list1.append(self.content[i]*transposed.content[j])
            vec_list.append(Vector(list1))
            list1=[]
        m=Matrix(vec_list)
        return m