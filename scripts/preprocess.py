import numpy as np
import cv2
import os


def preprocess_image(image):
    # Correct nonuniform illumination of the background
    se = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
    bg = cv2.morphologyEx(image, cv2.MORPH_DILATE, se)
    corrected_image = cv2.divide(image, bg, scale=255)

    # Enhance contrast using CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    contrast_enhanced_image = clahe.apply(corrected_image)

    # Binarization
    _, binary_image = cv2.threshold(contrast_enhanced_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Noise removal using median blur
    denoised_image = cv2.medianBlur(binary_image, 5)

    # Further noise removal using morphological operations
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    
    # Apply morphological opening (erosion followed by dilation)
    opened_image = cv2.morphologyEx(denoised_image, cv2.MORPH_OPEN, kernel)
    
    # Apply morphological closing (dilation followed by erosion)
    final_image = cv2.morphologyEx(opened_image, cv2.MORPH_CLOSE, kernel)

    return final_image

# Example usage
# image = cv2.imread('path_to_your_image', cv2.IMREAD_GRAYSCALE)
# processed_image = preprocess_image(image)
# cv2.imshow('Processed Image', processed_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



IMG_DIR = "/Users/linjin/Downloads/test_img.jpg"
with open("ETL6_n.csv", "wb") as f:
    # for subdir in os.listdir(IMG_DIR):
        # subdir_path = os.path.join(IMG_DIR, subdir)
        # if os.path.isdir(subdir_path):
    # for file_name in os.listdir(subdir_path):
    # file_path = os.path.join(subdir_path, file_name)
    file_path = "/Users/linjin/Downloads/test_img.jpg"
    img_array = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    if img_array is not None:
        img_array = preprocess_image(img_array)
        # img_array = img_array.flatten()
        # img_array = img_array.reshape(-1, 1).T
        # print(img_array)
        # np.savetxt(f, img_array, delimiter=",", fmt="%d", newline="\n")

        # img_array = img_array.reshape((63, 64))
        cv2.imshow("Image", img_array)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
                    # break
            # break
