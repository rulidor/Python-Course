# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 17:37:31 2018

@author: Lidor
"""

def add_prefixes(prefix_dict, input_string):
    "Receives dict. and string. Adds to dict. the relevant prefixes and string"
    if is_already_entered(prefix_dict, input_string)==False: #checks if word already entered to the dict.
        prefix='' #prefixes for received string
        for c in input_string:
            prefix+=c
            if prefix_dict.get(prefix, 'Not found99')=='Not found99': #prefix is not in the dict.
                prefix_dict[prefix]=[input_string] #add key and string to dict.
            else: #prefix was found in the dict.
                flag=False #indicates if the string is in the key. If so, will be True. Else- False
                for val in prefix_dict.get(prefix): #check if the input_string is inside the value list of the key of prefix
                    if val==input_string: #string is in the relevant key, than stop searching in the value list
                        flag=True
                        break
                if flag==False: #prefix is found as key in dict., but the string is not a value in its list
                    prefix_dict[prefix].append(input_string) 
                            

def is_already_entered(prefix_dict, input_string):
    "Returns True if received word already in the dict. Else, returns False"
    value_list=prefix_dict.values()
    for i in value_list:
        for j in i:
            if j==input_string:
                return True
    return False

def add_all_prefixes(prefix_dict, word_list):
    "Receives a dict. and list of words. Adds in dict. prefixes for every word"
    for w in word_list:
        add_prefixes(prefix_dict, w)

def init_from_url(webpage):
    "Receives an internet file. Returns a dict. with all prefixes to the received words"
    import urllib.request
    with urllib.request.urlopen(webpage) as url:
        text=str(url.read(), 'utf-8')
    word_list=text.split()
    prefix_dict={}
    add_all_prefixes(prefix_dict, word_list)
    return prefix_dict

def autocomplete(prefix_dict, prefix):
    "Receives a dict. and a prefix, returns list of suggestions of suffixes"
    if prefix_dict.get(prefix, 'Not found99')=='Not found99':
        empty_list=[]
        return empty_list
    return prefix_dict.get(prefix)
        