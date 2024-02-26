import pygame
import sys
from pathlib import Path 
from hanoi import *

pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 40

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game Launcher")
clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font(None, FONT_SIZE)

def draw_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action

    def draw(self):
        pygame.draw.rect(screen, BLACK, self.rect)
        draw_text(self.text, WHITE, self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2)

# Splash Screen
splash_screen = True
while splash_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    draw_text("DSA Minigame", BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    pygame.display.flip()

    pygame.time.delay(2000)  # Display splash screen for 2 seconds
    splash_screen = False

# Start Screen
start_screen = True
while start_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start_screen = False

    screen.fill(WHITE)
    draw_text("DSA Minigame", BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
    draw_text("Press Enter to Start", BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    pygame.display.flip()
    clock.tick(FPS)

# Menu Screen
menu_screen = True
game_buttons = [
    Button(300, 170, 250, 50, "Tower Of Hanoi", action=lambda: exec(open(Path(__file__).parent / "hanoi.py").read())),
    Button(300, 270, 250, 50, "Game 2", action=lambda: print("Clicked Game 2")),
    Button(300, 370, 250, 50, "Game 3", action=lambda: print("Clicked Game 3"))
]
while menu_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in game_buttons:
                if button.rect.collidepoint(event.pos):
                    if button.action:
                        button.action()

    screen.fill(WHITE)
    draw_text("Game Menu", BLACK, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4)

    # Display game buttons
    for button in game_buttons:
        button.draw()

    pygame.display.flip()
    clock.tick(FPS)
