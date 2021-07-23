# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 01:18:36 2018

@author: Lidor
"""

from Shop_Item import Shop_Item
from List_Item import List_Item

class Meat_Item(Shop_Item, List_Item):
    """Represents a meat item.
    Attributes: butcher name, exp. date, weight in grams"""
    
    def __init__(self, butcher_name, exp_date, weight, item_id, item_name, unit_price, qty, request=''):
        "Constructor for a meat item"
        Shop_Item.__init__(self, item_id, item_name, unit_price)
        List_Item.__init__(self, qty, request)
        self.butcher_name=butcher_name
        self.exp_date=exp_date
        self.wight=weight
    
    def __repr__(self):
        "Returns a string, representing this item"
        res=Shop_Item.__repr__(self)
        res+='\n' + List_Item.__repr__(self)
        res+='\n' + 'butcher: ' + self.butcher_name + ', exp: ' + self.exp_date + ', ' + str(self.wight) + 'g'
        return res