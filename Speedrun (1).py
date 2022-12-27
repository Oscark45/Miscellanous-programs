# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 21:45:19 2022

@author: Oscar
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

plt.close('all')

M = 9
N = 1000
k = 50000

#users = np.array(["A", "B", "C", "D", "E", "F", "G", "H"])
users = np.array(["Ari", "Jaakki", "Tuukka", "Elias P", "Miika", "Olli", "Steissi", "Veemeli", "Unna"])
indices = np.arange(len(users))

for _ in range(5):
    np.random.shuffle(indices)
user_dir = dict(zip(indices, users))

steps = np.arange(N)+1
flucM = np.floor(np.log10(steps))+2

data = np.zeros((M, N))

#linI = 2
#expI = 3 
#polyI1 = 4


exp_step = np.random.randint(0,8)
Qc = np.random.randint(0,2)
for i, step in enumerate(steps):
    
    data[0][i] = step*k # Just linear
    data[1][i] = data[1][i-1] + k + np.random.randint(-1000, 1000)*flucM[i] if i > 0 else 0 # Linear fluc
    data[3][i] = data[3][i-1] + (400 + exp_step)*1.00675**step if i > 0 else 0 # Exponential
    data[2][i] = (data[0][i]+data[3][i])/2 # Doomed average 1
    data[4][i] = data[4][i-1] + (99 + Qc)*step + np.random.randint(-10, 10)*flucM[i] if i > 0 else 0 # Quadratic
    data[5][i] = (data[3][i]+data[4][i]+data[0][i])/3 # Doomed average 2
    data[6][i] = data[6][i-1] + 5*step**0.5*(470 + Qc) + np.random.randint(-10, 10)*flucM[i] if i > 0 else 0 # "Quasipoly"
    data[7][i] = (data[0][i]+data[2][i]+data[3][i]+data[4][i]+data[5][i]+data[6][i] + data[7][i])/7
    data[8][i] = (data[4][i] + data[3][i])/2

"""
for i in range(M):
    
    if i == expI:
        data[i] = (99+np.random.randint(0,6))*np.floor(1.001**step)+np.floor(1.2*step**1.9) + np.random.randint(-1000, 1001, N)
    elif i == polyI1:
        data[i] = np.floor((125 + np.random.randint(-1,3))*step**1.4)
    elif i == linI:
        data[i] = k*step
    else:
        rfluc = np.random.randint(-2000, 2000, N)*np.floor(np.exp(flucM)) if not linI == i else 0
        data[i] = k*step + rfluc
"""

finals = np.zeros(M)
for i in range(M):
    finals[i] = (data[i])[-1]


plt.figure()
plt.plot(data[0], label = "Linear")
plt.plot(data[1], label = "Linear Random")
plt.plot(data[2], label = "Doomed 1")
plt.plot(data[3], label = "Exponential")
plt.plot(data[4], label = "Quadratic")
plt.plot(data[5], label = "Doomed 2")
plt.plot(data[6], label = "Quasipoly")
plt.plot(data[7], label = "Doomed 3")
plt.plot(data[8], label = "Doomed 4")
plt.legend()
plt.show()

export = pd.DataFrame()
for i, user in enumerate(users):
    export[user_dir[i]] = (np.floor(data[i][:])*(data[i] >= 0)).astype(int)
    export[user_dir[i]] = export.apply(lambda x: "{:,}".format(x[user_dir[i]]), axis=1)

export.to_csv("speedrun.csv")

#plt.plot(data[2])