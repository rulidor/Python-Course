# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 20:38:16 2018

@author: Lidor
"""

s="aaaabbc"
list=[] #compressed
count=1 #sequential charts counter
last_char=s[0]
print(len(s))
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        list.append([s[i],count])
        count=1
    last_char=s[i]
if s[i+1]==last_char:
    list.append([s[i],count])
else:
    list.append([s[i+1],1])
print(list)
        
"""for i in range(0,len(s)):
    if s[i]==s[i+1]:
        count+=1
    else:
        list.append([s[i],count])
print(list)
"""