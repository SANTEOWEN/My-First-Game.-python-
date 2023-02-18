import pygame 
from sys import exit

#init() = it starts the pygame

pygame.init()
#we use pygame.display.set_mode(()) to create a screen
#we need to create a play surface a window use to let the players see whats happening
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

#We need to create a loop that we use infinitely to open the screen window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            #we use sys module to exit the loop so it never encounters an error about initializing the screen.
            exit()
    #inside this loop we draw all of our elements 
    # and update everything that insides the game
    pygame.display.update()
    #clock.tick tells the loop to run a certain frame rate which in our case we can only run (60fps)
    clock.tick(60)
    
