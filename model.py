import cv2
from cv2 import dnn_superres
import glob
import os
import time

count = 0

for file in os.listdir(r'/Users/mac/PycharmProjects/pythonProject7/data'):
    if(file.endswith('jpg')):
        print(file)
        count += 1

print('Total:', count)
path = "/Users/mac/PycharmProjects/pythonProject7/data/*.jpg"

img_number = 1

while(img_number<=count):
    file_list = glob.glob(path)
    file_list.sort(key=os.path.getmtime)  # sort files by modification time
    for file in file_list:
        print(file)
        sr = dnn_superres.DnnSuperResImpl_create()
        img = cv2.imread(file)
        path = "FSRCNN_x2.pb"
        sr.readModel(path)

        sr.setModel("fsrcnn", 2)

        result = sr.upsample(img)
        cv2.imwrite("/Users/mac/Desktop/PT/" + "frame "+ str(img_number) + ".jpg", result)
        img_number += 1

os.system('python read2.py')
