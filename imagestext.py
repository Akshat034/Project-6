import os
import pyrebase

dir_path = r'/Users/mac/Desktop/finaloutput'
count = 0

for file in os.listdir(dir_path):
    if file.endswith('.txt'):
        print(file)
        count += 1

print('Total:', count)

file_number = 1
while file_number <= count:
    for file in os.listdir(dir_path):
        if file.endswith('.txt'):
            if file_number > count:
                break
            print(file)
            file_number += 1
            path_local = os.path.join(dir_path, file)
            storage.child(path_on_cloud).put(path_local)
