# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 22:15:45 2021

@author: Oscar

There is a song I really like and there is one part that loops. 
However I started to notice that the clips sound slightly different but I 
wasn't sure if it just depended what I wanted to hear or my mood.

So I wrote this program to test that hypothesis by randomly playing 
one of the clips each time listening several times and writing the
sequence consisting of 1 or 2 depending which I hear.

My hypothesis is correct xD They really do sound different. My headphones
especially allow to hear it. Isn't coding fun :DDDD

The song is MrBeast (Trap Remix) Outro Song - ST6
https://www.youtube.com/watch?v=VuHl7QNtp6U
"""

from pygame import mixer  
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
