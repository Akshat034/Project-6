import cv2
import glob
import os

dir_path = r'/Users/mac/Desktop/PT'
count = 0
files = []

for file in os.listdir(dir_path):
    if(file.endswith('jpg')):
        files.append(file)
        count += 1

print('Total:', count)

files.sort(key=lambda x: os.stat(os.path.join(dir_path, x)).st_ctime)

img_number = 1
for file in files:
    print(file)
    img = cv2.imread(os.path.join(dir_path, file))

    gaussian_blur = cv2.GaussianBlur(img, (7, 7), 2)
    sharpened3 = cv2.addWeighted(img, 7.5, gaussian_blur, -6.5, 0)

    cv2.imwrite(os.path.join('/Users/mac/Desktop/Fp', 'frame ' + str(img_number) + '.jpg'), sharpened3)
    img_number += 1

os.system('python tesing.py')