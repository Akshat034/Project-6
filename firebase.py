import os
import pyrebase

dir_path = r'/Users/mac/PycharmProjects/pythonProject8/final output'
count = 0

for file in os.listdir(dir_path):
    if file.endswith('.jpg'):
        print(file)
        count += 1

print('Total:', count)

img_number = 1
while img_number <= count:
    for file in os.listdir(dir_path):
        if file.endswith('.jpg'):
            if img_number > count:
                break
            print(file)
         
            path_local = os.path.join(dir_path, file)
            storage.child(path_on_cloud).put(path_local)
