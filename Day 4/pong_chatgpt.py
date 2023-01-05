import pygame, sys

# Initialize pygame
pygame.init()

# Set the window size
window_size = (600, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the window title
pygame.display.set_caption("Pong")

# Create the game objects
ball = pygame.Rect(300, 200, 20, 20)
paddle1 = pygame.Rect(10, 150, 20, 100)
paddle2 = pygame.Rect(570, 150, 20, 100)

# Set the ball's velocity
velocity = [2, 2]

# Create a font object
font = pygame.font.Font(None, 36)

# Set the initial scores
score1 = 0
score2 = 0

# Create a game loop
while True:
    
    # Handle user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddles with the arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddle2.y = max(0, paddle2.y - 3)
    if keys[pygame.K_DOWN]:
        paddle2.y = min(300, paddle2.y + 3)
    if keys[pygame.K_w]:
        paddle1.y = max(0, paddle1.y - 3)
    if keys[pygame.K_s]:
        paddle1.y = min(300, paddle1.y + 3)
    # Move the ball
    ball.x += velocity[0]
    ball.y += velocity[1]

    # Check for ball collision with paddles or edges
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        velocity[0] = -velocity[0]
    if ball.y < 0 or ball.y > 380:
        velocity[1] = -velocity[1]

    # Check for ball out of bounds and update scores
    if ball.x < 0:
        score2 += 1
        ball.x, ball.y = 300, 200
    if ball.x > 580:
        score1 += 1
        ball.x, ball.y = 300, 200

    #clear the screen
    screen.fill((0,0,0))

    # Draw the ball and paddles
    pygame.draw.rect(screen, (255, 255, 255), ball)
    pygame.draw.rect(screen, (255, 255, 255), paddle1)
    pygame.draw.rect(screen, (255, 255, 255), paddle2)

    # Display the scores
    score_text1 = font.render(str(score1), True, (255, 255, 255))
    score_text2 = font.render(str(score2), True, (255, 255, 255))
    screen.blit(score_text1, (200, 10))
    screen.blit(score_text2, (400, 10))

    # Update the display
    pygame.display.flip()
    

    # Control the frame rate
    clock = pygame.time.Clock()
    clock.tick(60)
