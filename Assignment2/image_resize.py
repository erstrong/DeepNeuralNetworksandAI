from __future__ import print_function
import os, sys
from PIL import Image
import numpy as np
import pickle
import pandas as pd

# Resize images to 32x32
size = (32, 32)

directories = [x[0] for x in os.walk('tiny-imagenet-200/train/')]

counter = 0

for d in directories:
    for filename in os.listdir(d):
        if filename[-4:] == 'JPEG':
            name = d + '/' + filename
            new_name = 'data/' + filename
            img = Image.open( name )
            img.load()
            img = img.resize(size, Image.ANTIALIAS)
            img.save(new_name)
            counter +=1
            if counter % 100 == 0:
                print(str(counter) + ' images resized')

counter = 0

for filename in os.listdir('tiny-imagenet-200/val/images'):
    if filename[-4:] == 'JPEG':
        name = 'tiny-imagenet-200/val/images/' + filename
        new_name = 'val/' + filename
        img = Image.open( name )
        img.load()
        img = img.resize(size, Image.ANTIALIAS)
        img.save(new_name)
        counter +=1
        if counter % 100 == 0:
            print(str(counter) + ' validation images resized')

# Save images to pickle files

train_images = []
train_labels = []

counter = 0

for filename in os.listdir('data'):
    if filename[-4:] == 'JPEG':
        name = 'data/'+filename
        label = filename[0:9]
        img = Image.open( name )
        img.load()
        train_images.append(np.asarray(img)) 
        train_labels.append(label)
        counter += 1
        if counter % 1000 == 0:
            print(str(counter) + ' images converted')


pickle.dump(train_images, open( "~/imagenet-200/train_images.pkl", "wb" ) )
pickle.dump( Y, open( "~/imagenet-200/train_labels.pkl", "wb" ) )