import urllib.request 
import time
import imageio
import os
import sys
import numpy as np
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 

#Grabs the image from Surfline, draws on it with the date/time, and saves it in the folder
timestr = time.strftime("%Y-%m-%d_%H-%M")
print('\nGrabbing Surfline image')
urllib.request.urlretrieve("https://slcharts01.cdn-surfline.com/charts/florida/sofla/regionalsst/sofla_large_1_F.png", 'filepath/Surfline Temps/FLSLWT_'+ timestr + '.png')

print('Drawing on the details')
img = Image.open('filepath/Surfline Temps/FLSLWT_'+ timestr + '.png')
img = img.convert('RGB')
draw = ImageDraw.Draw(img)
#make sure to have arial.ttf font file in the same folder as this file
font = ImageFont.truetype('filepath/arial.ttf', 24)
draw.text((0, 0),timestr,(255,255,255),font=font)
img.save('filepath/Surfline Temps/FLSLWT_'+ timestr + '.png')
print('File Saved!')



#animates the images in the folder to a gif
jpg_dir = "filepath/Surfline Temps"
images = []
for file_name in os.listdir(jpg_dir):
    if file_name.endswith('.png'):
        file_path = os.path.join(jpg_dir, file_name)
        images.append(imageio.imread(file_path))
        i = len(images)
print('\nPreparing Surfline GIF...')
imageio.mimsave('C:/Users/nadul/Desktop/Passport/Backup/Backup Files/Projects/Python Projects/Projects/Hurricane Photos/FLSLWT.gif', images, 'GIF-FI', duration = .2)
print('Surfline GIF... Complete!')
time.sleep(1)
