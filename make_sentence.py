import numpy as np

# Define the number of lines to extract
num_lines = 10

# Count the total number of lines in the CSV file
num_lines_total = sum(1 for _ in open("ETL1_n.csv"))

# Generate random line numbers to extract
random_lines = np.random.choice(num_lines_total, num_lines, replace=False)

# Read the selected lines from the CSV file using numpy
selected_data = np.genfromtxt(
    "ETL1_n.csv",
    delimiter=",",
    skip_header=random_lines[0],
    max_rows=num_lines,
)

# Display the selected data
print(selected_data)
