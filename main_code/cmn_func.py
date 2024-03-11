import pygame , os , sys
from pathlib import Path 

# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
NEON_PURPLE = (176, 38, 255)
BLUE = (0,0,255)
CYAN = (0,255,255)
RED = (255, 0, 0)
GOLD = (239, 229, 51)
# blue = (78,162,196) 
GREY = (170, 170, 170)
GREEN = (77, 206, 145)

BIG_SIZE = 100
MEDIUM_SIZE = 50
SMALL_SIZE = 40

global n_disks, game_done

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

def file_loc(filename):
    for root, _, files in os.walk('.'):
        if filename in files:
            return os.path.join(root, filename)
        
def draw_text(text, color, x, y,font):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

def custom_text(text,width,height,size):
    font_custom = pygame.font.Font(file_loc("VerminVibes1989Regular-m77m.ttf"), size)
    draw_text(text, CYAN, (width)+3, (height)+2,font_custom)
    draw_text(text, PURPLE, (width)+3, (height)+1,font_custom)
    draw_text(text, YELLOW, width, height,font_custom)

font_default =pygame.font.Font(None, SMALL_SIZE)
font_custom = pygame.font.Font(file_loc("VerminVibes1989Regular-m77m.ttf"), SMALL_SIZE)
background_image = pygame.image.load(file_loc('bg.png'))
background_main = pygame.image.load(file_loc('bg_main.png'))