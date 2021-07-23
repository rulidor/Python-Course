# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 22:15:11 2018

@author: Lidor
"""

from List_Item import List_Item
from Shop_Item import Shop_Item

class Shopping_List:
    """Represents a shopping list.
    Attributes: shopping list id, customer name, items, total price"""
    def __init__(self, sl_id, customer_name):
        "Constructor for shopping list"
        self.sl_id=sl_id
        self.customer_name=customer_name
        self.items=[]
        self.price_total=0
    
    def get_id(self):
        "Return this shopping list id"
        return self.sl_id
    
    def get_customer_name(self):
        "Return customer name for this shopping list"
        return self.customer_name
    
    def total_price(self):
        "Return total price of this shopping list"
        return self.price_total
    
    def __add__(self, item):
        "Adds item/s to shopping list"
        item_instance=List_Item(1, 'request')
        given_items_list=[]
        flag=False #to check if item exists in this item list
        if issubclass(type(item), type(item_instance)): #received 1 item
            given_items_list.append(item)
        else: #received multiple items
            given_items_list=item
        for i in given_items_list: #for given items
            for j in self.items: #for exist items
                if i.item_id==j.item_id:
                    j.qty+=i.qty
                    j.request=i.request
                    flag=True
            if flag==False:
                self.items.append(i)
            flag=False #initial flag for next iteration
            self.price_total+=i.qty*i.unit_price
    
    def item_summary(self):
        "Returns all products and quantities in shopping list"
        res_list=[]
        for i in self.items:
            t=(i.item_name,i.qty)
            res_list.append(t)
        return res_list
    
    def is_empty(self):
        "Returns True if shopping list is empty. Else - False"
        return len(self.items)==0
    
    def __gt__(self, other):
        "Returns True if this shopping list is greater than other. Else - False"
        if self.price_total>other.price_total:
            return True
        if self.price_total<other.price_total:
            return False
        #if total_price is equal:
        sum_self=0
        sum_other=0
        for i in self.items:
            sum_self+=i.qty
        for j in other.items:
            sum_other+=j.qty
        if sum_self>sum_other:
            return True
        if sum_self<sum_other:
            return False
        #if total_price and quantities are equal:
        if len(self.items)>len(other.items):
            return True
        else:
            return False
    
    def num_of_items_total(self):
        "Returns total number of items in shopping list"
        sum=0
        for i in self.items:
            sum+=i.qty
        return sum
    
    def __repr__(self):
        "Returns a string, representing shopping list"
        res='*' * 30 + '\n'
        res+='List id: ' + str(self.get_id()) + '\n'
        res+='Number of Products: ' + str(len(self.items)) + '\n'
        res+='Number of Items: ' + str(self.num_of_items_total()) + '\n'
        res+='Total Price: ' + str(self.price_total)
        res+='\n' + '*' * 30
        return res