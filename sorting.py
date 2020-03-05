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
pygame.display.set_caption("Array Sorting Visualizer Program")


N = 250

#ARRAY DEFINITIONS
Arr = []
ArrRects = []
ArrHold = []

# Define some colors
BLACK        = (   0,   0,   0)
WHITE        = ( 255, 255, 255)
GREEN        = (   0, 255,   0)
RED          = ( 255,   0,   0)
BLUE         = (   0,   0, 255)
lightBLUE    = ( 135, 206, 250)
#Buttons
def text_objects(text, font):
    textSurface = font.render(text, True, WHITE)
    return textSurface, textSurface.get_rect()

homeBut = pygame.image.load("home.png").convert_alpha()
homeBut = pygame.transform.scale(homeBut,(50,50))
Text = pygame.font.Font("AveraSansTcBld.ttf",20)
inserSurf, inserRect = text_objects("Insertion Sort", Text)
inserRect.center = ((160), (150)) 
quickSurf, quickRect = text_objects("Quick Sort", Text)
quickRect.center = ((300), (150))

def createArr():
    for _ in range(N):
        Arr.append(randrange(500))
    return Arr
def partition(low,high): 
    i = (low-1)
    pivot = Arr[high] 
    for j in range(low , high):
        #event check breaks when click on home button, fix
        check = eventCheck()
        if(check == 100):
            return 100
        if(check == 1):
            return 1
        if(Arr[j] < pivot): 
            i = i+1 
            Arr[i],Arr[j] = Arr[j],Arr[i]
            update(j)
            update(i) 
    Arr[i+1],Arr[high] = Arr[high],Arr[i+1]
    update(high)
    update(i+1) 
    return ( i+1 ) 
def quickSort(low,high): 
    if low < high: 
        
        pi = partition(low,high) 
        quickSort(low, pi-1) 
        quickSort(pi+1, high)
    return 0
def eventCheck():
    for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT:
                return 100
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if(100 > pos[0] > 50 and 100 > pos[1] > 50):
                    return 1

def insertionSort(): 
    for i in range(1, len(Arr)):
        check = eventCheck()
        if(check == 100):
            return 100
        if(check == 1):
            return 1
        key = Arr[i] 
        j = i-1
        while j >= 0 and key < Arr[j] : 
                Arr[j + 1] = Arr[j]
                update(j+1) 
                j -= 1
        Arr[j + 1] = key
        update(j+1)
          

def update(curr):
    screen.fill(WHITE)
    #Finish title bar on home and during sorting
    pygame.draw.rect(screen, BLUE ,(160,20,440,100))
    screen.blit(homeBut,(50,50))
    ArrRects = []
    for i in range(N):
        ArrRects.append(pygame.Rect((2*i)+100,HEIGHT-50,arrWidth,-Arr[i]/2))
        R = abs(Arr[i]/2-120)
        G = abs(Arr[i]/2 - 50)
        B = abs(Arr[i]/2)
        if i == curr:
            R, G, B = 0, 0, 0
        pygame.draw.rect(screen, ( R, G, B ), ArrRects[i])
    pygame.display.flip()
    
    
    

def drawHome():
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE ,(160,20,440,100))
    #Create Home Button
    h = screen.blit(homeBut,(50,50))
    #Add Buttons for each 
    pygame.draw.rect(screen, lightBLUE ,(100,125,125,50))
    pygame.draw.rect(screen, lightBLUE ,(240,125,125,50))
    i = screen.blit(inserSurf, inserRect)
    q = screen.blit(quickSurf, quickRect)
    pygame.display.flip()
    

if __name__ == "__main__":
    Arr = createArr()
    ArrRects = []
    drawHome()
    currentScreen = 0
    clock = pygame.time.Clock()
    
    # -------- Main Program Loop -----------
    while currentScreen != 100:
        Arr = []
        Arr = createArr()
        h = screen.blit(homeBut,(50,50))
        i = screen.blit(inserSurf, inserRect)
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                pygame.quit()
                quit()
                currentScreen = 100
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if(100 > pos[0] > 50 and 100 > pos[1] > 50):
                    currentScreen = 1
                if(225 > pos[0] > 100 and 175 > pos[1] > 125):
                    currentScreen = 2
                if(365 > pos[0] > 240 and 175 > pos[1] > 125):
                    currentScreen = 3
        if(currentScreen == 1):
            currentScreen = drawHome()
            currentScreen = 0
        if(currentScreen == 2):
            currentScreen = insertionSort()
            currentScreen = 0
        if(currentScreen == 3):
            currentScreen = quickSort(0,len(Arr)-1)
            currentScreen = 0
        

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        clock.tick(60)