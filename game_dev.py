import pygame
from sys import exit

#init() = it starts the pygame

pygame.init()
#we use pygame.display.set_mode(()) to create a screen
#we created a play surface a window use to let the players see whats happening
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')

# we use the variable clock to set the default frames per seconds of a the game and we use the pygame.time.Clock() to input what default ticks/frames we want
clock = pygame.time.Clock()

#we added a font to create basic text on the game. by using pygame.font.Font('filename of the font', size)
test_font = pygame.font.Font('Fonts/Pixeltype.ttf', 50)
# We use render() this method use to render any text surfaces and it needs some inputs whic are the ("TEXT", ANTI ALIAZING COUNT U WANT, "COLOR OF THE TEXT")
text_surface = test_font.render('My Game', False, 'Black')

#we create a surface for the game.

#we have the sky_surface() variable to set the background of the game, pygame.image.load() use to load the imported images so that pygame can use it.
sky_surface = pygame.image.load('Graphics/Sky.png').convert()

ground_surface = pygame.image.load('Graphics/ground.png').convert()

#Enemy Surface 
snail_surface = pygame.image.load('Graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

#Player Surface/Player Rectangle
Player_surface = pygame.image.load('Graphics/player/player_walk_1.png').convert_alpha()
#pygame.rect() use to create a rectangle for a certain image which needs this inputs (lect,top,width,height)
player_rectangle = Player_surface.get_rect(midbottom = (80, 300))


#We need to create a loop that we use infinitely to open the screen window
while True:
    for event in pygame.event.get():
        # this condtion is about if you press the exit button of the display window it will end the display/game
        if event.type == pygame.QUIT:
            pygame.quit()
            
            #we use sys module to exit the loop so it never encounters an error about initializing the screen.
            exit()

    #we use .blit() to call out the created that we made named(test_surface) (block image transfer)       
    screen.blit(sky_surface,(0,0) )
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface, (300,50))

    snail_rect.x -= 3
    #this condition repositions the snail if the snail hits a -100 coordinate on the display coordinate it will continue to move untile it rach again the coordinate 800 of the screen 
    #If the postion(coordinate) of the snail reaches the value of -100 under the 600 default coordinate it will continue walking till it reach the 800 value of coordiniate/position
    if snail_rect.right <= 0: snail_rect.left = 800

    #we increment the value of the X position of the snail to move it on the left side of the display
    screen.blit(snail_surface, snail_rect)
    screen.blit(Player_surface, player_rectangle)
    #inside this loop we draw all of our elements 
    # and update everything that insides the game
    pygame.display.update()
    #clock.tick tells the loop to run a certain frame rate which in our case we can only run (60fps)
    clock.tick(60 )
    

    #---------- we create basic serface now ---------------------



