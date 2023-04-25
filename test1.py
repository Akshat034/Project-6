import cv2
import time
import os

start = time.time()
cam = cv2.VideoCapture("/Users/mac/PycharmProjects/pythonProject7/output1.mp4")

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print('Error: Creating directory of data')

currentframe = 0
frame_interval = 2  # read every other frame
prev_time = time.time()

while True:
    ret, frame = cam.read()
    if ret:
        # check if enough time has elapsed
        curr_time = time.time()
        elapsed_time = curr_time - prev_time
        if elapsed_time > 1/20:  # 30 frames per second
            prev_time = curr_time
            name = './data/frame' + str(currentframe) + '.jpg'
            print('Creating...' + name)
            cv2.imwrite(name, frame)
            currentframe += 1
        else:
            continue
    else:
        break

end = time.time()
print("Time consumed in working: ", end - start)

cam.release()
cv2.destroyAllWindows()