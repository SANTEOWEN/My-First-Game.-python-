import pygame
from sys import exit
from random import randint

#x = width (width always turns left and right) y = height (height always turns up and down)
# This function use to show the time in game which is our score system
#we created variable valued with 0 so every time the or if the player presses the keyinputs the value of time.ticks will reset to 0, we subtract 0 on the current game time to reset the value of the current time.
def display_score():
    current_t = int(pygame.time.get_ticks() / 1000) - start_time 
    score_surf = test_font.render(f'SCORE: {current_t}',False,(0,0,0))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf,score_rect)
    # we use return method to return any value from the varaiable current_t()
    return current_t

#
def obs_movement(obs_list):
    #we first need to check if theres something in the list
    if obs_list:
        #for every obstacle_rectangles on the obstacle list we are moving every single obs by every 5 secs. 
        for obs_rect in obs_list:
            obs_rect.x -= 5

            #Now we created a condition obs_rect is not at the bottom 300 the snail will spawn if its not the fly will spawn
            if obs_rect.bottom == 300:screen.blit(snail_surf, obs_rect)
            else: screen.blit(fly_surf,obs_rect)
                
        #we copy the existing item(rect) on the list every time the x greater than -100
        # we are only going to copy every single item on the list if the condition is true that the x attribute is greater than 0
        obs_list = [obstacle for obstacle in obs_list if obstacle.x > -100]
        #Now we need a global scope for returning a new list.
        return obs_list
    else: return []


#init() = it starts the pygame
pygame.init()
#we use pygame.display.set_mode(()) to create a screen
#we created a play surface a window use to let the players see whats happening
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Takbo')
# we use the variable clock to set the default frames per seconds of a the game and we use the pygame.time.Clock() to input what default ticks/frames we want
clock = pygame.time.Clock()
#we added a font to create basic text on the game. by using pygame.font.Font('filename of the font', size)
test_font = pygame.font.Font('Fonts/Pixeltype.ttf', 50)
# We use render() this method use to render any text surfaces and it needs some inputs whic are the ("TEXT", ANTI ALIAZING COUNT U WANT, "COLOR OF THE TEXT")

game_active = False
start_time = 0
#then we created a especific variable to pin out the values from the function called display()
score = 0
#score_surf = test_font.render('My Game', False, (0, 0, 0))
#score_rect = score_surf.get_rect(center = (400, 50))

#we create a surface for the game.

#we have the sky_surface() variable to set the background of the game, pygame.image.load() use to load the imported images so that pygame can use it.
sky_surf = pygame.image.load('Graphics/Sky.png').convert()
ground_surf = pygame.image.load('Graphics/ground.png').convert()

#Enemy Surface 
snail_surf = pygame.image.load('Graphics/snail/snail1.png').convert_alpha()

fly_surf = pygame.image.load('Graphics/fly/fly1.png').convert_alpha()

obs_rect_list = []

#Player Surface/Player Rectangle
Player_surf = pygame.image.load('Graphics/player/player_walk_1.png').convert_alpha()
#pygame.rect() use to create a rectangle for a certain image which needs this inputs (lect,top,width,height)
player_rectangle = Player_surf.get_rect(midbottom = (80, 300))
player_grav = 0

#Intro Screen
#This surface use to create a intro to start the game and we call this surface under the game active condition!
player_stand = pygame.image.load('Graphics/player/player_stand.png').convert_alpha() # 1. we import the image here
#.scale() use to double the image widtg but keeps the height the same
#.scale2x() basically the same as the scale() but its boneless and easy to use
#.rotozoom() it is also use to resize but this one makes the image more smoother
player_stand = pygame.transform.rotozoom(player_stand, 0, 2) #2. we take the imported image(player_stand) and returning a new surface by overiding it
player_stand_rect = player_stand.get_rect(center = (400,200)) #3. we create a rectangle variable.

game_name = test_font.render("TAKBO", False, (111,196,169))
game_name_rect = game_name.get_rect(center = (400,70))

