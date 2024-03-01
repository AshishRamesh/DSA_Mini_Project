import pygame
import math

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Define a function to draw a line with a custom width and neon effect
def draw_neon_line(screen, start_pos, end_pos, line_width=10, color=(255, 0, 255)):
    # Calculate the line length and direction
    dx, dy = end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]
    length = int(math.hypot(dx, dy))
    dx, dy = dx / length, dy / length

    # Create a gradient color list with fading alpha values
    gradient_colors = [(color[0], color[1], color[2], i) for i in range(255, 0, -1)]

    # Draw the gradient onto the line surface
    for i in range(length):
        pygame.draw.line(screen, gradient_colors[i % 255], 
                         (start_pos[0] + dx * i, start_pos[1] + dy * i), 
                         (start_pos[0] + dx * (i + 1), start_pos[1] + dy * (i + 1)), line_width)
# Sample line endpoints
line_points = [
    (50, 150), (300, 50),
    (70, 300), (400, 280),
    # Add more points for more lines
]

# Draw the lines with the neon effect
for start_point, end_point in line_points:
    draw_neon_line(screen, start_point, end_point, line_width=inner_line_width * 3, color=(255, 0, 255))

# Update the display
pygame.display.flip()

# Quit Pygame when the window is closed
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()
