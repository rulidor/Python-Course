# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 21:05:16 2019

@author: Lidor
"""

class Queue:
    """Represents a queue, an abstract data type
    Attributes: list of elements"""
    
    def __init__(self):
        "Constructor for Queue"
        self.queue=[]
    
    def enqueue(self, val):
        "Inserts received val. to end of queue"
        self.queue.append(val)
    
    def dequeue(self):
        "Removes first element in queue and returns it"
        if len(self.queue)==0:
            raise IndexError('The queue is empty')
        value=self.queue[0]
        self.queue=self.queue[1:]
        return value
    
    def is_empty(self):
        "Returns True if queue is empty, else - returns False"
        if len(self.queue)==0:
            return True
        return False
    
    def front(self):
        "Returns first element in queue without removing it from queue"
        if len(self.queue)==0:
            raise IndexError('The queue is empty')        
        return self.queue[0]
    
    def rear(self):
        "Returns last element in queue, without removing it from queue"
        if len(self.queue)==0:
            raise IndexError('The queue is empty')   
        return self.queue[len(self.queue)-1]
    
    def __len__(self):
        "Returns this queue length"
        return len(self.queue)
    
    def __repr__(self):
        "Returns a string representing this queue"
        res='front <-- '
        for i in range(len(self.queue)-1):
            res+="'" + str(self.queue[i]) + "' | "
        res+="'" + str(self.queue[i+1]) + "' <-- rear"
        return res
    
    def __getitem__(self, loc):
        "Returns item in received loc."
        if not (0 <= loc < len(self.queue)):
            return
        return self.queue[loc]