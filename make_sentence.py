import numpy as np

# Define the number of image vectors to extract
num_words = 10

# Count the total number of lines in the CSV file
num_lines_total = sum(1 for _ in open("ETL1_n.csv"))

# Generate random line numbers to extract
random_lines = np.random.choice(num_lines_total, num_words, replace=False)

# Read the selected image vectors from the CSV file using numpy
selected_data = np.genfromtxt(
    "ETL1_n.csv",
    delimiter=",",
    skip_header=random_lines[0],
    max_rows=num_words,
)

original_shape = (63, 64)  ## got this by printing in pre-processing
reshaped_images = selected_data.reshape(-1, *original_shape)
# print(reshaped_images.shape)
sentence_image = np.hstack(reshaped_images)
# print(sentence_image.shape)
