import pygame
import sys
import random
import cmn_func as func

# Initialize Pygame
pygame.init()
RADIUS = 20
FONT = pygame.font.SysFont(None, 30)

# Node class
class Node:
    def __init__(self, value, x, y):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.x = x
        self.y = y

# Function to draw nodes
def draw_node(node, highlight=False, empty=False):
    pygame.draw.circle(func.screen, func.BLACK, (node.x, node.y), RADIUS)
    pygame.draw.circle(func.screen, func.YELLOW, (node.x, node.y), RADIUS - 2)
    font = pygame.font.Font(None, 36)
    text = font.render(str(node.value), True, func.BLACK)
    text_rect = text.get_rect(center=(node.x, node.y))
    func.screen.blit(text, text_rect)
    if highlight:
        pygame.draw.circle(func.screen, (255, 0, 0), (node.x, node.y), RADIUS + 5, 2)
    if empty:
        pygame.draw.circle(func.screen, func.WHITE, (node.x, node.y + 60), RADIUS - 2)
        text_empty = font.render(str(node.value), True, func.BLACK)
        text_empty_rect = text_empty.get_rect(center=(node.x, node.y + 60))
        func.screen.blit(text_empty, text_empty_rect)

# Function to draw the entire tree
def draw_tree(root, current_node, empty_nodes):
    if root:
        draw_node(root, root == current_node)
        if root.left:
            draw_edge(root, root.left)
            draw_tree(root.left, current_node, empty_nodes)
        if root.right:
            draw_edge(root, root.right)
            draw_tree(root.right, current_node, empty_nodes)
    for empty_node in empty_nodes:
        draw_node(empty_node, empty=True)

# Function to draw edges
def draw_edge(start, end):
    pygame.draw.line(func.screen,func.WHITE, (start.x, start.y + RADIUS), (end.x, end.y - RADIUS), 2)

# Function to generate a random binary tree
def generate_random_tree(depth, x, y, horizontal_spacing, nodes_left, nodes_right, parent=None):
    if depth == 0 or (nodes_left == 0 and nodes_right == 0):
        return None

    value = random.randint(1, 100)
    node = Node(value, x, y)
    node.parent = parent

    generate_left = nodes_left > 0
    generate_right = nodes_right > 0

    if generate_left:
        node.left = generate_random_tree(depth - 1, x - horizontal_spacing, y + 60, horizontal_spacing // 2, nodes_left - 1, nodes_right, parent=node)

    if generate_right:
        node.right = generate_random_tree(depth - 1, x + horizontal_spacing, y + 60, horizontal_spacing // 2, nodes_left, nodes_right - 1, parent=node)

    return node

# Function to check if the entered expression is correct
def check_answer(current_node, entered_expression):
    postfix_expression = postfix_traversal(current_node)
    return entered_expression.strip() == postfix_expression.strip()

# Function to draw input box and text
def draw_input_box():
    pygame.draw.rect(func.screen, func.YELLOW, (func.SCREEN_WIDTH // 2 - 200, func.SCREEN_HEIGHT - 150, 400, 40), 2)
    func.custom_text('Enter postfix expression:',func.SCREEN_WIDTH // 2, func.SCREEN_HEIGHT - 200,func.SMALL_SIZE)

# Function to draw text on func.screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    func.screen.blit(text_surface, text_rect)

# Function to generate and return a new random tree with constraints
def get_next_random_tree(total_nodes):
    total_nodes += random.randint(1, 5)  # Increment total nodes by a random number between 1 and 5
    if total_nodes <= 1:
        total_nodes += 1

    # Randomly distribute the total_nodes between left and right subtrees
    nodes_left = random.randint(1, total_nodes - 1)
    nodes_right = total_nodes - nodes_left

    return generate_random_tree(2, func.SCREEN_WIDTH // 2, 50, func.SCREEN_WIDTH // 4, nodes_left, nodes_right)


# Function to calculate postfix expression
def postfix_traversal(node):
    if node is None:
        return ""
    left = postfix_traversal(node.left)
    right = postfix_traversal(node.right)
    if left and right:
        return f"{left} {right} {node.value}"
    elif left:
        return f"{left} {node.value}"
    elif right:
        return f"{right} {node.value}"
    else:
        return str(node.value)


# Main game function
def main():
    screen = pygame.display.set_mode((func.SCREEN_WIDTH, func.SCREEN_HEIGHT))
    pygame.display.set_caption("Binary Tree Game")
    clock = pygame.time.Clock()

    global total_nodes
    total_nodes = 3

    running = True

    random_tree = get_next_random_tree(total_nodes)
    current_node = random_tree
    empty_nodes = []
    input_text = ""

    message = None
    blurred_screen = pygame.Surface((func.SCREEN_WIDTH, func.SCREEN_HEIGHT)) 
    overlay = pygame.Surface((func.SCREEN_WIDTH, func.SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 0))

    while running:
        func.screen.fill(func.BLACK)
        func.screen.blit(func.background_image, (0, 0))

        if message:
            background_snapshot = func.screen.copy()
            blurred_screen = pygame.transform.smoothscale(background_snapshot, (func.SCREEN_WIDTH // 10, func.SCREEN_HEIGHT // 10))
            blurred_screen = pygame.transform.smoothscale(blurred_screen, (func.SCREEN_WIDTH, func.SCREEN_HEIGHT))
            overlay = pygame.Surface((func.SCREEN_WIDTH, func.SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 150))
            func.screen.blit(overlay, (0, 0))
            func.screen.blit(blurred_screen, (0, 0))
            func.custom_text(message, func.SCREEN_WIDTH // 2, func.SCREEN_HEIGHT // 3, func.BIG_SIZE)
            func.custom_text("Press Enter to continue", func.SCREEN_WIDTH // 2, func.SCREEN_HEIGHT // 3 + 75, func.MEDIUM_SIZE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if message and event.key == pygame.K_RETURN:
                    message = None
                elif not message:
                    if event.key == pygame.K_RETURN:
                        if check_answer(current_node, input_text):
                            message = "Correct!"
                            total_nodes += 1
                            random_tree = get_next_random_tree(total_nodes)  # Generate a new tree
                            current_node = random_tree
                            input_text = ""  # Reset input text
                        else:
                            message = "Incorrect!"
                            print("Postfix Expression:", postfix_traversal(current_node).strip())
                            print("Entered Expression:", input_text.strip())
                            input_text = ""  # Reset input text
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

        draw_tree(random_tree, current_node, empty_nodes)
        draw_input_box()
        draw_text(input_text, FONT, func.WHITE, func.SCREEN_WIDTH // 2, func.SCREEN_HEIGHT - 125)        
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

