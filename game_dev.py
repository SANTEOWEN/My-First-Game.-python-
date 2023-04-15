import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
	def __init__(self):
        #This is the player sprite with its 
		super().__init__()
		player_walk_1 = pygame.image.load('Graphics/player/player_walk_1.png').convert_alpha()
		player_walk_2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
		self.player_walk = [player_walk_1,player_walk_2]
		self.player_index = 0
		self.player_jump = pygame.image.load('Graphics/player/jump.png').convert_alpha()

		self.image = self.player_walk[self.player_index]
		self.rect = self.image.get_rect(midbottom = (80,300))
        #This is the default value of the gravity
		self.gravity = 0

		self.jump_sound = pygame.mixer.Sound('Sounds/jump.mp3')
		self.jump_sound.set_volume(0.5)
    # This function allows us to use the keys in our keyboard and in this case we especifically use the key "Space" and we also added a sound that everytime player hits the space button the character will jump and the sound will be triggered
	def player_input(self):
		keys = pygame.key.get_pressed()
        #when ever the player pressed the space button the character will increment its height value by -20 thicks and the sound trigger will be played.
		if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            
			self.gravity = -20
			self.jump_sound.play()
    # We also apply the gravity physics so the player can jump like a human
	def apply_gravity(self):
        #we set a default value of 1 so we can increment it everytime the player jumps
		self.gravity += 1
        #We set the value of the player rect Y coordinates into the default value of the gravity so it can do the jump physics
		self.rect.y += self.gravity
        #we have a condition here that if the character rect value increases because of the gravity incrementation the condition will be activated and it will set the incremented value back to its default value which is 300 x coordinate.
		if self.rect.bottom >= 300:
			self.rect.bottom = 300

	def animation_state(self):
        # if the player pressed the space and the value of the X coordinates went to 300 the jump animation will be triggered.
		if self.rect.bottom < 300: 
			self.image = self.player_jump
		else:
        #this self.player_index += 0.1 is the value we need to move the first walk animation
			self.player_index += 0.1
            # and in this condition every time the player_index becomes greater than or equal to the length of player walk we simple brings it back to its default value which is 0 so it can loop back to back
            # basically if the player index value goes higher than the default value, the condition will be triggered and it will reset its value to the default one so it can continue looping.
			if self.player_index >= len(self.player_walk):self.player_index = 0
			self.image = self.player_walk[int(self.player_index)]

	def update(self):
        # Now we run all of the created functions inside a one function so it can easily call all of it at once.
		self.player_input()
		self.apply_gravity()
		self.animation_state()

class Obstacle(pygame.sprite.Sprite):
	def __init__(self,type):
		super().__init__()
		# We have here are the same as the player we added the animation and stuffs 
		if type == 'fly':
			fly_1 = pygame.image.load('Graphics/fly/fly1.png').convert_alpha()
			fly_2 = pygame.image.load('Graphics/fly/fly2.png').convert_alpha()
			self.frames = [fly_1,fly_2]
			y_pos = 210
		else:
			snail_1 = pygame.image.load('Graphics/snail/snail1.png').convert_alpha()
			snail_2 = pygame.image.load('Graphics/snail/snail2.png').convert_alpha()
			self.frames = [snail_1,snail_2]
			y_pos  = 300
        
        #this section is for the animation same on the player
		self.animation_index = 0
		self.image = self.frames[self.animation_index]
        # This arguments randomize the spawn position of the obstacle so they can spawn in different places.
		self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

	def animation_state(self):
		self.animation_index += 0.1 
		if self.animation_index >= len(self.frames): self.animation_index = 0
		self.image = self.frames[int(self.animation_index)]

	def update(self):
		self.animation_state()
		self.rect.x -= 6
		self.destroy()

	def destroy(self):
		if self.rect.x <= -100: 
			self.kill()

def display_score():
    #This display score out is base on pygame.time we use the time function so we can get an unique scoring system.
    #We devided the default of the pygame.time into 1000 so it will show as simple integer.
	current_time = int(pygame.time.get_ticks() / 1000) - start_time
    #we also render the word score and the score itself
	score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    #we added the position of the score at the center of the screen
	score_rect = score_surf.get_rect(center = (400,50))
    #Then we draw the rect and the score surface so it will apear on the screen.
	screen.blit(score_surf,score_rect)
    # now we return values so we can use it on other functions.
	return current_time

def collision_sprite():
	if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
		obstacle_group.empty()
		return False
	else: return True


pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('TAKBO')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Fonts/Pixeltype.ttf', 50)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('Sounds/music.wav')


bg_music.play(loops = -1)

#Groups
#This sprite group represents the player sprite we created a group so we can easily call it out.
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()


#This 2 surfaces are used for the background and the ground setups.
sky_surface = pygame.image.load('Graphics/Sky.png').convert()
ground_surface = pygame.image.load('Graphics/ground.png').convert()

# Intro screen
# We render the player 2 image inside the intro screen so it can show some graphics
player_stand = pygame.image.load('Graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

#we also render the word takbo as the tittle of the game
game_name = test_font.render('TAKBO',False,(111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

#and we render the word "Press space to run" so the player will know how to restart the game.
game_message = test_font.render('Press space to run',False,(111,196,169))
game_message_rect = game_message.get_rect(center = (400,330))

# Timer 
#This one serves as a timer.
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

while True:
	for event in pygame.event.get():
        #we created a game event that if press the exit button it will exit the game
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

		if game_active:
            #This condition randomize the spawn time of every obstacles(enemies) when ever the game starts using the creation of game event and pygame timer. this condition will randomize between snail or fly enemy with the time thick of 1.5 milleseconds
			if event.type == obstacle_timer:
				obstacle_group.add(Obstacle(choice(['fly','snail','snail','snail'])))
		
		else:
            #this condition will trigger if the player used the space(key) to set the variable game active to true so it can retry the game and it also resets the game score to 0
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				game_active = True
				start_time = int(pygame.time.get_ticks() / 1000)


	if game_active:
		screen.blit(sky_surface,(0,0))
		screen.blit(ground_surface,(0,300))
        
        #This one calls out the function (display score) to display the score
		score = display_score()

		 #Sprite groups in pygame have 2 main diferent functions which is to draw and update all of the sprites 
        #Player.draw (draws all of the rectangles on the screen)
		player.draw(screen)
		player.update()

		obstacle_group.draw(screen)
		obstacle_group.update()

        #This one tells the program to stop after the player colide on any obstacles
		game_active = collision_sprite()
		
	else:
		screen.fill((94,129,162))
		screen.blit(player_stand,player_stand_rect)

        #This one renders the word [Your score] including your real score
		score_message = test_font.render(f'Your score: {score}',False,(111,196,169))
		score_message_rect = score_message.get_rect(center = (400,330))
		screen.blit(game_name,game_name_rect)

        # now we created a condition state that everytime the players dies the score will show up after it hits any enemy
		if score == 0: screen.blit(game_message,game_message_rect)
		else: screen.blit(score_message,score_message_rect)
    
    #This one updates the whole game itself
	pygame.display.update()
    #clock.tick tells the loop to run a certain frame rate which in our case we can only run (60fps)
	clock.tick(60)