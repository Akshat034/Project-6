import pyrebase


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


file_path = r"/Users/mac/PycharmProjects/pythonProject7/gps_locations.txt"


storage.child("gps_locations.txt").put(file_path)

print("File uploaded successfully!")