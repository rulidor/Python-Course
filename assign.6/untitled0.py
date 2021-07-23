# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 18:24:39 2018

@author: Lidor
"""

def partition(lst, values_lst):
    return part_help(lst,len(lst),values_lst[0],values_lst[1],0,0)

def part_help(lst,len_of_lst,s1,s2,count1,count2,res='',mem = None):
    if not lst: # if list is empty
        if s1==0 and s2==0 and count1<=len_of_lst-1 and count2<=len_of_lst-1:
            return True
        else:
            return False
    if mem == None: # if we didn't get the memo as input
        mem = {}
    key = (len(lst), s1, s2)
    if key not in mem:
        give_Liora = part_help(lst[1:],len_of_lst,s1-lst[0],s2,count1 + 1,count2,res+"Liora",mem)
        give_Yosi = part_help(lst[1:],len_of_lst,s1,s2-lst[0], count1, count2 + 1, res+"Yossi",mem)
        if give_Liora:
            mem[key] = ("Liora")
        elif give_Yosi:
            mem[key] = ("Yossi")
    return res+mem[key]

lst=[20,10,5]
values_lst=(10,5)
print(partition(lst,values_lst))