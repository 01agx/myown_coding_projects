# Professional Game Example

import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Professional Game Example")

# Game variables
player_pos = [400, 300]
player_size = 50
enemy_size = 50
enemy_pos = [random.randint(0, SCREEN_WIDTH-enemy_size), 0]
enemy_list = [enemy_pos]
score = 0

# Clock
clock = pygame.time.Clock()

# Game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Move the enemy
    if enemy_pos[1] >= 0 and enemy_pos[1] < SCREEN_HEIGHT:
        enemy_pos[1] += 10
    else:
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, SCREEN_WIDTH-enemy_size)
        score += 1

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the player
    pygame.draw.rect(screen, BLACK, (player_pos[0], player_pos[1], player_size, player_size))

    # Draw the enemy
    pygame.draw.rect(screen, BLACK, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

    # Check for collision
    if (player_pos[0] < enemy_pos[0] < player_pos[0] + player_size or player_pos[0] < enemy_pos[0] + enemy_size < player_pos[0] + player_size) and \
       (player_pos[1] < enemy_pos[1] < player_pos[1] + player_size or player_pos[1] < enemy_pos[1] + enemy_size < player_pos[1] + player_size):
        game_over = True

    # Update the display
    pygame.display.update()

    # Frame Per Second
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
