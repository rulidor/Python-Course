# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 01:55:56 2018

@author: Lidor
"""

def partition(lst,s1,s2, memo):
    if not lst:
        return s1 == s2
    key = (len(lst) , s1 , s2)
    if key not in memo:
        give_Liora = partition(lst[1:],s1+lst[0],s2,memo)
        give_Yosi = partition(lst[1:],s1,lst[0] + s2,memo)
        memo[key] = give_Liora or give_Yosi 

    return memo[key] 

print(partition([9,6,4],0,0,{}))


