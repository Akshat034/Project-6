import pyrebase


config =


firebase = pyrebase.initialize_app(config)


storage = firebase.storage()


file_path = r"/Users/mac/PycharmProjects/pythonProject7/gps_locations.txt"


storage.child("gps_locations.txt").put(file_path)

print("File uploaded successfully!")
