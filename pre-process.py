import numpy as np
import cv2
import os

IMG_DIR = "/Users/linjin/Downloads/dataset/filtered/ETL6"

for subdir in os.listdir(IMG_DIR):
    subdir_path = os.path.join(IMG_DIR, subdir)
    if os.path.isdir(subdir_path):
        for file_name in os.listdir(subdir_path):
            file_path = os.path.join(subdir_path, file_name)
            img_array = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
            if img_array is not None:
                img_array = img_array.flatten()
                img_array = img_array.reshape(-1, 1).T
                print(img_array)
                with open("ETL6.csv", "ab") as f:
                    np.savetxt(f, img_array, delimiter=",")
