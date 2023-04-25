import cv2
import os

# Set input and output directories
input_dir = r'/Users/mac/Desktop/Fp'
output_dir = r'/Users/mac/Desktop/finaloutput'

# Load model and classes
with open(os.path.join("project_files", 'obj.names'), 'r') as f:
    classes = f.read().splitlines()

net = cv2.dnn.readNet('project_files/yolov4_tiny.weights', 'project_files/yolov4_tiny.cfg')
model = cv2.dnn_DetectionModel(net)
model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)

# Create text file for storing image names
with open(os.path.join(output_dir, 'detected_images.txt'), 'w') as f:
    f.write('List of images where objects are detected:\n')

# Get list of image files in input directory sorted by modification time
files = [(os.path.join(input_dir, f), os.stat(os.path.join(input_dir, f)).st_mtime)
         for f in os.listdir(input_dir) if f.endswith('.jpg')]
files.sort(key=lambda x: x[1])

# Loop through input images and process them
for i, (file, _) in enumerate(files):
    print(f'Processing image {i+1} of {len(files)} ({file})')
    # Load input image
    img = cv2.imread(file)
    # Run object detection
    classIds, scores, boxes = model.detect(img, confThreshold=0.6, nmsThreshold=0.4)
    # Draw bounding boxes on image
    for (classId, score, box) in zip(classIds, scores, boxes):
        cv2.rectangle(img, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]),
                      color=(0, 255, 0), thickness=2)
    # Save output image if objects are detected
    if len(classIds) > 0:
        output_file = os.path.join(output_dir, f'frame {i+1}.jpg')
        cv2.imwrite(output_file, img)
        # Append image name to text file
        with open(os.path.join(output_dir, 'detected_images.txt'), 'a') as f:
            f.write(f'{os.path.basename(file)}\n')

os.system('python firebase1.py')
os.system('python imagestext.py')
