import ssl
from geopy.geocoders import Nominatim
import time
start = time.time()

PERIOD_OF_TIME = 7
ssl._create_default_https_context = ssl._create_unverified_context
file = open("gps_locations.txt", "w")
geolocator = Nominatim(user_agent="geoapiExercises")
i=1
while True:
    location = geolocator.geocode("me")
    file.write("frame "+str(i) +" "+ str(location.latitude) + ", " + str(location.longitude) + "\n")
    i=i+1
    if time.time() > start + PERIOD_OF_TIME: break
    time.sleep(1)