# Simple pygame program

# Import and initialize the pygame library
import pygame
import sys 
from GameArray import LifeArray 
import numpy as np

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

def drawGrid(WINDOW_WIDTH, WINDOW_HEIGHT, screen, blockSize):
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, (0,30,50), rect, 1)

pygame.init()

# Set up the drawing window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
blocksize = 40
array = LifeArray(SCREEN_HEIGHT//blocksize, SCREEN_WIDTH//blocksize, True)

# set clock
# Setup the clock for a decent framerate
clock = pygame.time.Clock()
# Run until the user asks to quit
running = True
array.print()
print(array.LifeArr.shape)
paused = False
while running:
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p: # Pausing/Unpausing
                paused = not paused
            if event.key == pygame.K_s:
                array.print()
        elif event.type == pygame.MOUSEBUTTONDOWN: # Creating new live cell 
            y,x = event.pos
            x = x // blocksize
            y = y // blocksize
            array.born(x,y)
            x*=blocksize
            y*=blocksize
            pygame.draw.rect(screen,(min(x,255),min(y,255),0),pygame.Rect(y,x,blocksize,blocksize))
            pygame.display.flip()

    if not paused:
        keys = pygame.key.get_pressed()
        # Fill the screen with white
        screen.fill((255, 255, 255))
        drawGrid( SCREEN_WIDTH, SCREEN_HEIGHT,screen, blocksize)
        # Create a surface and pass in a tuple containing its length and width
        surf = pygame.Surface((15, 10))

        # Give the surface a color to separate it from the background
        surf.fill((0, 0, 0))
        rect = surf.get_rect()
        array.update()
        for p in np.ndenumerate(array.LifeArr):
            if p[1] == 1:
                x, y = p[0]
                x*=blocksize
                y*=blocksize
                pygame.draw.rect(screen,(min(x,255),min(y,255),0),pygame.Rect(y,x,blocksize,blocksize))
        # Flip the display
        
        pygame.display.flip()

        # Ensure program maintains a rate of 30 frames per second
        clock.tick(0.5)
# Done! Time to quit.
pygame.quit()

