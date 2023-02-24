import pygame 
from sys import exit

#init() = it starts the pygame

pygame.init()
#we use pygame.display.set_mode(()) to create a screen
#we need to create a play surface a window use to let the players see whats happening
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
# we use the variable clock to set the default frames per seconds of a the game.
clock = pygame.time.Clock()

#we added a font to create basic text on the game.
test_font = pygame.font.Font('Fonts/Pixeltype.ttf', 50)

#we create a surface_1 for the game.
sky_surface = pygame.image.load('Graphics/Sky.png')
ground_surface = pygame.image.load('Graphics/ground.png')

# We use render() this method use to render any text surfaces and it needs some inputs whic are the ("TEXT", ANTI ALIAZING COUNT U WANT, "COLOR OF THE TEXT")
text_surface = test_font.render('My Game', False, 'Black')

#We need to create a loop that we use infinitely to open the screen window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
            #we use sys module to exit the loop so it never encounters an error about initializing the screen.
            exit()

    #we use .blit() to call out the created that we made named(test_surface) (block image transfer)       
    screen.blit(sky_surface,(0,0) )
    screen.blit(ground_surface,(0,250))
    screen.blit(text_surface, (350,50))

    #inside this loop we draw all of our elements 
    # and update everything that insides the game
    pygame.display.update()
    #clock.tick tells the loop to run a certain frame rate which in our case we can only run (60fps)
    clock.tick(60)
    

    #---------- we create basic serface now ---------------------



