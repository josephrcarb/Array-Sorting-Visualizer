#Comparing different sorting algorithms.
from random import randrange
import pygame
pygame.init()
pygame.mixer.music.load('beep.mp3')


# DIMENSIONS OF WINDOW
WIDTH = 700
HEIGHT = 500
arrWidth = 2
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)

N = 250

#ARRAY DEFINITIONS
Arr = []
ArrRects = []

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

def partition(low,high): 
    i = ( low-1 )
    pivot = Arr[high] 
    for j in range(low , high):
        if   Arr[j] < pivot: 
            i = i+1 
            Arr[i],Arr[j] = Arr[j],Arr[i] 
    Arr[i+1],Arr[high] = Arr[high],Arr[i+1] 
    return ( i+1 ) 
def quickSort(low,high): 
    if low < high: 
        
        pi = partition(low,high) 
        quickSort(low, pi-1) 
        quickSort(pi+1, high)

def eventCheck():
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT:
                return True

def insertionSort(): 
    for i in range(1, len(Arr)): 
        
        key = Arr[i] 
        j = i-1
        while j >= 0 and key < Arr[j] : 
                Arr[j + 1] = Arr[j]
                update(j+1) 
                j -= 1
        Arr[j + 1] = key
        update(j+1)
        if eventCheck() == True:
            return True

def createArr():
    for _ in range(N):
        Arr.append(randrange(500))
    return Arr

def update(curr):
    screen.fill(WHITE)
    ArrRects = []
    for i in range(N):
        ArrRects.append(pygame.Rect((2*i)+100,HEIGHT-50,arrWidth,-Arr[i]/2))
        R = abs(0)
        G = abs(Arr[i]/2 - 255)
        B = abs(Arr[i]/2)
        if i == curr:
            R, G, B = 0, 0, 0
        pygame.draw.rect(screen, ( R, G, B ), ArrRects[i])
    pygame.display.flip()
    
    
    


def drawArr():
    screen.fill(WHITE)
    for i in range(N):
        pygame.draw.rect(screen, BLACK, ArrRects[i])
    
    



if __name__ == "__main__":
    ArrHold = createArr()
    ArrRects = []
    
    pygame.display.set_caption("Array Sorting Visualizer Program")
    done = False
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    update(0)
    insertionSort()
    # -------- Main Program Loop -----------
    while not done:
        update(0)
        
        done = insertionSort()
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        clock.tick(60)