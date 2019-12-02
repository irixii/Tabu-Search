# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:51:02 2019

@author: Rhett
"""
from Tabu import Tabu

class TabuT(Tabu):
    
    def __init__(self, w, p, d, sequence):
        super().__init__(sequence)
        
        # Weight
        self.w = w
        # Production Time
        self.p = p
        # Due Date
        self.d = d
        
    def calc(self, nseq):   
        """
        finds cost of a sequence
        """
        c = 0
        wt = 0
        for x in nseq:
            x -= 1
            c = self.p[x] + c
            ct = max(c - self.d[x], 0)
            wt += ct * self.w[x]
            
        return wt

p = [10, 10, 13, 4]
d = [4, 2, 1, 12]
w = [14, 12, 1, 12]
sequence = [2, 1, 4, 3]

print("### Problem 1. ###")
t = TabuT(w, p, d, sequence)
t.optimize(5, 2, min)