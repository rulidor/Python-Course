# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:54:59 2018

@author: Lidor
"""

import hw4_part2

prefix_dict={}
hw4_part2.add_all_prefixes(prefix_dict, ['aba', 'abba', 'abbey', 'small'])
#print(prefix_dict)

#print(hw4_part2.autocomplete(prefix_dict, 'a'))
#print(hw4_part2.autocomplete(prefix_dict, 'small'))
#print(hw4_part2.autocomplete(prefix_dict, 'blabla'))



webpage='https://www.dropbox.com/s/0mpu0tag3wkzu2b/example1.txt?dl=1'
print(hw4_part2.init_from_url(webpage))
