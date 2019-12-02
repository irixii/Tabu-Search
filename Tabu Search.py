# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:39:02 2019

@author: Rhett
"""

from Tabu import Tabu
import numpy as np

class TabuS(Tabu):
    
    def __init__(self, data, sequence):
        super().__init__(sequence)
        
        # Data
        self.data = np.array(data)
        
    def calc(self, nseq):   
        """
        finds cost of a sequence
        """
        
        # Coverage Count
        cc = [0] * self.jobs
        for r, x in enumerate(nseq):
            if x == 1:
                for c, y in enumerate(self.data[r]):
                    if y <= 20:
                        cc[c] = 1
        # Coverage
        c = sum(cc)
        # Number of Stations
        ns = sum(nseq)
        cost = ns + (self.jobs - c) * self.jobs
        return cost
    
data = [[0, 10, 20, 30, 30, 20],
        [10, 0, 25, 35, 20, 10],
        [20, 25, 0, 15, 30, 20],
        [30, 35, 15, 0, 15, 25],
        [30, 20, 30, 15, 0, 14],
        [20, 10, 20, 25, 14, 0]]
sequence = [0, 0, 1, 0, 1, 0]

print("### Problem 7 ###")
t = TabuS(data, sequence)
#t.optimize(10, 2, min)