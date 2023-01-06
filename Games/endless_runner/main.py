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

#Player
player_velocity = 4
y_velocity = 0
jumping = False
player_textures = []
player_textures.append(pygame.image.load('C:/Users/Phil/Documents/Coding/Python/Learning Python/Games/textures/player_0.png'))
player_pos = [0, window_size[1] - ground_textures[0].get_size()[1] - player_textures[0].get_size()[1]]
#Game loop
while True:
    #User Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Player Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if not jumping:
            y_velocity = 10
            jumping = True
    else:
        if jumping:
            y_velocity = -10
        else:
            y_velocity = 0
    if keys[pygame.K_d]:
        player_pos[0] += player_velocity
    if keys[pygame.K_a]:
        player_pos[0] -= player_velocity
    player_pos[1] += y_velocity
    #Check if player has landed
    if player_pos[1] > window_size[1] - ground_textures[0].get_size()[1] - player_textures[0].get_size()[1]:
        player_pos[1] = window_size[1] - ground_textures[0].get_size()[1] - player_textures[0].get_size()[1]
        jumping = False
    #Clear window #Draw objects until flip()
    window.fill((0,100,255))

    window.blit(player_textures[0], (player_pos[0], player_pos[1]))
    window.blit(ground_textures[0], (0, window_size[1] - ground_textures[0].get_size()[1]))
    window.blit(ground_textures[0], (ground_textures[0].get_size()[0], window_size[1] - ground_textures[0].get_size()[1]))

    #Display all drawed objects
    pygame.display.flip()

    #FPS
    clock.tick(60)
