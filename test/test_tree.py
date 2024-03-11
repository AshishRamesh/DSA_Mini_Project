import pygame , sys , random
import cmn_func as func

# Initialize Pygame
pygame.init()
RADIUS = 20  # Adjust the radius to match the node size

# Pygame setup
pygame.display.set_caption("Random Binary Tree Visualization")

# Node class
class Node:
    def __init__(self, value, x, y):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None  # Add the parent attribute
        self.x = x
        self.y = y

# Function to draw nodes
def draw_node(node, highlight=False, empty=False):
    pygame.draw.circle(func.screen, func.BLACK, (node.x, node.y), RADIUS)  # Draw black background
    pygame.draw.circle(func.screen, func.YELLOW, (node.x, node.y), RADIUS - 2)  # Fill with white
    font = pygame.font.Font(None, 36)
    text = font.render(str(node.value), True, func.BLACK)  # Render text in black
    text_rect = text.get_rect(center=(node.x, node.y))
    func.screen.blit(text, text_rect)

    # Highlight the current node with a red outline
    if highlight:
        pygame.draw.circle(func.screen, (255, 0, 0), (node.x, node.y), RADIUS + 5, 2)

    # Draw an empty circle below the highlighted node
    if empty:
        pygame.draw.circle(func.screen, func.WHITE, (node.x, node.y + 60), RADIUS - 2)
        text_empty = font.render(str(node.value), True, func.BLACK)  # Render text in black
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
    pygame.draw.line(func.screen, func.WHITE, (start.x, start.y + RADIUS), (end.x, end.y - RADIUS), 2)

