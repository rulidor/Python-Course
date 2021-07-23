# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 00:20:21 2018

@author: Lidor
"""

def partition(lst, values_lst):
    "Receives assets list, returns list of name of heir for each asset"
    return part_help(lst,len(lst),values_lst[0],values_lst[1],0,0,[])

def part_help(lst,len_of_lst,s1,s2,count1,count2,res_list=[],mem = None):
    if not lst: # if the list is empty
        if s1==0 and s2==0 and count1<len_of_lst-1 and count2<len_of_lst-1:
            return res_list
        else:
            return []
    if mem == None: # if we didn't get the memo as input
        mem = {}
    key = (len(lst), s1, s2)
    if key not in mem:
        give_Liora = part_help(lst[1:],len_of_lst,s1-lst[0],s2,count1 + 1,count2,res_list+['Liora'],mem)
        give_Yosi = part_help(lst[1:],len_of_lst,s1,s2-lst[0], count1, count2 + 1, res_list+['Yossi'],mem)
        mem[key] = give_Liora or give_Yosi
    return mem[key]