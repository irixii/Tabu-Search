# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 19:22:03 2019

@author: Rhett
"""

class Tabu:
    
    def __init__(self, sequence):
        
        # Data
        self.jobs = len(sequence)
        
        self.cseq = sequence
        self.solution = [sequence]
        
        self.tabu = []
        
        self.cost = 0
        
        # Optimal Index
        self.oi = None
        

    def optimize(self, nmoves = 50, tabul = 3, ostrat = min):
        """
        iterate through possible moves until an optimal solution is found or no more moves are available.
        """
        # Initialize Cost
        self.cost = self.calc(self.cseq)
        
        for x in range(nmoves):
            # Identify possible moves
            seqs, swaps, ind = list(self.movegen())
            
            # Quit if no available moves
            if len(seqs) == 0:
                break
            
            # Identify costs of each move
            scost = list(map(self.calc, seqs))
            
            # Find optimal Cost
            c = ostrat(scost)
            
            # Index of optimal
            oi = scost.index(c)
            
            # Find Optimal Cost Sequence
            optseq = seqs[oi]
            optswap = swaps[oi]
            
            # Update Solution if smaller
            if (c < self.cost and ostrat == min) or (c > self.cost and ostrat == max):
                self.solution = [optseq]
                self.cost = c
            # Add solution if equal
            elif c == self.cost and optseq not in self.solution:
                self.solution.append(optseq)
                
            self.oi = ind[oi]
            
            # Update Tabu with most optimal entity.
            self.tabu.insert(0, optswap)
            self.tabu = self.tabu[: tabul]
        
            # Update starting point
            self.cseq = optseq
            
        self.status()
        
        
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
        Status of Tabu Search
        """
        res = self.sol2str(self.solution)
        print("Cost: {0}, Solution: {1}".format(self.cost, res))
        
             
    def movegen(self):
        """
        Identifies all possible swaps and associated sequences not in tabu or current solutions.
        """
        swaps, seqs, ind = [], [], []
        
        for i in range(self.jobs - 1):
            
            # Skip old optimal index
            if i == self.oi:
                continue
            
            # Identify Swap Content
            r, f = self.cseq[i + 1], self.cseq[i]
            
            # Generate Swap
            swap = [f, r]
            
            # Create new sequence
            seq = self.cseq[:]
            seq[i + 1], seq[i] = f, r
            
            # check if tabu
            if swap not in self.tabu:
                swaps.append(swap), seqs.append(seq), ind.append(i)
        
        return seqs, swaps, ind
        
    def calc(self, seq):   
        """
        finds cost of a sequence
        """
        pass