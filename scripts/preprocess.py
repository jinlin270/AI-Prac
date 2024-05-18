import numpy as np
import cv2
import os


def preprocess_image(image):
    se = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))
    bg = cv2.morphologyEx(image, cv2.MORPH_DILATE, se)
    corrected_image = cv2.divide(image, bg, scale=255)

    # Enhance contrast using CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    contrast_enhanced_image = clahe.apply(corrected_image)

    # Binarization
    _, binary_image = cv2.threshold(contrast_enhanced_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Noise removal
    denoised_image = cv2.medianBlur(binary_image, 5)

    return denoised_image

    # Skew correction
    # coords = np.column_stack(np.where(denoised_image > 0))
    # angle = cv2.minAreaRect(coords)[-1]
    # if angle < -45:
    #     angle = -(90 + angle)
    # else:
    #     angle = -angle
    # (h, w) = image.shape[:2]
    # center = (w // 2, h // 2)
    # rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    # rotated_image = cv2.warpAffine(
    #     denoised_image,
    #     rotation_matrix,
    #     (w, h),
    #     flags=cv2.INTER_CUBIC,
    #     borderMode=cv2.BORDER_REPLICATE,
    # )

    return denoised_image


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
