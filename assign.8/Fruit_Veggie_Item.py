# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 00:50:42 2018

@author: Lidor
"""

from Shop_Item import Shop_Item
from List_Item import List_Item

class Fruit_Veggie_Item(Shop_Item, List_Item):
    """Represents a fruit or a vegetable item.
    Attributes: farm name, type: fruit or vegetable, vitamins contained"""
    
    def __init__(self, farm_name, isFruit, vitamins, item_id, item_name, unit_price, qty, request=''):
        "Constructor for a fruit or vegetable item"
        Shop_Item.__init__(self, item_id, item_name, unit_price)
        List_Item.__init__(self, qty, request)
        self.farm_name=farm_name
        self.isFruit=isFruit
        self.vitamins=vitamins
    
    def number_vitamins(self):
        "Returns number of vitamins"
        return len(self.vitamins)
    
    def __repr__(self):
        "Returns a string, representing this item"
        res=Shop_Item.__repr__(self)
        res+='\n' + List_Item.__repr__(self)
        res+='\n' + 'farm: ' + self.farm_name + ', '
        if self.isFruit==True:
            res+='fruit'
        else:
            res+='vegetable'
        res+=', ' + str(len(self.vitamins)) + ' vitamins'
        return res
        