game_message = test_font.render("Press space to run", False, (111,196,169))
game_message_rect = game_message.get_rect(center = (415, 330))

#-----------------------------------------TIMER for the game events----------------------------------------------------#

obs_timer = pygame.USEREVENT + 1
#set_timer() needs 2 different arguments, 1. the event you want to trigger 2. how often we want it to trigger the event in mille seconds
pygame.time.set_timer(obs_timer,1500)

#---------------------------------------- EVENT/LOOPS SECTION -------------------------------------#



#We need to create a loop that we use infinitely to open the screen window
while True: 
    for event in pygame.event.get():
        # this condtion is about if you press the exit button of the display window it will end the display/game
        if event.type == pygame.QUIT:
            pygame.quit()
        #we use sys module to exit the loop so it never encounters an error about initializing the screen.
            exit()

        if game_active:
            #we use this event loop to know if the mouse collides on the player rectangle.
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom >= 300:
                    player_grav = -20
                
            #this event loop us to get key inputs using the combined pygame.key() and eventloop method   
            if event.type == pygame.KEYDOWN:
                #this combined conditions tells us that the character can only jump if its on the ground surface. 
                if event.key == pygame.K_SPACE and player_rectangle.bottom >= 300:
                    player_grav = -20
        else:
            #This statement serves as the restart button everytime it hits the space key it will restart the game after the collision of enemy_rectangle.
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000) 



        if event.type == obs_timer and game_active:
            # we use the randint to randomize this 2 obstacle so everytime the randint method gives 1 the snail will pop out and if it gives us a 0 the fly will pop out.
            if randint(0,2):
                obs_rect_list.append(snail_surf.get_rect(midbottom = (randint(900,1100),300)))
            else:
                obs_rect_list.append(fly_surf.get_rect(midbottom = (randint(900,1100),210)))

    #inside this loop we draw all of our elements             
    if game_active:       
        #we use .blit() to call out the created surface that we named(test_surface) (block image transfer)       
        screen.blit(sky_surf,(0,0) )
        screen.blit(ground_surf,(0,300))

        #pygame.draw() use to create/draw any shapes on any part of the screen using this attributes (name of the screen, color, what surface)
        #pygame.draw.rect(screen, '#f1cbff', score_rect)
        #pygame.draw.rect(screen, '#f1cbff', score_rect,20)
        #screen.blit(score_surf, (score_rect))

        score = display_score()

        #we use .x() so the coordinates of the snail turns left reducing the value by 3 so it can reach the default value of 0
        #snail_rect.x -= 5

        #in this condition we use the method .right() wiht the value of <= 0 to make the object continue turning left if it hits the value of 800 in coordinate.
        #we increment the value of the X position of the snail to move it on the left side of the display

        #if snail_rect.right <= 0: snail_rect.left = 800


        #screen.blit(snail_surf, snail_rect)

        #PLAYER_GRAVITY_PYSHICS
        #this part also serves as the gravity physics of the player!
        player_grav += 1
        player_rectangle.y += player_grav 
        #this conditional statement use to make the character stays on the surface and not fall down because of the gravity variable.
        if player_rectangle.bottom >= 300: player_rectangle.bottom = 300
        screen.blit(Player_surf, player_rectangle)

        #OBSTACLE MOVEMENT
        # first we run the function [obs_movement] 
        # then it will take the obstacle rect list which is under the game event loop then move every single rect a b it further to the left.
        # after all of process is done we override the rect_list to continuesly update the list inside the function
        obs_rect_list = obs_movement(obs_rect_list)
            
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        
        score_message = test_font.render(f'Your Score is: {score}', False,(111,196,169))
        score_message_rect = score_message.get_rect(center = (400, 330))

        screen.blit(game_name, game_name_rect)
        # now we created a condition state that everytime the players dies the score will show up after it hits any enemy
        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
        
    # and update everything that insides the game
    pygame.display.update()
    #clock.tick tells the loop to run a certain frame rate which in our case we can only run (60fps)
    clock.tick(75)
    





