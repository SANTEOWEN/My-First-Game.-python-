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
score_surf = test_font.render('My Game', False, 'Black')
score_rect = score_surf.get_rect(center = (400, 50))

#we create a surface for the game.

#we have the sky_surface() variable to set the background of the game, pygame.image.load() use to load the imported images so that pygame can use it.
sky_surf = pygame.image.load('Graphics/Sky.png').convert()
ground_surf = pygame.image.load('Graphics/ground.png').convert()

#Enemy Surface 
snail_surf = pygame.image.load('Graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600,300))

#Player Surface/Player Rectangle
Player_surf = pygame.image.load('Graphics/player/player_walk_1.png').convert_alpha()
#pygame.rect() use to create a rectangle for a certain image which needs this inputs (lect,top,width,height)
player_rectangle = Player_surf.get_rect(midbottom = (80, 300))


#We need to create a loop that we use infinitely to open the screen window
while True:
    for event in pygame.event.get():
        # this condtion is about if you press the exit button of the display window it will end the display/game
        if event.type == pygame.QUIT:
            pygame.quit()
        #we use sys module to exit the loop so it never encounters an error about initializing the screen.
            exit()
        #we use this event loop to know if the mouse collides on the player rectangle.
        #if event.type == pygame.MOUSEMOTION:
            #if player_rectangle.collidepoint(event.pos): print('collision')

    #we use .blit() to call out the created that we made named(test_surface) (block image transfer)       
    screen.blit(sky_surf,(0,0) )
    screen.blit(ground_surf,(0,300))
    screen.blit(score_surf, (score_rect))

    #we use .x() so the coordinates of the snail turns left reducing the value by 3 so it can reach the default value of 0
    snail_rect.x -= 3

    #in this condition we use the method .right() wiht the value of <= 0 to make the object continue turning left if it hits the value of 800 in coordinate.
    if snail_rect.right <= 0: snail_rect.left = 800

    #we increment the value of the X position of the snail to move it on the left side of the display
    screen.blit(snail_surf, snail_rect)
    screen.blit(Player_surf, player_rectangle)

    #collision is when the character hits the enemy  it will be game over and we use conditional statements to setup the damage to the character.
    #if (player_rectangle.colliderect(snail_rect)):
        #print('collision')

    #pygame.mouse.get_pos() use to know the position of the mouse
    #pygame.mouse.get_pressed() use to know which button of the mouse is getting pressed.

    #mouse_pos = pygame.mouse.get_pos()
    #if player_rectangle.collidepoint((mouse_pos)):
        #print(pygame.mouse.get_pressed())

    #inside this loop we draw all of our elements 
    # and update everything that insides the game
    pygame.display.update()
    #clock.tick tells the loop to run a certain frame rate which in our case we can only run (60fps)
    clock.tick(60)
    

    #---------- we create basic serface now ---------------------



