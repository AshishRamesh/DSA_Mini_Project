import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Obstacle types
OBSTACLE_TYPES = ["UP", "DOWN", "LEFT", "RIGHT"]

# Initialize Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Queue Runner Game")
clock = pygame.time.Clock()

# Font
font = pygame.font.Font(None, 36)

def display_text(text, x, y):
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Queue Runner class
class QueueRunner:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.obstacle_queue = self.generate_obstacle_queue()
        self.player_input = []

    def generate_obstacle_queue(self):
        return random.sample(OBSTACLE_TYPES * self.difficulty, self.difficulty)

# Main menu
def main_menu():
    selected_difficulty = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and selected_difficulty > 1:
                    selected_difficulty -= 1
                elif event.key == pygame.K_RIGHT and selected_difficulty < 10:
                    selected_difficulty += 1
                elif event.key == pygame.K_RETURN:
                    return selected_difficulty

        # Draw background
        screen.fill(WHITE)

        # Draw difficulty options
        display_text(f"Select Difficulty: {selected_difficulty}", WIDTH // 2, 100)
        
        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

# Game flow
while True:
    difficulty = main_menu()
    player = QueueRunner(difficulty)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.player_input.append("UP")
                elif event.key == pygame.K_DOWN:
                    player.player_input.append("DOWN")
                elif event.key == pygame.K_LEFT:
                    player.player_input.append("LEFT")
                elif event.key == pygame.K_RIGHT:
                    player.player_input.append("RIGHT")
                elif event.key == pygame.K_RETURN:
                    if player.player_input == player.obstacle_queue:
                        result = "You Win!"
                    else:
                        result = "You Lose!"

                    # Display result
                    while True:
                        for event_result in pygame.event.get():
                            if event_result.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                            if event_result.type == pygame.KEYDOWN and event_result.key == pygame.K_RETURN:
                                break

                        # Draw background
                        screen.fill(WHITE)

                        # Display result text
                        display_text(result, WIDTH // 2, HEIGHT // 2)
                        display_text("Press Enter to Play Again", WIDTH // 2, HEIGHT // 2 + 50)

                        # Update display
                        pygame.display.flip()

                        # Cap the frame rate
                        clock.tick(FPS)

                    break

        # Draw background
        screen.fill(WHITE)

        # Draw obstacles on the left side
        for i, obstacle in enumerate(player.obstacle_queue):
            text = font.render(obstacle, True, BLACK)
            screen.blit(text, (50, 100 + i * 40))

        # Draw player controls on the right side
        display_text("Controls", WIDTH - 100, 50)
        display_text("UP", WIDTH - 50, 100)
        display_text("DOWN", WIDTH - 50, 140)
        display_text("LEFT", WIDTH - 50, 180)
        display_text("RIGHT", WIDTH - 50, 220)

        # Draw player input
        display_text("Your Input", WIDTH - 100, 300)
        for i, key in enumerate(player.player_input):
            text = font.render(key, True, BLACK)
            screen.blit(text, (WIDTH - 50, 340 + i * 40))

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)
