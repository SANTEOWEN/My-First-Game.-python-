import pygame
from sys import exit
from random import randint


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Graphics/player/player_walk_1.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom =(200,300))
        
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

# This  function detects if the player collides on the enemy(obstacle) surface, if the player surface collides on the enemy surface it will end the game and go on the retry game state.
def collisions(player, obstacles):
    if obstacles:
        for obs_rect in obstacles:
            # this conditions tells us if the player colides on obstacle rectangle(enemy) the game will end and will go on retry state.
            if player.colliderect(obs_rect): return False
    return True

def player_animation():
    global player_surf, player_index

    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        #We incremented +0.1 to slowly move the animation by 0.1 pixels under the player_index so if the player moves it slowly moves by 0.1 milleseconds
        player_index += 0.1

        # this condition tells us that if the player_index becomes greater than or equal to the length of player walk we simple brings it back to its default value which is 0 so it can loop back to back
        # the player  index went too large this condition statement down here will bring its value back on default.
        if player_index >= len(player_walk): player_index = 0

        player_surf = player_walk[int(player_index)]


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
player = Player()
#score_surf = test_font.render('My Game', False, (0, 0, 0))
#score_rect = score_surf.get_rect(center = (400, 50))
#we create a surface for the game.

#we have the sky_surface() variable to set the background of the game, pygame.image.load() use to load the imported images so that pygame can use it.
sky_surf = pygame.image.load('Graphics/Sky.png').convert()
ground_surf = pygame.image.load('Graphics/ground.png').convert()

#snail
snail_frame_1 = pygame.image.load('Graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('Graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]


#fly
fly_frame1 = pygame.image.load('Graphics/Fly/Fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('Graphics/Fly/Fly2.png').convert_alpha()
fly_frames = [fly_frame1, fly_frame2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obs_rect_list = []

#Player Surface/Player Rectangle
#pygame.rect() use to create a rectangle for a certain image which needs this inputs (lect,top,width,height)
Player_walk1 = pygame.image.load('Graphics/player/player_walk_1.png').convert_alpha()
Player_walk2 = pygame.image.load('Graphics/player/player_walk_2.png').convert_alpha()
player_walk = [Player_walk1, Player_walk2]
player_index = 0
player_jump = pygame.image.load('Graphics/player/jump.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80, 300))
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

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 200)

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
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_grav = -20
                
            #this event loop us to get key inputs using the combined pygame.key() and eventloop method   
            if event.type == pygame.KEYDOWN:
                #this combined conditions tells us that the character can only jump if its on the ground surface. 
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_grav = -20
        else:
            #This statement serves as the restart button everytime it hits the space key it will restart the game after the collision of enemy_rectangle.
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = int(pygame.time.get_ticks() / 1000) 

        if game_active:
            if event.type == obs_timer:
            # we use the randint to randomize this 2 obstacle so everytime the randint method gives 1 the snail will pop out and if it gives us a 0 the fly will pop out.
                if randint(0,2):
                    obs_rect_list.append(snail_surf.get_rect(midbottom = (randint(900,1100),300)))
                else:
                    obs_rect_list.append(fly_surf.get_rect(midbottom = (randint(900,1100),210)))

            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else: snail_frame_index = 0
                snail_surf = snail_frames[snail_frame_index]
    
            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]
    

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
        player_rect.y += player_grav 
        #this conditional statement use to make the character stays on the surface and not fall down because of the gravity variable.
        if player_rect.bottom >= 300: 
            player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf, player_rect)

        #OBSTACLE MOVEMENT
        # first we run the function [obs_movement] 
        # then it will take the obstacle rect list which is under the game event loop then move every single rect a b it further to the left.
        # after all of process is done we override the rect_list to continuesly update the list inside the function
        obs_rect_list = obs_movement(obs_rect_list)

        #COLLISIONS ON ENEMIES
        #First the function will run and dectet the collisions
        # then if the detection went true the game state will go retry mode
        # If the collision turns false  the game state will turn on retry mode and if doesnt it will continue the game
        game_active = collisions(player_rect, obs_rect_list)
            
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        
        
        # we use the clear() method to clear all of the entity created so it will not loop the game again and again.
        obs_rect_list.clear()
        # ------- we reinput the position of the player so it will go back on its default position ------- #
        player_rect.midbottom = (80,300) 
        # ------- same as the gravity so the position of the character still the same ------- #
        player_grav = 0

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
    clock.tick(60)
    





