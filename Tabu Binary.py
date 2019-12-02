# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:55:43 2019

@author: Rhett
"""

from Tabu import Tabu
import numexpr as ne

class TabuB(Tabu):
    
    def __init__(self, sequence, equation):
        super().__init__(sequence)
        
        # Data
        self.equation = equation
    
    
    def seq2int(self, seq):
        """
        Turns a sequence into a base 10 integer.
        """
        return int(''.join(map(str, seq)), 2)
    
    
    def calc(self, seq):   
        """
        finds cost of a sequence
        """
        x = self.seq2int(seq)
        return float(ne.evaluate(self.equation))
    
    
    def seq2str(self, seq):
        """
        Sequence to String
        """
        return "".join(map(str, seq))
        
    
    def sol2str(self, sol):
        """
        Solution to String
        """
        return ", ".join([self.seq2str(x) for x in sol])
    
    
    def status(self):
        """
        Status of Tabu Binary Search
        """
        b2 = self.sol2str(self.solution)
        b10 = [self.seq2int(x) for x in self.solution]
        b10 = ", ".join(map(str, b10))
        print("Cost: {0}, Solution: {1} (b2) or {2} (b10)".format(round(self.cost, 4), b2, b10))
    
    
    def movegen(self):
        """
        Identifies all possible swaps and associated sequences not in tabu or current solutions.
        """
        seqs = []
        swaps = []
        ind = []
        for i, x in enumerate(self.cseq):
            
            if i == self.oi:
                continue
            
            seq = self.cseq[:]
            seq[i] = 0 if x == 1 else 1
            swap = i
            
            # check if tabu
            if swap not in self.tabu:
                swaps.append(swap), seqs.append(seq), ind.append(i)
        
        return seqs, swaps, ind
    
# Test Data
"""
eq = "x ** 3 - 60 * x ** 2 + 900 * x" 
ss = [1, 0, 0, 0, 1]
t = TabuB(eq, ss)
t.cost
t.optimize(50, 2, max)
"""

print("### Problem 2. ###")
# Equation
eq = "x ** 2 - 30 * x * cos(50 * x) + 20 * x * sin(70 * x)"
# Starting Solution
ss = [0, 0, 0, 1, 1]  
# Run Model
t = TabuB(ss, eq)
t.cost
t.optimize(50, 2, min)
