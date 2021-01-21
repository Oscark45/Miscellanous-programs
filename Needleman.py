# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 22:28:53 2020

@author: Oscar
"""

import numpy as np

def score(l1, l2):
    
    if (l1 == 'C' and l2 == 'Y') or (l1 == 'T' and l2 == 'Y'):
        return 1
    elif l1 == l2 and l1 != '-':
        return 1
    elif (l1 == '-' and l2 != '-') or (l1 != '-' and l2 == '-'):
        return -1 
    elif l1 == '-' and l2 == '-':
        return -100
    elif l1 != l2:
        return -1

f1 = open("Needleman.txt", "w")

# Exericse 2 (2)
#s1 = "-ACTCTC"
#s2 = "-ACTTTGA"

# Exercise 3a (2)
#s1 = "-ACTCTCA"
#s2 = "-ACTGTG"

# Exercise 1 (3)
#s1 = "-ACCTAAGG"
#s2 = "-GGCTCAATCA"

# Exercise 2 (3)
s1 = "-ATGT"
s2 = "-YGYYYGATYGYAY"

n = len(s1)
m = len(s2)

M = np.zeros((len(s1), len(s2)), dtype = int)

M[0,0] = 0
for j in range(1,m): M[0,j] = -1*j*0
for i in range(1,n): M[i,0] = -1*i*0

for i in range(1,n):
    for j in range(1,m):
        print("M({},{})".format(i+1,j+1))
        f1.write("M({},{}):\n\n\n".format(i+1,j+1))
        
        score1 = M[i-1, j-1] + score(s1[i], s2[j])
        score2 = M[i-1, j]-2
        score3 = M[i, j-1]-2
        ma = max([score1, score2, score3, 0])
        f1.write("M({},{})".format(i-1+1, j-1+1) + " + " + "s({}{},{}{})".format(s1[i], i+1, s2[j], j+1) + " = "+str(score1)+" MAX"*(score1==ma))
        f1.write("\n")
        f1.write("M({},{})".format(i-1+1, j+1) + " + " + "s({}{},-)".format(s1[i], i+1) + " = "+str(score2)+" MAX"*(score2==ma))
        f1.write("\n")
        f1.write("M({},{})".format(i+1, j-1+1) + " + " + "s(-,{}{})".format(s2[j], j+1) + " = "+str(score3)+" MAX"*(score3==ma))
        f1.write("\n")
        f1.write("0 "+'MAX'*(0 == ma)+"'\'")

        f1.write("\n\n")

        print("M({},{})".format(i-1+1, j-1+1) + " + " + "s({},{})".format(s1[i-1],s2[j-1]) + " = "+str(score1)+" MAX"*(score1==ma))
        print("M({},{})".format(i-1+1, j+1) + " + " + "s({},-)".format(s1[i-1]) + " = "+str(score2)+" MAX"*(score2==ma))
        print("M({},{})".format(i+1, j-1+1) + " + " + "s(-,{})".format(s2[j-1]) + " = "+str(score3)+" MAX"*(score3==ma))
        print("0 " + 'MAX'*(0 == ma))
        M[i,j] = ma
        print()
          
print(M)
f1.close()

        
        
        
        
        
        
