# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 01:39:01 2018

@author: Lidor
"""

from Shop_Item import Shop_Item
from List_Item import List_Item

class Frozen_Item(Shop_Item, List_Item):
    """Represents a frozen item.
    Attributes: max. temp., exp. date"""
    
    def __init__(self, max_temp, exp_date, item_id, item_name, unit_price, qty, request=''):
        "Constructor for a frozen item"
        Shop_Item.__init__(self, item_id, item_name, unit_price)
        List_Item.__init__(self, qty, request)
        self.max_temp=max_temp
        self.exp_date=exp_date