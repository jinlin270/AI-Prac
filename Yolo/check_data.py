import cv2

# Read image
image = cv2.imread("/Users/linjin/Downloads/YOLO/Data/Training/images/1.jpg")

# Read YOLOv8 label file
with open("/Users/linjin/Downloads/YOLO/Data/Training/labels/1.txt", "r") as file:
    labels = file.readlines()

# Draw bounding boxes and class labels
for label in labels:
    # Extract bounding box coordinates and class label
    class_id, x_center, y_center, width, height = map(float, label.split())

    # Convert coordinates to integers
    x, y = int((x_center - width / 2) * image.shape[1]), int(
        (y_center - height / 2) * image.shape[0]
    )
    w, h = int(width * image.shape[1]), int(height * image.shape[0])

    # Draw bounding box
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Add class label
    cv2.putText(
        image,
        f"Class {int(class_id)}",
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (0, 255, 0),
        2,
    )

# Display or save visualization
cv2.imshow("YOLOv8 Visualization", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
