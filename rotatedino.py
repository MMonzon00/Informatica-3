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
    x, y = map(int, line.strip().split(','))
    original_coordinates.append((x, y))

# Find the center of the bounding box
max_x = max(original_coordinates, key=lambda x: x[0])[0]
min_x = min(original_coordinates, key=lambda x: x[0])[0]
max_y = max(original_coordinates, key=lambda x: x[1])[1]
min_y = min(original_coordinates, key=lambda x: x[1])[1]
center_x = (max_x + min_x) // 2
center_y = (max_y + min_y) // 2

# Translate the coordinates so that the center becomes the origin
translated_coordinates = [(x - center_x, y - center_y) for x, y in original_coordinates]

# Rotate the translated coordinates by 180 degrees
rotated_coordinates = [(-x, -y) for x, y in translated_coordinates]

# Translate the rotated coordinates back to their original positions
final_coordinates = [(x + center_x, y + center_y) for x, y in rotated_coordinates]

# Save the final coordinates to a new text file
with open('rotated_dino.txt', 'w') as output_file:
    for x, y in final_coordinates:
        output_file.write(f'{x},{y}\n')
