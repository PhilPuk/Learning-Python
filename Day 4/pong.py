from turtle import Vec2D
import pygame, sys
from pygame.math import Vector2
#Init pygame
pygame.init()

#Init window and it's variables
window_size = Vector2(800,600)
screen = pygame.display.set_mode(window_size)

# Set the window title
pygame.display.set_caption("Pong")

# Create a font object
font = pygame.font.Font(None, 36)

#Game variables
velocity = Vector2(2.5,2.5)
scores = [0,0]

#Init game object
paddle_size = Vector2(20,150)
paddles = [pygame.Rect(10,window_size[1] / 2 - paddle_size[1] / 2, paddle_size[0],paddle_size[1]), pygame.Rect(window_size[0] - paddle_size[0] - 10,window_size[1] / 2 - paddle_size[1] / 2, paddle_size[0],paddle_size[1])]
ball = pygame.Rect(window_size.x / 2 - 10, window_size.y / 2 - 10, 20, 20)

#Game loop
while True:
    #User Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #Paddle Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddles[1].y = max(0, paddles[1].y - 3)
    if keys[pygame.K_DOWN]:
        paddles[1].y = min(window_size[1] - paddle_size[1], paddles[1].y + 3)
    if keys[pygame.K_w]:
        paddles[0].y = max(0, paddles[0].y - 3)
    if keys[pygame.K_s]:
        paddles[0].y = min(window_size[1] - paddle_size[1], paddles[0].y + 3)
    
    #Ball Movement
    ball.x += velocity[0]
    ball.y -= velocity[1]

    #Collision Ball - Paddles - Edges
    if ball.colliderect(paddles[0]) or ball.colliderect(paddles[1]):
        velocity[0] = -velocity[0]
    if ball.y < 0 or ball.y > window_size[1] - ball.size[1]:
        velocity[1] = -velocity[1]

    #Collision with walls
    if ball.x < 0:
        scores[0] += 1
        ball.x = window_size[0] / 2 - 10
        ball.y = window_size[1] / 2 - 10
    if ball.x > window_size[0] - paddle_size[0]:
        scores[1] += 1
        ball.x = window_size[0] / 2 - 10
        ball.y = window_size[1] / 2 - 10

    #Clear window
    screen.fill((0,0,0))

    #Draw game object
    for i in range(2):
        pygame.draw.rect(screen, (255, 255, 255), paddles[i])
    pygame.draw.rect(screen, (255, 255, 255), ball)

    # Display the scores
    score_text1 = font.render(str(scores[1]), True, (255, 255, 255))
    score_text2 = font.render(str(scores[0]), True, (255, 255, 255))
    screen.blit(score_text1, (window_size[0] / 4, 10))
    screen.blit(score_text2, (window_size[0] * 0.66, 10))

    #Display all drawed objects
    pygame.display.flip()

    #FPS controlling
    clock = pygame.time.Clock()
    clock.tick(60)