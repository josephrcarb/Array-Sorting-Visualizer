from random import randrange
import pygame
from algorithms.insertion_sort import insertion_sort
from algorithms.quick_sort import quick_sort

pygame.init()
pygame.display.set_caption("Array Sorting Visualizer Program")

# CONSTANTS
WIDTH = 700
HEIGHT = 500
ARR_WIDTH = 2
ARR_SIZE = 250
WIN_SIZE = (WIDTH, HEIGHT)
HOME_PNG_PATH = "resources/home.png"
FONT_TTF_PATH = "resources/AveraSansTcBld.ttf"
BG_PNG_PATH = "resources/bg.png"

# Define some colors
BLACK        = (   0,   0,   0)
WHITE        = ( 255, 255, 255)
GREEN        = (   0, 255,   0)
RED          = ( 255,   0,   0)
BLUE         = (   0,   0, 255)
LIGHT_BLUE   = ( 135, 206, 250)

class Sorting:
    def __init__(self):
        self.arr = []
        self.win_screen = 1
        self.screen = pygame.display.set_mode(WIN_SIZE)
        self.home_button = pygame.image.load(HOME_PNG_PATH).convert_alpha()
        self.home_button = pygame.transform.scale(self.home_button,(50,50))
        self.bg = pygame.image.load(BG_PNG_PATH).convert_alpha()
        self.bg = pygame.transform.scale(self.bg,(700,500))
        self.banner, self.banner_rect = self.text_objects("Sorting Visualizer")
        self.banner_rect.center = ((380), (75))
        self.sound = pygame.mixer.Sound("resources/beep.wav")

    def init_arr(self):
        self.arr = [randrange(500) for _ in range(ARR_SIZE)]

    def update(self, curr, name):
        self.screen.fill(WHITE)
        self.screen.blit(self.bg, (0,0))

        pygame.draw.rect(self.screen, LIGHT_BLUE, (160, 50, 440, 50))
        self.screen.blit(self.home_button, (50,50))
        self.banner, self.banner_rect = self.text_objects(name)
        self.banner_rect.center = ((380), (75))
        self.screen.blit(self.banner, self.banner_rect)

        for i in range(ARR_SIZE):
            x = (2 * i) + 100  # Calculate x position for rectangle
            height = (self.arr[i]) / 2  # Calculate height based on array value
            y = HEIGHT - height - 50   # Fixed y position for bottom of the screen
            rect = pygame.Rect(x, y, ARR_WIDTH, height)

            # Calculate color based on height in HSV color space
            hue = int((self.arr[i] / 500) * 360)  # Map height to hue (0 to 360)
            color = pygame.Color(0)  # Start with black
            color.hsva = (hue, 100, 100)

            if i == curr:
                self.play_sound(height)
                color = pygame.Color(0, 0, 0)
            pygame.draw.rect(self.screen, color, rect)  # Draw the rectangle
        pygame.display.flip()
    
    def draw_home(self):
        self.screen.fill(WHITE)
        self.screen.blit(self.bg,(0,0))

        pygame.draw.rect(self.screen, LIGHT_BLUE, (160, 50, 440, 50))
        self.screen.blit(self.home_button, (50, 50))
        pygame.draw.rect(self.screen, LIGHT_BLUE, (100, 125, 125, 50))
        pygame.draw.rect(self.screen, LIGHT_BLUE, (240, 125, 125, 50))

        self.banner, self.banner_rect = self.text_objects("Sorting Visualizer")
        self.banner_rect.center = ((380), (75))

        insert_surface, insert_rect = self.text_objects("Insertion Sort")
        insert_rect.center = ((160), (150)) 

        quick_surface, quick_rect = self.text_objects("Quick Sort")
        quick_rect.center = ((300), (150))

        self.screen.blit(insert_surface, insert_rect)
        self.screen.blit(quick_surface, quick_rect)
        self.screen.blit(self.banner, self.banner_rect)
        pygame.display.flip()

    def play_sound(self, height):
        self.sound.set_volume(height / 1000)  # Adjust volume if needed
        self.sound.play()

    def text_objects(self, text):
        text_surface = pygame.font.Font(FONT_TTF_PATH, 20).render(text, True, BLACK)
        return text_surface, text_surface.get_rect()

    def event_check(self):
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if(100 > pos[0] > 50 and 100 > pos[1] > 50):
                    return 3000
        return 0
    
if __name__ == "__main__":
    sorting = Sorting()
    sorting.draw_home()
    clock = pygame.time.Clock()
    
    # -------- Main Program Loop -----------
    while True:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if(100 > pos[0] > 50 and 100 > pos[1] > 50):
                    sorting.win_screen = 1
                if(225 > pos[0] > 100 and 175 > pos[1] > 125):
                    sorting.win_screen = 2
                    sorting.init_arr()
                if(365 > pos[0] > 240 and 175 > pos[1] > 125):
                    sorting.win_screen = 3
                    sorting.init_arr()

        if sorting.win_screen == 1:
            sorting.draw_home()
        elif sorting.win_screen == 2:
            sorting.win_screen = insertion_sort(sorting)
        elif sorting.win_screen == 3:
            sorting.win_screen = quick_sort(sorting, 0, len(sorting.arr) - 1)
        pygame.display.flip()
        clock.tick(60)