import os
from PIL import Image
from ultralytics import YOLO

# Load the trained model
model = YOLO("yolov8_weights.pt")


# Define the path to your test set folder containing images
test_folder = "/Users/linjin/Downloads/Yolo/Data/Test/images"

# Get a list of image files in the test set folder
image_files = [
    os.path.join(test_folder, file)
    for file in os.listdir(test_folder)
    if file.endswith(".jpg")
]

# Run inference on each image in the test set
for image_file in image_files:
    # Load the image
    image = Image.open(image_file)

    # Perform inference
    results = model.predict(image)

    # Print or process the detection results as needed
    print(results)
