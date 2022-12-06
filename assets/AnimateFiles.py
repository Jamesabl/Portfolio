import urllib.request 
import time
import imageio
import os
import sys
import numpy as np



jpg_dir = "C:/Users/nadul/Desktop/Passport/Backup/Backup Files/Projects/Python Projects/Projects/Hurricane Photos/Surfline Temps"
images = []
for file_name in os.listdir(jpg_dir):
    if file_name.endswith('.png'):
        file_path = os.path.join(jpg_dir, file_name)
        images.append(imageio.imread(file_path))
        i = len(images)
print('Gathering Surfline...')
imageio.mimsave('C:/Users/nadul/Desktop/Passport/Backup/Backup Files/Projects/Python Projects/Projects/Hurricane Photos/FLSLWT.gif', images, 'GIF-FI', duration = .2)
print('Gathering Surfline... Complete!')
time.sleep(1)
