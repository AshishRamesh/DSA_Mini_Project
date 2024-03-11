import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RADIUS = 20

# Pygame setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Binary Tree Visualization")

# Node class
class Node:
    def _init_(self, value, x, y):
        self.value = value
        self.left = None
        self.right = None
        self.x = x
        self.y = y

# Function to draw nodes
def draw_node(node):
    pygame.draw.circle(screen, WHITE, (node.x, node.y), RADIUS)
    font = pygame.font.Font(None, 36)
    text = font.render(str(node.value), True, BLACK)
    screen.blit(text, (node.x - 10, node.y - 10))

# Function to draw the entire tree
def draw_tree(root):
    if root:
        draw_node(root)
        if root.left:
            draw_edge(root, root.left)
            draw_tree(root.left)
        if root.right:
            draw_edge(root, root.right)
            draw_tree(root.right)

def draw_edge(start, end):
    pygame.draw.line(screen, WHITE, (start.x, start.y + RADIUS), (end.x, end.y - RADIUS), 2)

# Function to generate a random binary tree with a minimum of 3 nodes and a maximum of 20 nodes on both sides
def generate_random_tree(height, x, y, horizontal_spacing, node_count):
    if height == 0 or node_count >= 20:
        return None  # Limit the depth and ensure a maximum of 20 nodes

    value = random.randint(1, 100)
    node = Node(value, x, y)
    generate_left = random.choice([True, False])
    generate_right = random.choice([True, False])

    if generate_left:
        node.left = generate_random_tree(height - 1, x - horizontal_spacing, y + 60, horizontal_spacing // 2, node_count + 1)

    if generate_right:
        node.right = generate_random_tree(height - 1, x + horizontal_spacing, y + 60, horizontal_spacing // 2, node_count + 1)

    return node

random_height_left = random.randint(2, 4)  # Random height for the left side
random_height_right = random.randint(2, 4)  # Random height for the right side

random_tree = Node(50, WIDTH // 2, 50)
random_tree.left = generate_random_tree(random_height_left, random_tree.x - WIDTH // 8, 110, WIDTH // 16, 1)
random_tree.right = generate_random_tree(random_height_right, random_tree.x + WIDTH // 8, 110, WIDTH // 16, 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    draw_tree(random_tree)
    pygame.display.flip()