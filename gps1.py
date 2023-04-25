from geopy.geocoders import Nominatim
import time
file = open("gps_locations.txt", "w")
geolocator = Nominatim(user_agent="geoapiExercises")
i=1
while True:
    location = geolocator.geocode("me")
    file.write("frame "+str(i) +" "+ str(location.latitude) + ", " + str(location.longitude) + "\n")
    i=i+1
    time.sleep(0) # wait for 5 seconds before getting the location again