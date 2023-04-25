import os
import pyrebase

dir_path = r'/Users/mac/Desktop/finaloutput'
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
            img_number += 1
            config = {
                "apiKey": "AIzaSyCwjlcY-J2hr4fWaq4QqRe_a4EvVxP0wUY",
                "authDomain": "pothole-fcc49.firebaseapp.com",
                "projectId": "pothole-fcc49",
                "storageBucket": "pothole-fcc49.appspot.com",
                "messagingSenderId": "1098414391097",
                "appId": "1:1098414391097:web:1ae28ebf65acbd84cdf2e8",
                "measurementId": "G-GQK07PBWF4",
                "serviceAccount": "serviceAccount.json",
                "databaseURL": " https://pothole-fcc49-default-rtdb.firebaseio.com/"
            }
            firebase = pyrebase.initialize_app(config)
            storage = firebase.storage()
            path_on_cloud = file
            path_local = os.path.join(dir_path, file)
            storage.child(path_on_cloud).put(path_local)



