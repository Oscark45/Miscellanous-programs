# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 22:15:45 2021

@author: Oscar
"""

from pygame import mixer  # Load the popular external library
import os
import numpy as np
import time

rand_seq = np.random.randint(1,3,15)
start = np.random.uniform(0,1, size=15) 

mixer.init()

for k, i in enumerate(rand_seq):
    
    mixer.music.load(os.getcwd()+'\\st6'+'{:}.mp3'.format(i))
    print('Song loaded: st6'+'{:}.mp3'.format(i))
    mixer.music.play(start=start[k])
    time.sleep(20)
    mixer.music.stop()
    
print(rand_seq)