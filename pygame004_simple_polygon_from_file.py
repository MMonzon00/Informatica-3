# Example of a simple polygon from a list of points from a file
import pygame
import os

gradient_colors = {
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
    "Magenta": (255, 0, 255),
    "Cyan": (0, 255, 255),
    "Maroon": (128, 0, 0),
    "GreenMid": (0, 128, 0),
    "Navy": (0, 0, 128),
    "Gray": (128, 128, 128)
}


#from pygame003_intersect import is_inside_polygon
#import pygame003_intersect
def is_inside_polygon(points: list, p: tuple) -> bool:
    cn = 0    # the crossing number counter

    # repeat the first vertex at the end
    points = tuple(points[:])+(points[0],)
   ## print("para mirar",points)

    # loop through all edges of the polygon
    for i in range(len(points)-1):   # edge from V[i] to V[i+1]
        if ((points[i][1] <= p[1] and points[i+1][1] > p[1])   # an upward crossing
                or (points[i][1] > p[1] and points[i+1][1] <= p[1])):  # a downward crossing
            # compute the actual edge-ray intersect x-coordinate
            # Since they are straight lines, proportions of x and y (slope) are taken, and it is checked that they are in range
            vt = (p[1] - points[i][1]) / float(points[i+1][1] - points[i][1])
            if p[0] < points[i][0] + vt * (points[i+1][0] - points[i][0]):  # P[0] < intersect
                cn += 1  # a valid crossing of y=P[1] right of P[0]

    return cn % 2   # 0 if even (out), and 1 if odd (in)

def read_points(file_path):
    # Takes the file and creates a list of points.
    points = []
    data = open(file_path)
    try:
        for line in data:
            x, y = line.split(',')
            points.append((int(x), int(y)))
    except:
        print(f'Error opening the file {file_path}')
    finally:
        data.close()
    return points

def polygon(canvas, point_list, color):
    points = point_list
    p1 = points[0]
    line = 0
    for p2 in points[1:]:
        print(f'Line={line} p1={p1} p2={p2}')
        pygame.draw.aaline(canvas, (0, 0, 0), p1, p2)
        p1 = p2
        line += 1

def get_dino_points(point_list):
    # Calculate the bounding box of the polygon
    max_x = max(point_list, key=lambda x: x[0])[0]
    min_x = min(point_list, key=lambda x: x[0])[0]
    max_y = max(point_list, key=lambda x: x[1])[1]
    min_y = min(point_list, key=lambda x: x[1])[1]

    # Iterate through points and select those within or intersecting with the bounding box
    selected_points = [(x, y) for x in range(min_x, max_x + 1) for y in range(min_y, max_y + 1)]

    # Calculate the number of selected points
    num_points = len(selected_points)

    # Initialize the color index and step size for color transition
    color_index = 0
    color_step = 5  # Increase this value to make colors change faster

    # Iterate through the selected points and draw them with a gradient between red and blue
    for p in selected_points:
        if is_inside_polygon(point_list, p):
            # Calculate the gradient color between red and blue based on the index
            r = max(0, min(255, int(255 - (255 * color_index / num_points))))  # Ensure within [0, 255] range
            g = 0  # Green component (zero for pure red)
            b = max(0, min(255, int(255 * color_index / num_points)))  # Ensure within [0, 255] range

            # Convert RGB values to integers
            gradient_color = (r, g, b)

            pygame.draw.aaline(canvas, gradient_color, p, p)

            # Increment the color index
            color_index += color_step
    
    pygame.display.update()
    


def get_dino_points_inf(point_list):
    # Calculate the bounding box of the polygon
    max_x = max(point_list, key=lambda x: x[0])[0]
    min_x = min(point_list, key=lambda x: x[0])[0]
    max_y = max(point_list, key=lambda x: x[1])[1]
    min_y = min(point_list, key=lambda x: x[1])[1]

    # Iterate through points and select those within or intersecting with the bounding box
    selected_points = [(x, y) for x in range(min_x, max_x + 1) for y in range(min_y, max_y + 1)]

    # Calculate the number of selected points
    num_points = len(selected_points)

    # Initialize the color index and step size for color transition
    color_index = 0
    color_step = 2  # Change this value to control the speed of the color transition

    # Main loop for animation
    while True:
        canvas.fill(color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Iterate through the selected points and draw them with a gradient
        for i, p in enumerate(selected_points):
            if is_inside_polygon(point_list, p):
                # Calculate the gradient color based on the current color index
                r, g, b = gradient_colors[color_index]
                pygame.draw.aaline(canvas, (r, g, b), p, p)

            # Increment the color index with wrap-around
            color_index = (color_index + color_step) % len(gradient_colors)
            pygame.draw.rect(canvas, rect_color, pygame.Rect(30, 30, 60, 60))
            pygame.display.update()
        
    


# def draw_inside_dino(point_list):
#     pygame.draw.aaline(canvas, (200, 200, 255), (200,300), (400,300))
#     # Create a list of points from 200,300 to 400,300 with increment 1
#     line_points = get_dino_points(read_points(file='./pygame/dino.txt'))


# Driver code
if __name__ == '__main__':
    pygame.init()
    # Get the directory where the script is located
    script_dir = os.path.dirname(__file__)
    # Define the relative path to your file
    relative_path = 'dino.txt'
    # Create the full path by joining the script directory and relative path
    full_path = os.path.join(script_dir, relative_path)
    # Now, full_path contains the absolute path to your file based on the script's location

    color = (20, 20, 20)
    rect_color = (255, 100, 0)

    # CREATING CANVAS
    canvas = pygame.display.set_mode((1920, 1080))

    # TITLE OF CANVAS
    pygame.display.set_caption("UCCG Polygon from Files")

    exit = False

    while not exit:
        canvas.fill(color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
        polygon(canvas, read_points(full_path), rect_color)
        get_dino_points(read_points(full_path))
        #get_dino_points_inf(read_points(full_path))


# Quit Pygame
pygame.quit()  

