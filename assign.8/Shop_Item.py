# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 00:31:53 2018

@author: Lidor
"""

class Shop_Item:
    """Represents an item in shop.
    Attributes: id, name, price"""
    
    def __init__(self, item_id, item_name, unit_price):
        "Constructor for an item in shop"
        self.item_id=item_id
        self.item_name=item_name
        self.unit_price=unit_price
    
    def __repr__(self):
        "Returns a string the item"
        res='id: ' + str(self.item_id) + ', name: ' + str(self.item_name) + ', price: ' + str(self.unit_price) + ' nis'
        return res
        