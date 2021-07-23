# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 17:06:27 2018

@author: Lidor
"""

def is_valid_sudoku_board(board):
    "Checks if a board is valid and returns True or False accordingly"
    list=[1,2] #list to compare board's type
    if type(board)!=type(list): #checks if board's type is valid
        return False
    for r in board: #checks type validation for every row
        if type(r)!=type(list):
            return False
    if len(board)!=9: #checks number of rows in the board
        return False
    for r in board: #checks number of elements (or columns) in every row
        if len(r)!=9:
            return False
    for r in board: #checks type and value for every element in board
        for elem in r:
            if type(elem)!=int:
                return False
            if elem>9 or elem<0:
                return False
    return True

def is_valid_move(board, row, col, digit):
    "Checks if a move is valid and returns True or False accordingly"
    if is_valid_sudoku_board(board)==False: #cheks if board is valid
        return False
    if row<0 or row>8 or col<0 or col>8:
        return False
    if digit<=0 or digit>9:
        return False
    if board[row][col]!=0: #checks if the given index is empty
        return False
    if is_valid_for_row(board, row, digit)==False: #checks if valid for row
        return False
    if is_valid_for_col(board, col, digit)==False: #checks if valid for col
        return False
    if is_valid_for_block(board, row, col, digit)==False: #checks if valid for block
        return False
    return True


def is_valid_for_row(board, row, digit):
    "Checks if given row in board doesn't contain the digit"
    for elem in board[row]:
        if elem==digit:
            return False
    return True

def is_valid_for_col(board, col, digit):
    "Checks if given column in board doesn't contain the digit"
    for r in board:
        if r[col]==digit:
            return False
    return True
    
def is_valid_for_block(board, row, col, digit):
    "Checks if a block in board doesn't contain the digit"
    for i in range(3*int(row/3),(3*int(row/3)+3)): #iterator per row in block
        for j in range(3*int(col/3),(3*int(col/3)+3)): #iterator per col in block
            if board[i][j]==digit:
                return False
    return True

def enter_digit(board, row, col, digit):
    "Enters digit to board and returns True if move is valid."
    "Otherwise, returns False"
    if is_valid_move(board, row, col, digit)==True:
        board[row][col]=digit
        return True
    return False