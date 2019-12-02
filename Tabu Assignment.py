# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:23:47 2019

@author: Rhett
"""

from Tabu import Tabu
import numpy as np

class TabuA(Tabu):
    
    def __init__(self, data, sequence):
        super().__init__(sequence)
        
        # Data
        self.data = np.array(data)
        
    def calc(self, nseq):   
        """
        finds cost of a sequence
        """
        cost = 0
        for i, x in enumerate(nseq):
            cost += self.data[i, x - 1]
        return cost
    
data = [[14, 5, 8, 7], 
        [2, 12, 6, 5], 
        [7, 8, 3, 9], 
        [2, 4, 6, 10]]

print("### Problem 4. ###")
sequence = [4, 2, 1, 3]
t = TabuA(data, sequence)
t.optimize(50, ostrat = min)