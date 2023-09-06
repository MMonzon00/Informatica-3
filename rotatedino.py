import math
import os
# Get the directory where the script is located
script_dir = os.path.dirname(__file__)
# Define the relative path to your file
relative_path = 'dino.txt'
# Create the full path by joining the script directory and relative path
full_path = os.path.join(script_dir, relative_path)
# Load and parse the coordinates from your text file
with open(full_path, 'r') as file:
    lines = file.readlines()

original_coordinates = []
for line in lines:
    x, y = map(int, line.strip().split())
    original_coordinates.append((x, y))

# Rotate the coordinates by 180 degrees
rotated_coordinates = []
for x, y in original_coordinates:
    rotated_x = -x  # Rotate x-coordinate by 180 degrees
    rotated_y = -y  # Rotate y-coordinate by 180 degrees
    rotated_coordinates.append((rotated_x, rotated_y))

# Save the rotated coordinates to a new text file
with open('rotated_dino.txt', 'w') as output_file:
    for x, y in rotated_coordinates:
        output_file.write(f'{x} {y}\n')