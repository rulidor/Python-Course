# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 01:27:44 2018

@author: Lidor
"""

from Shop_Item import Shop_Item
from List_Item import List_Item

class Dry_Item(Shop_Item, List_Item):
    """Represents a dry item.
    Attributes: provider name, weight, calories, exp. date"""
    
    def __init__(self, provider_name, weight, num_calories, exp_date, item_id, item_name, unit_price, qty, request=''):
        "Constructor for a dry item"
        Shop_Item.__init__(self, item_id, item_name, unit_price)
        List_Item.__init__(self, qty, request)
        self.provider_name=provider_name
        self.weight=weight
        self.num_calories=num_calories
        self.exp_date=exp_date
    
    def calories_in_100g(self):
        "Returns number of calories per 100g"
        return 100/self.weight * self.num_calories