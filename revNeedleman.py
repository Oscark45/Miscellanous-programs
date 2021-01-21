# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 20:11:39 2020

@author: Oscar
"""

import numpy as np
import queue as Q

s1 = "..AACGCGT"
s2 = "..AACGT"

def score(l1, l2):
    if l1 == l2:
        return 1
    else:
        return -1

M = np.array([[0,0,0,0,0,0,0],[0,0,-1,-2,-3,-4,-5], [0,-1, 1, 0, -1, -2, -3], [0,-2, 0, 2, 1, 0, -1],
              [0,-3, -1, 1, 3, 2, 1], [0,-4, -2, 0, 2, 4, 3], [0,-5, -3, -1, 1, 3, 3],
              [0,-6, -4, -2, 0, 2, 2], [0,-7, -5, -3, -1, 1, 3]])


q = Q.PriorityQueue()
q.put((M.shape[0]-1, M.shape[1]-1))
print((M.shape[0]-1, M.shape[1]-1))
paths = dict()
path = []


while not q.empty():
    k = 0
    (i,j) = q.get()

    if M[i-1,j-1] == M[i,j] - score(s1[i], s2[j]):
        q.put((i-1,j-1))
        print("YAY")
        continue
        
    if M[i,j-1] == M[i,j] + 1:
        print("LOL")
        continue
        
    if M[i-1,j] == M[i,j] + 1:
        print("HUHU")
        continue
        
    if k == 0:
        pass
    
       