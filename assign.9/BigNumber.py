# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 23:27:27 2019

@author: Lidor
"""

from QueueModule import Queue

class BigNumber(Queue):
    """Represents a number.
    Attributes: queue of chars, which are string type, representing the num"""
    
    def __init__(self, num):
        "Constructor for a BigNumber"
        if type(num)!=type(''):
            raise TypeError('BigNumber init expected str')
        if num.isdigit()==False: #if num received is a string, check whether num contains only digits
            raise TypeError('The number contains non digit characters')
        self.digits=Queue()
        for i in num:
            self.digits.enqueue(i)
    
    def __str__(self):
        "Returns num. as string"
        res=''
        for i in range(len(self.digits)):
            res+=self.digits[i]
        return res
    
    def __eq__(self, other):
        "Compares between two numbers and returns True if they are equal"
        if type(other)!=type(self):
            raise TypeError('Can only compare two BigNumbers')
        if len(self.digits)!=len(other.digits):
            return False
        for i in range(len(self.digits)):
            if int(self.digits[i])!=int(other.digits[i]):
                return False
        return True
    
    def __gt__(self, other):
        "Returns True if self is greater than other"
        if type(other)!=type(self):
            raise TypeError('Can only compare two BigNumbers')
        if len(other.digits)>len(self.digits):
            return False
        if len(self.digits)>len(other.digits):
            return True
        for i in range(len(self.digits)): #len is equal in both queues
            if int(other.digits[i]) >= int(self.digits[i]):
                return False
        return True
    
    def read_and_return_biggest(self, path):
        "Reads content of file, returns BigNumber object of max. num. between numbers in file and self"
        try:
            list1=[] #list of numbers from file
            f=open(path, 'r')
            list1=f.read().split('\n')
            max_num=BigNumber(self.__str__)
            for num in list1:
                cur_num=BigNumber(num)
                if cur_num.__gt__(max_num):
                    max_num=BigNumber(cur_num.__str__())
            f.close()
            return max_num
        except BaseException:
            print()
    
    def add_number_to_file(self, path):
        "Adds number to file"
        f=open(path, 'a')
        f.write('\n' + self.__str__())
        
        