#Comparing different sorting algorithms.
from random import randrange
import pygame
pygame.init()
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

def partition(arr,low,high): 
    i = ( low-1 )
    pivot = arr[high] 
    for j in range(low , high):
        if   arr[j] < pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
def quickSort(arr,low,high): 
    if low < high: 
        
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high)


def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key

def createArr():
    N = (randrange(1000))
    Arr = []
    for _ in range(N):
        Arr.append(randrange(1000))
    return Arr

if __name__ == "__main__":
    ArrHold = createArr()
    ArrSort = ArrHold
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Array Sorting Visualizer Program")
    done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
    screen.fill(WHITE)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(60)