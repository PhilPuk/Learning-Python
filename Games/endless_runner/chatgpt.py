from pickletools import long1
import random
import pygame, sys
from pygame.math import Vector2

#Init pygame
pygame.init()

#Init window
window_size = (1600,900)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Endless Runner")
clock = pygame.time.Clock()

gameOver = False

#Background
background_textures = []
background_textures.append(pygame.image.load('C:/Users/Phil/Documents/Coding/Python/Learning Python/Games/textures/b_0.png'))

#Grounds
ground_textures = []
ground_textures.append(pygame.image.load('C:/Users/Phil/Documents/Coding/Python/Learning Python/Games/textures/ground_0.png'))
grounds_x = [0, ground_textures[0].get_size()[0], ground_textures[0].get_size()[0] * 2]
ground_to_move = 0
ground_last = 2

#Player
player_velocity = [8,5]
jumping = False
jump_velocity = 0
player_textures = []
player_textures.append(pygame.image.load('C:/Users/Phil/Documents/Coding/Python/Learning Python/Games/textures/player_0.png'))
player_textures.append(pygame.image.load('C:/Users/Phil/Documents/Coding/Python/Learning Python/Games/textures/player_1.png'))
player_pos = [450, window_size[1] - ground_textures[0].get_size()[1] - player_textures[0].get_size()[1]]
sprite_change_max = 20
sprite_change_current = 0
sprite_change_add = 1
player_current_sprite = 0

#Camera
camera_move_right = False

#Bullet
bullet_textures = []
bullet_textures.append(pygame.image.load('C:/Users/Phil/Documents/Coding/Python/Learning Python/Games/textures/ball_0.png'))
ball_velocity = 9.00
ball_pos = Vector2(-200, window_size[1] / 2)
ball_active = False

#Difficulty increase
current_time = 0.00

def player_Quit_Game(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def move_Grounds(velocity_x):
    for i in range(3):
        grounds_x[i] += velocity_x

def jump():
    global jumping
    global jump_velocity
    jumping = True
    jump_velocity = 17

def player_Movement():
    global jumping
    global jump_velocity
    #Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        if not camera_move_right: #Move player
            player_pos[0] += player_velocity[0]
        else: #Move camera
            move_Grounds(-player_velocity[0])
    if keys[pygame.K_a]:
        player_pos[0] -= player_velocity[0]
    
    # Jumping
    if jumping:
        player_pos[1] -= jump_velocity
        jump_velocity -= 0.5 # Decrease jump velocity to simulate gravity
        if player_pos[1] >= window_size[1] - ground_textures[0].get_size()[1] - player_textures[0].get_size()[1]:
            # Player has landed on the ground
            jumping = False
            jump_velocity = 0
            player_pos[1] = window_size[1] - ground_textures[0].get_size()[1] - player_textures[0].get_size()[1]
    else: #Player on ground
        if keys[pygame.K_w]:
            jump() # Jump when W key is pressed

def checkCameraMovement():
    global camera_move_right
    if player_pos[0] > window_size[0] / 2.5: #Player right moving
        camera_move_right = True
    else:
        camera_move_right = False

def checkGroundReplace():
    global ground_to_move
    global ground_last
    if grounds_x[ground_to_move] < -ground_textures[0].get_size()[0]: 
        grounds_x[ground_to_move] = grounds_x[ground_last] + ground_textures[0].get_size()[0] #Move ground that goes outofscreen at left to the total right
        if ground_to_move < 2:
            ground_to_move += 1
        else:
            ground_to_move = 0
        if ground_last < 2:
            ground_last += 1
        else:
            ground_last = 0

def changePlayerSprite():
    global sprite_change_current
    global sprite_change_add
    global player_current_sprite
    if sprite_change_current >= sprite_change_max:
        sprite_change_current = 0
        if player_current_sprite == 0:
            player_current_sprite = 1
        else:
            player_current_sprite = 0
    else:
        sprite_change_current += sprite_change_add

def ballShooting():
    global ball_active
    global ball_pos
    if not ball_active: #Roll to activate the ball
        roll = random.randint(0,1000)
        if roll > 960:
            ball_active = True
            ball_pos[0] = window_size[0] + bullet_textures[0].get_size()[0] * 2
    else:
        if ball_pos[0] < -bullet_textures[0].get_size()[0]:
            ball_active = False
        else: 
            ball_pos[0] -= ball_velocity

def checkBallPlayerCollision():
    global gameOver
    if ball_pos[1] < player_pos[1] + player_textures[0].get_size()[1]:
        if ball_pos[0] < player_pos[0] + player_textures[0].get_size()[0] and ball_pos[0] > player_pos[0]:
            gameOver = True

def increaseTimer():
    global current_time
    global player_velocity
    global ball_velocity
    current_time += 0.000001
    player_velocity[0] = player_velocity[0] * (1 + current_time * 0.03)
    ball_velocity = ball_velocity * (1 + current_time * 0.2)

def event_Manager():
    for event in pygame.event.get():
        player_Quit_Game(event)
    checkCameraMovement()
    player_Movement()
    changePlayerSprite()
    checkGroundReplace()
    ballShooting()
    checkBallPlayerCollision()
    increaseTimer()

def renderBackground():
    window.blit(background_textures[0], (0,-150))

def render():
    window.fill((0,100,255)) #Clear screen with color
    renderBackground()
    window.blit(player_textures[player_current_sprite], (player_pos[0], player_pos[1]))
    window.blit(bullet_textures[0], (ball_pos[0],ball_pos[1]))
    window
    for i in range(3):
        window.blit(ground_textures[0], (grounds_x[i], window_size[1] - ground_textures[0].get_size()[1]))
    pygame.display.flip() #Display all drawed objects

#Game loop
while not gameOver:
    event_Manager() #Handles user inputs
    render()
    #FPS
    clock.tick(60)

if gameOver:
    pygame.quit()
    sys.exit()
