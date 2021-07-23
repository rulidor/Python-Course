# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 23:50:08 2018

@author: Lidor
"""

def longestSet(numbers_set, size, i, maxfinal, count):
    if i==size:
        return count
    length1 = longestSet(numbers_set, size, i + 1, maxfinal, count)
    if numbers_set[i] > maxfinal:
        length2 = longestSet(numbers_set, size, i + 1, numbers_set[i], count + 1)
        if length2 > length1:
            length1 = length2
    return length1