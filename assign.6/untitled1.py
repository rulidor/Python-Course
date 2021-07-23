# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 18:35:30 2018

@author: Lidor
"""

def partition(lst, values_lst):
    return part_help(lst,len(lst),0,0,0,0,values_lst)

def part_help(lst,len_list,s1,s2,count1,count2, mem = None):
    if not lst: # if the list is empty
        if s1==tuple_part[0] and s2==tuple_part[1] and count1<=len_list and count2<=len_list:
            return True
        return False
    if mem == None: # if we didn't get the memo as input
        mem = {}
        
    key = (len(lst), s1, s2)
    if key not in mem:
        give_Liora = part_help(lst[1:],len_list,s1+lst[0],s2,count1 + 1,count2,tuple_part,mem)
        give_Yosi = part_help(lst[1:],len_list,s1,s2+lst[0],count1,count2 + 1,tuple_part,mem)
        mem[key] = give_Liora or give_Yosi # either ways works - we only need on partition
        
    return mem[key]



lst=[20,10,5]
values_lst=(10,5)
print(partition([10,5],(10,5)))