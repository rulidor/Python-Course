# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 19:52:25 2018

@author: Lidor
"""

def sum_digits(num): #RECURSIVE-targil 14
    "Receives a num., returns sum of its digits"
    if num==0:
        return 0
    return (num%10)+sum_digits(num//10)

def pal_num(num): #RECURSIVE - targil 15
    "Receives a num, prints it as a palindrome"
    str_num=str(num)
    return pal_helper(num, num, (len(str_num)-1)*2, len(str_num))

def pal_helper(num,res,cur_pwr,min_pwr):
    if cur_pwr<min_pwr:
        return res
    res += ((num%10)*(10**cur_pwr))
    return pal_helper(num//10,res,cur_pwr-1,min_pwr)

def factorial(num): #RECURSIVE - targil 19
    if num==1:
        return 1
    return num * factorial(num-1)

def check_positive(num_list): #RECURSIVE - targil 22
    if len(num_list)==0:
        return True
    return num_list[0]>=0 and check_positive(num_list[1:])


def binary_search(num_list, num_to_search): #RECURSIVE - targil 27
    res=binary_search_helper(num_list, num_to_search, 0, len(num_list)-1)
    if res<0:
        print('Number was not found')
    else:
        print('Number was found, in index: ' + str(res))
    
def binary_search_helper(num_list, num_to_search, left, right):
        if left>right:
            return -1
        middle=(left+right)//2
        if num_list[middle]==num_to_search:
            return middle
        elif num_list[middle]>num_to_search:
            return binary_search_helper(num_list, num_to_search, left, middle-1)
        else:
            return binary_search_helper(num_list, num_to_search, middle+1, right)
        
    

print(factorial(10))