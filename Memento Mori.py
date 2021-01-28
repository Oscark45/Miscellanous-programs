# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 21:49:47 2021

@author: Oscar
"""
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

import datetime

then = datetime.datetime(2020, 5, 1, 0, 2, 13) 
now  = datetime.datetime(2021, 5, 1, 0, 0, 0)
length = 10

def UA_counter(time1, time2, length = 10):
    
    """
    Args:
        time1: countdown from
        time2: countdown to
        duration: length of countdown
    Returns:
        String formatted to days:hours:minutes:seconds
        
    """
    duration = time1 - time2  
    days = duration.days
    total_seconds = duration.total_seconds()
    days = duration.days
    hours = int((total_seconds - days*86400)//3600)
    minutes = int((total_seconds/60 - days*1440)%60)
    seconds = int(total_seconds%60)
    
    return '0'*(days < 10)+str(days)+':'+'0'*(hours < 10) + str(hours) \
        +':'+'0'*(minutes < 10) + str(minutes) \
        +':'+'0'*(seconds < 10) + str(seconds)
    

count = UA_counter(now, then)
print(count)

frames = []
for i in range(10):

    count = UA_counter(now, then + datetime.timedelta(seconds=i))    

    font = ImageFont.truetype("/usr/share/fonts/truetype/DejaVuSans.ttf",72)
    img=Image.new("RGBA", (800,400),(0,0,0))
    draw = ImageDraw.Draw(img)
    draw.text((160, 160),count,(256,256,256),font=font)
    #draw.chord((100, 75, 125, 100), 0, 360, fill='green')
    #draw.chord((75, 100, 100, 125), 0, 360, fill='blue')
    #draw.chord((125, 125, 150, 150), 0, 360, fill='yellow')
    draw = ImageDraw.Draw(img)
    frames.append(img)
    
# Save into a GIF file that loops forever
frames[0].save('moving_text.gif', format='GIF',
               append_images=frames[1:], save_all=True, duration=1000, loop=0)

img.save("test.png")