import numpy as np
import cv2
import os



def preprocess_image_computer(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Threshold the grayscale image to extract the text (assuming text is black)
    _, text_binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Remove the grid structure by thresholding based on color (assuming green grid)
    lower_green = np.array([40, 50, 40])  # Adjust these thresholds to match the green color in your image
    upper_green = np.array([100, 255, 100])
    mask = cv2.inRange(image, lower_green, upper_green)
    grid_binary = cv2.bitwise_not(mask)

    # Combine the text and grid binary images
    combined_binary = cv2.bitwise_and(text_binary, text_binary, mask=grid_binary)

    # Noise removal using median blur
    denoised_image = cv2.medianBlur(combined_binary, 5)

    # Further noise removal using morphological operations
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    
    # Apply morphological opening (erosion followed by dilation)
    opened_image = cv2.morphologyEx(denoised_image, cv2.MORPH_OPEN, kernel)
    
    # Apply morphological closing (dilation followed by erosion)
    final_image = cv2.morphologyEx(opened_image, cv2.MORPH_CLOSE, kernel)

    # Identify and remove small noise regions
    contours, _ = cv2.findContours(final_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    min_area = 100  # Adjust this threshold based on your image size and noise characteristics
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < min_area:
            cv2.drawContours(final_image, [contour], 0, (0, 0, 0), -1)  # Fill contour with black
    
    # Strengthen non-noise segments by slightly widening them
    final_image = cv2.dilate(final_image, kernel, iterations=1)
    
    return final_image





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

    # Identify and remove small noise regions
    contours, _ = cv2.findContours(final_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    min_area = 100  # Adjust this threshold based on your image size and noise characteristics
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < min_area:
            cv2.drawContours(final_image, [contour], 0, (0, 0, 0), -1)  # Fill contour with black
    
    # Strengthen non-noise segments by slightly widening them
    final_image = cv2.dilate(final_image, kernel, iterations=1)
    
    return final_image


# if the image being processed is pixelated
computer_image = False

file_path = "/Users/linjin/Downloads/test_img.jpg"

if computer_image:
    colored_img_array = cv2.imread(file_path)
    if colored_img_array is not None:
        img_array = preprocess_image_computer(colored_img_array)
else:
    img_array = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    if img_array is not None:
        img_array = preprocess_image(img_array)
cv2.imshow("Image", img_array)
cv2.waitKey(0)
cv2.destroyAllWindows()


# code for making csv 
# IMG_DIR = "/Users/linjin/Downloads/test_img.jpg"
# with open("ETL6_n.csv", "wb") as f:
    # for subdir in os.listdir(IMG_DIR):
        # subdir_path = os.path.join(IMG_DIR, subdir)
        # if os.path.isdir(subdir_path):
    # for file_name in os.listdir(subdir_path):
    # file_path = os.path.join(subdir_path, file_name)
    # file_path = "/Users/linjin/Downloads/test_img.jpg"
    # img_array = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    # if img_array is not None:
    #     img_array = preprocess_image(img_array)
        # img_array = img_array.flatten()
        # img_array = img_array.reshape(-1, 1).T
        # print(img_array)
        # np.savetxt(f, img_array, delimiter=",", fmt="%d", newline="\n")

        # img_array = img_array.reshape((63, 64))
        # cv2.imshow("Image", img_array)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
 
 