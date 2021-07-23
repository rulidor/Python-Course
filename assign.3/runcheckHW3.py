# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 17:42:47 2018

@author: Lidor
"""

import hw3
board=[[0,0,0,-1,5,0,0,0,0],
       [0,6,0,0,3,0,2,0,0],
       [0,2,9,4,0,0,0,7,8],
       [0,0,4,1,7,0,0,8,0],
       [0,0,6,3,0,5,9,0,0],
       [0,5,0,0,8,4,1,0,0],
       [7,1,0,0,0,8,5,6,0],
       [0,0,5,0,1,0,0,2,0],
       [0,0,0,0,9,0,0,1,3]]
print(hw3.is_valid_sudoku_board(board))
print(hw3.enter_digit(board,3,1,3))
print(board)

#list10=[1,2,3]
#
#print(type(list10) is list)
#print(type(list10) == list)
#print(type(list10) is 'list')
#print(type(list10) == 'list')
#print(type(list10))