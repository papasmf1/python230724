import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 7
BLOCK_WIDTH, BLOCK_HEIGHT = 80, 30
BLOCK_ROWS, BLOCK_COLS = 5, 8
PADDLE_WIDTH, PADDLE_HEIGHT = 150, 20
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Breaker")

# Create the ball
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_speed_x = random.choice([-BALL_SPEED, BALL_SPEED])
ball_speed_y = -BALL_SPEED

# Create the paddle
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create blocks
blocks = []
for row in range(BLOCK_ROWS):
    for col in range(BLOCK_COLS):
        block = pygame.Rect(col * BLOCK_WIDTH, row * BLOCK_HEIGHT + 50, BLOCK_WIDTH, BLOCK_HEIGHT)
        blocks.append(block)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= PADDLE_SPEED
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.right += PADDLE_SPEED

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collisions
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x = -ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y

    # Paddle collision
    if ball.colliderect(paddle) and ball_speed_y > 0:
        ball_speed_y = -ball_speed_y

    # Block collisions
    for block in blocks[:]:
        if ball.colliderect(block):
            blocks.remove(block)
            ball_speed_y = -ball_speed_y

    # Check if the ball is below the paddle
    if ball.top >= HEIGHT:
        # Game over
        pygame.quit()
        sys.exit()

    # Clear the window
    window.fill(WHITE)

    # Draw the blocks
    for block in blocks:
        pygame.draw.rect(window, GREEN, block)

    # Draw the paddle
    pygame.draw.rect(window, RED, paddle)

    # Draw the ball
    pygame.draw.ellipse(window, RED, ball)

    # Update the display
    pygame.display.update()

    # Set the frame rate
    pygame.time.Clock().tick(60)