# Function to generate a random binary tree with a minimum of 3 nodes and a maximum of 20 nodes on both sides
def generate_random_tree(depth, x, y, horizontal_spacing, nodes_left, nodes_right, parent=None):
    if depth == 0 or (nodes_left == 0 and nodes_right == 0):
        return None  # Limit the depth and ensure a maximum of 20 nodes

    value = random.randint(1, 100)
    node = Node(value, x, y)
    node.parent = parent  # Set the parent attribute

    # Randomly determine whether to generate left and right children
    generate_left = nodes_left > 0
    generate_right = nodes_right > 0

    if generate_left:
        node.left = generate_random_tree(depth - 1, x - horizontal_spacing, y + 60, horizontal_spacing // 2, nodes_left - 1, nodes_right, parent=node)

    if generate_right:
        node.right = generate_random_tree(depth - 1, x + horizontal_spacing, y + 60, horizontal_spacing // 2, nodes_left, nodes_right - 1, parent=node)

    return node

# Function to generate and return a new random tree with constraints
def get_next_random_tree():
    global total_nodes
    # Increment the total number of nodes
    total_nodes += random.randint(1, 5)

    # Ensure the total number of nodes is greater than 1
    if total_nodes <= 1:
        total_nodes += 1

    # Calculate the number of nodes for each side, ensuring a minimum of 3 nodes on each side
    nodes_left = random.randint(3, min(total_nodes - 3, 20))
    nodes_right = total_nodes - nodes_left

    return generate_random_tree(5, func.SCREEN_WIDTH // 2, 50, func.SCREEN_WIDTH // 4, nodes_left, nodes_right)

# Function to calculate infix expression
def infix_traversal(node):
    if node is None:
        return ""
    return f"({infix_traversal(node.left)} {node.value} {infix_traversal(node.right)})"

# Function to calculate postfix expression
def postfix_traversal(node):
    if node is None:
        return ""
    return f"{postfix_traversal(node.left)} {postfix_traversal(node.right)} {node.value}"

# Function to calculate prefix expression
def prefix_traversal(node):
    if node is None:
        return []
    return [node] + prefix_traversal(node.left) + prefix_traversal(node.right)

# Function to draw expressions above the circles
def draw_expressions(root, prefix_nodes):
    infix_expression = infix_traversal(root)
    postfix_expression = postfix_traversal(root)

    font_expression = pygame.font.Font(None, 24)

    # Calculate the position to center the text above the circles
    x_position = func.SCREEN_WIDTH // 2
    y_position = func.SCREEN_HEIGHT - 50 - RADIUS - 30  # Adjust the y-coordinate for proper placement

    # Infix expression
    text_infix = font_expression.render(f"Infix: {infix_expression}", True, func.WHITE)
    text_infix_rect = text_infix.get_rect(center=(x_position, y_position - 20))
    func.screen.blit(text_infix, text_infix_rect)

    # Postfix expression
    text_postfix = font_expression.render(f"Postfix: {postfix_expression}", True, func.WHITE)
    text_postfix_rect = text_postfix.get_rect(center=(x_position, y_position))
    func.screen.blit(text_postfix, text_postfix_rect)

    # Prefix expression
    prefix_text = f"Prefix: {' '.join(map(str, [node.value for node in prefix_nodes]))}"
    text_prefix = font_expression.render(prefix_text, True, func.WHITE)
    text_prefix_rect = text_prefix.get_rect(center=(x_position, y_position + 20))
    func.screen.blit(text_prefix, text_prefix_rect)

# Function to draw enter button
# ... (previous code)

# Function to draw enter button
def draw_enter_button(x, y, is_active):
    button_width, button_height = 80, 30
    color = func.WHITE if is_active else (150, 150, 150)
    pygame.draw.rect(func.screen, color, (x - button_width // 2, y - button_height - 50, button_width, button_height))  # Rectangle for the button
    font_button = pygame.font.Font(None, 24)
    text_button = font_button.render("Enter", True, func.BLACK)
    text_button_rect = text_button.get_rect(center=(x, y - button_height / 2 - 50))
    func.screen.blit(text_button, text_button_rect)

# ... (rest of the code)

# Main loop
if __name__ == '__main__':
    total_nodes = 6  # Initial number of nodes
    random_tree = get_next_random_tree()
    current_node = random_tree  # Start with the root node
    empty_nodes = []  # Store the empty nodes below the highlighted nodes

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mx, my = pygame.mouse.get_pos()
                    # Check if the click is within the "Next" button
                    if func.SCREEN_WIDTH - 100 <= mx <= func.SCREEN_WIDTH - 20 and 10 <= my <= 40:
                        random_tree = get_next_random_tree()
                        current_node = random_tree
                        empty_nodes = []  # Reset the empty nodes when generating a new tree

            # Handle key events for node traversal and value transfer
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and current_node.left:
                    current_node = current_node.left
                    empty_nodes = []  # Reset the empty nodes when traversing to a new node
                elif event.key == pygame.K_RIGHT and current_node.right:
                    current_node = current_node.right
                    empty_nodes = []  # Reset the empty nodes when traversing to a new node
                elif event.key == pygame.K_UP and current_node.parent:
                    current_node = current_node.parent
                    empty_nodes = []  # Reset the empty nodes when traversing to a new node
                elif event.key == pygame.K_RETURN and current_node and not current_node.left and not current_node.right:
                    # If the highlighted node is a leaf node
                    empty_node = Node(current_node.value, current_node.x, current_node.y + 60)
                    empty_node.parent = current_node
                    empty_nodes.append(empty_node)

        func.screen.fill(func.BLACK)
        func.screen.blit(func.background_image, (0, 0))

        # Draw the tree
        draw_tree(random_tree, current_node, empty_nodes)

        # Draw infix, postfix, and prefix expressions above the circles
        draw_expressions(random_tree, prefix_traversal(random_tree))

        # Draw the "Enter" button above infix expression line (active only for leaf nodes)
        draw_enter_button(func.SCREEN_WIDTH // 2, func.SCREEN_HEIGHT - 50 - RADIUS - 30, is_active=(current_node and not current_node.left and not current_node.right))

        # Draw circles for each node in a single line below the expressions
        prefix_nodes = prefix_traversal(random_tree)
        for i, node in enumerate(prefix_nodes):
            draw_node(node)
            x_position = func.SCREEN_WIDTH // 2 - (len(prefix_nodes) * RADIUS) + i * (2 * RADIUS + 5)
            y_position = func.SCREEN_HEIGHT - 50
            pygame.draw.circle(func.screen, func.WHITE, (x_position, y_position), RADIUS - 2)  # Fill the circle with white

        # Draw the "Next" button
        pygame.draw.rect(func.screen, func.WHITE, (func.SCREEN_WIDTH - 100, 10, 80, 30))  # Rectangle for the button
        font_button = pygame.font.Font(None, 24)
        text_button = font_button.render("Next", True, func.BLACK)
        func.screen.blit(text_button, (func.SCREEN_WIDTH - 70, 15))

        pygame.display.flip()