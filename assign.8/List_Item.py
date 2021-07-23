# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 00:37:32 2018

@author: Lidor
"""

class List_Item:
    """Represents an item in shopping list.
    Attribures: quantity of units ordered, request"""
    
    def __init__(self, qty, request=''):
        "Constructor for an item in shopping list"
        self.qty=qty
        if len(request)==0:
            self.request=None
        else:
            self.request=request
    
    def get_request(self):
        "Returns request if exists, else - returns empty string"
        if self.request==None:
            return ''
        return self.request
    
    def update_quantity(self, new_qty):
        "Updates quantity of units ordered"
        self.qty=new_qty
    
    def __repr__(self):
        "Returns a string, representing quantity and request"
        res='qty: ' + str(self.qty) + ', request: '
        if self.request==None:
            res+='None'
        else:
            res+=self.request
        return res