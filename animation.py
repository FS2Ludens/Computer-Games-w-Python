import pygame, sys, time
from pygame.locals import *

#setup pygame
pygame.init()

#setup the window
WINDOWWIDTH = 750
WINDOWHEIGHT = 600
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation')

#setup direction variables
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 7

#setup the colors
BG = (0, 0, 0)
RED = (250, 0, 50)
GREEN = (0, 200, 0)
BLUE = (75, 50, 255)
RANDOM = (250, 150, 100)

#setup the box data structure
b1 = {'rect':pygame.Rect(239, 500, 275, 115), 'color':RED, 'dir':UPRIGHT}
b2 = {'rect':pygame.Rect(453, 176, 75, 150), 'color':GREEN, 'dir':UPLEFT}
b3 = {'rect':pygame.Rect(151, 32, 250, 250), 'color':BLUE, 'dir':DOWNLEFT}
b4 = {'rect':pygame.Rect(100, 50, 43, 32), 'color':RANDOM, 'dir':DOWNRIGHT}
boxes = [b4, b3, b2, b1]

#run the game loop
while True:
    #check for the Quit event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #draw the white background on the surface
    windowSurface.fill(BG)

    for b in boxes:
        #move the box data structure
        if b['dir'] == DOWNLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == DOWNRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top += MOVESPEED
        if b['dir'] == UPLEFT:
            b['rect'].left -= MOVESPEED
            b['rect'].top -= MOVESPEED
        if b['dir'] == UPRIGHT:
            b['rect'].left += MOVESPEED
            b['rect'].top -= MOVESPEED

        #check whther the box has moved out of the window
        if b['rect'].top < 0:
            #the box has moved past the top
            if b['dir'] == UPLEFT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = DOWNRIGHT

        if b['rect'].bottom > WINDOWHEIGHT:
            #the box has moved past the bottom
            if b['dir'] == DOWNLEFT:
                b['dir'] = UPLEFT
            if b['dir'] == DOWNRIGHT:
                b['dir'] = UPRIGHT
        if b['rect'].left < 0:
            #the box has moved past the left side
            if b['dir'] == DOWNLEFT:
                b['dir'] = DOWNRIGHT
            if b['dir'] == UPLEFT:
                b['dir'] = UPRIGHT
        if b['rect'].right > WINDOWWIDTH:
            #the box has moved past the right side
            if b['dir'] == DOWNRIGHT:
                b['dir'] = DOWNLEFT
            if b['dir'] == UPRIGHT:
                b['dir'] = UPLEFT

        #draw the box onto the surface
        pygame.draw.rect(windowSurface, b['color'], b['rect'])

    #draw the window onto the screen
    pygame.display.update()
    time.sleep(0.02)
