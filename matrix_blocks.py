# -*- coding: utf-8 -*-
"""
Created on Thu May 12 21:38:48 2022

@author: Oscar
"""
import numpy as np


block = 8

ny = 100
size = 7

parts_f = (ny-2)//block

r =  np.random.randint(1,10, ny)
c = np.zeros(ny)
d = np.zeros(ny)

idx1 = 0
for i in range(ny):
    idx1 += 1
    c[i] = r[i]
    

idx2 = 0
for vb in range(parts_f):
    for j in range(block):
        
        idx2 += 1
        i = j + vb*block
        d[i] = r[i]
    
for v_left in range(ny-parts_f*block):
    
    idx2 += 1
    i = parts_f*block + v_left
    d[i] = r[i]
    
#print(idx1)
#print(idx2)

def idx_cmp(ny, size, block):
    
    parts_f = (ny-2)//block

    idx1 = 0
    for i in range(ny):
        idx1 += 1
        
    
    idx2 = 0
    for vb in range(parts_f):
        for j in range(block):
            idx2 += 1
        
    for v_left in range(ny-parts_f*block):
        idx2 += 1
        
    return idx1, idx2
        
a = np.zeros(100)
b = np.zeros(100)

for i in range(100):
    id1, id2 = idx_cmp(2+i, size, block)
    a[i] = id1
    b[i] = id2

print(((a-b) == 0).all())
print(((c-d) == 0).all())

def roundup(a,b):
    return (a+b-1)//b*b

n = 1000
ia = 1
ja = 1
ic = 1
jc = 1
for ks in np.arange(0, n, 4):
    ija = ja*8+ia    
    i = ic*64+ija
    j = jc*64+ija
    #print("ija, i and j: {} {} {}".format(ija, i, j))
    for f in range(4):
        k = ks + f
        
        
ny =0
A = np.arange(1,21)
B = np.zeros(20)

for j in range(4):
    for i in range(5):
        B[j+i*4] = A[i+j*5]
        
