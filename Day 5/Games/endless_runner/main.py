import pygame, sys

#Init pygame
pygame.init()

#Init window
window_size = (1600,900)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Endless Runner")
clock = pygame.time.Clock()

#Grounds
ground_textures = []
ground_textures.append(pygame.image.load('C:/Users/Phil/Documents/Coding/Python/Learning Python/Games/textures/ground_0.png'))
grounds_x = [0, ground_textures[0].get_size()[0], ground_textures[0].get_size()[0] * 2]
ground_to_move = 0
ground_last = 2

#Player
player_velocity = [8,5]
jumping = False
player_textures = []
player_textures.append(pygame.image.load('C:/Users/Phil/Documents/Coding/Python/Learning Python/Games/textures/player_0.png'))
player_pos = [450, window_size[1] - ground_textures[0].get_size()[1] - player_textures[0].get_size()[1]]

#Camera
camera_move_right = False

def player_Quit_Game(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

def move_Grounds(velocity_x):
    for i in range(3):
        grounds_x[i] += velocity_x

def player_Movement():
    #Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        jumping = True # Placeholder
    if keys[pygame.K_d]:
        if not camera_move_right: #Move player
            player_pos[0] += player_velocity[0]
        else: #Move camera
            move_Grounds(-player_velocity[0])
    if keys[pygame.K_a]:
        player_pos[0] -= player_velocity[0]

def checkCameraMovement():
    global camera_move_right
    if player_pos[0] > window_size[0] / 2: #Player right moving
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


def event_Manager():
    for event in pygame.event.get():
        player_Quit_Game(event)
    checkCameraMovement()
    player_Movement()
    checkGroundReplace()

def render():
    window.fill((0,100,255)) #Clear screen with color
    window.blit(player_textures[0], (player_pos[0], player_pos[1]))
    for i in range(3):
        window.blit(ground_textures[0], (grounds_x[i], window_size[1] - ground_textures[0].get_size()[1]))
    pygame.display.flip() #Display all drawed objects

#Game loop
while True:
    event_Manager() #Handles user inputs
    render()
    #FPS
    clock.tick(60)