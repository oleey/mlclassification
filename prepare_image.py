import os
import shutil
import cv2
import random

def is_image(file):
    """Checks if file is an image"""
    root, ext = os.path.splitext(file)
    if ext not in ['.jpg', '.jpe', '.jpeg', '.png']:
        return False
    return True

def resize_image(file, dest_folder, scale_percent):
    filename = file.split('/')[-1]
    img = cv2.imread(file, cv2.IMREAD_UNCHANGED)
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width,height)
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    folder = os.path.join(dest_folder,"%s.jpg"%filename)
    cv2.imwrite(folder, resized)
    print("Image %s resized"%file)
    

def process_folder(folder, dest_folder):
    """Processes the images in a folder"""
    for file in os.listdir(folder):
        if is_image(file):
            resize_image(os.path.join(folder,file),dest_folder,60)
           

if __name__=='__main__':
    source_folder = 'training_images'
    hotels = 'hotels'
    not_hotels = 'not-hotels'
    dest_folder = 'processed_training_images'
    if not os.path.exists(dest_folder):
        os.mkdir(dest_folder)
        os.mkdir(dest_folder+'/'+hotels)
        os.mkdir(dest_folder+'/'+not_hotels)
    subfolders = [hotels, not_hotels]
    for folder in subfolders:
        process_folder(source_folder+'/'+folder, dest_folder+'/'+folder)
