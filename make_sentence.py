import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

# Define the number of image vectors to extract
num_words = 10

# Count the total number of lines in the CSV file
num_lines_total = sum(1 for _ in open("images.csv"))
print(num_lines_total)

# Read the selected image vectors from the CSV file using numpy
images = pd.read_csv("images.csv", header=None).values

sentence = []

for i in range(num_words):
    rand = random.randint(0, num_lines_total - 1)
    row = images[rand].reshape(48, 48)[:, 9:39]
    sentence.append(row)
b = np.hstack(sentence)

# todo: output to a image
plt.imshow(b)
plt.show()
