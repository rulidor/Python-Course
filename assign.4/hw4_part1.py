# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 21:26:31 2018

@author: Lidor
"""

def base_to_decimal(num_as_str, orig_base):
    "Receives base number and the representing string. Returns num in decimal"
    dict={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15} #keys for string values
    decimal_number=0
    n_digits=len(num_as_str)
    for i in range(n_digits):
        if num_as_str[i]!='0':
            decimal_number+=(orig_base**(n_digits-i-1))*dict[num_as_str[i]]
    return decimal_number

def int_to_base(decimal_number, dest_base):
    "Receives a decimally represented number. Returns num as string, in the dest. base"
    dict={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
    result=''
    while decimal_number != 0:
        digit=decimal_number%dest_base
        decimal_number=decimal_number//dest_base
        result=dict[digit] + result
    return result

def base_to_base(num_as_str, orig_base, dest_base):
    "Receives string represented by orig. base. Returns string represented by dest. base"
    dec_number=base_to_decimal(num_as_str, orig_base)
    return int_to_base(dec_number,dest_base)