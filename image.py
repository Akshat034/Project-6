
import cv2
import os


img = cv2.imread("38.jpg")
try:
    resize = cv2.resize(img, (700,415))
except cv2.error as e:
    print('Invalid frame!')
cv2.waitKey()


with open(os.path.join("project_files",'obj.names'), 'r') as f:
    classes = f.read().splitlines()


net = cv2.dnn.readNet(r"C:\Users\saksh\PycharmProjects\pythonProject\yolov3_training_2000.weights", r"C:\Users\saksh\PycharmProjects\pythonProject\yolov3_testing.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)
classIds, scores, boxes = model.detect(img, confThreshold=0.6, nmsThreshold=0.4)


for (classId, score, box) in zip(classIds, scores, boxes):
    cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),
                  color=(0, 255, 0), thickness=2)
 
cv2.imshow("pothole",img)
cv2.imwrite("result1"+".jpg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
