import pygame
import sys
import random
import time
import os
from PIL import Image

# Paths
ASSETS_DIR = './PacJumper-2.1-2022/all_assets'

# if we want to load file we need to use: (os.path.join(ASSETS_DIR, 'the file'))

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1534
SCREEN_HEIGHT = 800
GRAVITY = 0.10
PLAYER_JUMP_STRENGTH = 3
OBSTACLE_SPAWN_SPEED = 1000
GAME_SPEED = 250
OBSTACLE_HEIGHTS = [0,50,100,150,200,250,300,350,400,450,500,550,600,650,700,750,800]
SPAWN_OBSTACLE = pygame.USEREVENT
pygame.time.set_timer(SPAWN_OBSTACLE,OBSTACLE_SPAWN_SPEED)
player_movement = 0

 

# Function to load assets
def load_assets():
    bg_image = pygame.image.load(os.path.join(ASSETS_DIR, 'background.png')).convert()
    bg_image = pygame.transform.scale2x(bg_image)
    
    player_image = pygame.image.load(os.path.join(ASSETS_DIR, 'pacman.png')).convert_alpha()
    
    obstacle_image = pygame.image.load(os.path.join(ASSETS_DIR, 'Red_ghost.png')).convert_alpha()
    obstacle_image = pygame.transform.scale2x(obstacle_image)
    
    secret_code_image = pygame.image.load(os.path.join(ASSETS_DIR, 'you_win.png')).convert_alpha()
    
    game_over_image = pygame.transform.scale2x(pygame.image.load(os.path.join(ASSETS_DIR, 'Game_over.png')).convert_alpha())
    return bg_image, player_image, obstacle_image, secret_code_image, game_over_image

# Function to draw the background image
def draw_background_image(screen, bg_image, bg_x_pos, bg_y_pos):
    screen.blit(bg_image, (bg_x_pos, bg_y_pos))
    screen.blit(bg_image, (bg_x_pos + SCREEN_WIDTH, bg_y_pos))

# Function to create an obstacle
def create_obstacle(obstacle_surface):
    random_obstacle_pos = random.choice(OBSTACLE_HEIGHTS)
    new_obstacle = obstacle_surface.get_rect(midtop=(SCREEN_WIDTH, random_obstacle_pos))
    return new_obstacle

# Function to move obstacles
def move_obstacles(obstacles):
    for obstacle in obstacles:
        obstacle.centerx -= 2
    return obstacles

# Function to draw obstacles
def draw_obstacles(screen, obstacle_surface, obstacles):
    for obstacle in obstacles:
        screen.blit(obstacle_surface, obstacle)

# Function to check for collisions
def check_collision(player_rect, obstacles):
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            pygame.mixer.Sound.play(player_death)
            return False
    if player_rect.top <= -200 or player_rect.bottom >= 1000:
        pygame.mixer.Sound.play(player_death)
        return False
    return True

# Function to display the score
def score_display(screen, game_font, score, game_state):
    if game_state == 'game_main':
        score_surface = game_font.render(str(int(score)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))
        screen.blit(score_surface, score_rect)
    if game_state == 'game_over':
        score_surface = game_font.render(f'Score:{int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))
        screen.blit(score_surface, score_rect)

# Function to play the congratulation sound
def play_congratulation():
    pygame.mixer.Sound.play(congratulation)

# Function to display the secret password and related information
def secret_password(screen, secret_code, secret_code_image):
    if secret_code == 121:
        screen.blit(secret_code_image, (SCREEN_WIDTH // 2 - secret_code_image.get_width() // 2, 220))
        play_congratulation()
        current_time()

# Function to display the current time
def current_time():
    current_time_1 = time.strftime("%d/%m/%Y %H:%M:%S")
    time_surface = game_font.render(f'You won in {current_time_1} time', True, (255, 0, 0))
    time_rect = time_surface.get_rect(center=(SCREEN_WIDTH // 2, 90))
    screen.blit(time_surface, time_rect)

# Function to quit the game
def quit_game(game_exit):
    if game_exit >= 2:
        pygame.quit()
        sys.exit()



# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Load assets
bg_image, player_image, obstacle_image, secret_code_image, game_over_image = load_assets()

# Fonts
game_font = pygame.font.Font(os.path.join(ASSETS_DIR, 'Font1.ttf'), 40)

# Lists
obstacle_list = []

# Initial game variables
player_rect = player_image.get_rect(center=(100, 295))
bg_x_pos = 0
bg_y_pos = 0
score = 0
game_active = True
secret_code = 0
game_exit = 0

# Load sounds
player_death = pygame.mixer.Sound(os.path.join(ASSETS_DIR, 'Roblox Death Sound Effect.mp3'))
congratulation = pygame.mixer.Sound(os.path.join(ASSETS_DIR, 'Congratulations-sound-effect.mp3'))

# Load songs
bg_music1 = pygame.mixer.Sound(os.path.join(ASSETS_DIR, '1.mp3'))
bg_music2 = pygame.mixer.Sound(os.path.join(ASSETS_DIR, '2.mp3'))
bg_music3 = pygame.mixer.Sound(os.path.join(ASSETS_DIR, '3.mp3'))
bg_music4 = pygame.mixer.Sound(os.path.join(ASSETS_DIR, '4.mp3'))
bg_music5 = pygame.mixer.Sound(os.path.join(ASSETS_DIR, '5.mp3'))
bg_music6 = pygame.mixer.Sound(os.path.join(ASSETS_DIR, '6.mp3'))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT:
                pygame.mixer.stop()

            if event.key == pygame.K_ESCAPE:
                game_exit += 1

            if event.key == pygame.K_F1:
                bg_music1.stop()
                bg_music2.stop()
                bg_music3.stop()
                bg_music4.stop()
                bg_music5.stop()
                bg_music6.stop()
                pygame.mixer.Sound.play(bg_music1)
            if event.key == pygame.K_F2:
                bg_music1.stop()
                bg_music2.stop()
                bg_music3.stop()
                bg_music4.stop()
                bg_music5.stop()
                bg_music6.stop()
                pygame.mixer.Sound.play(bg_music2)
            if event.key == pygame.K_F3:
                bg_music1.stop()
                bg_music2.stop()
                bg_music3.stop()
                bg_music4.stop()
                bg_music5.stop()
                bg_music6.stop()
                pygame.mixer.Sound.play(bg_music3)
            if event.key == pygame.K_F4:
                bg_music1.stop()
                bg_music2.stop()
                bg_music3.stop()
                bg_music4.stop()
                bg_music5.stop()
                bg_music6.stop()
                pygame.mixer.Sound.play(bg_music4)
            if event.key == pygame.K_F5:
                bg_music1.stop()
                bg_music2.stop()
                bg_music3.stop()
                bg_music4.stop()
                bg_music5.stop()
                bg_music6.stop()
                pygame.mixer.Sound.play(bg_music5)
            if event.key == pygame.K_F6:
                bg_music1.stop()
                bg_music2.stop()
                bg_music3.stop()
                bg_music4.stop()
                bg_music5.stop()
                bg_music6.stop()
                pygame.mixer.Sound.play(bg_music6)

            if event.key == pygame.K_1:
                secret_code += 1
            if event.key == pygame.K_2:
                secret_code += 2
            if event.key == pygame.K_3:
                secret_code += 3
            if event.key == pygame.K_4:
                secret_code += 4
            if event.key == pygame.K_5:
                secret_code += 5
            if event.key == pygame.K_6:
                secret_code += 6
            if event.key == pygame.K_7:
                secret_code += 7
            if event.key == pygame.K_8:
                secret_code += 8
            if event.key == pygame.K_9:
                secret_code += 9
            if event.key == pygame.K_0:
                secret_code += 0
            if event.key == pygame.K_DELETE:
                secret_code = 0

            if event.key == pygame.K_SPACE and game_active:
                player_movement = 0
                player_movement -= PLAYER_JUMP_STRENGTH

            if event.key == pygame.K_RETURN and not game_active:
                game_active = True
                obstacle_list.clear()
                score = 0
                player_rect.center = (100, 295)
                player_movement = 0
                obstacle_spawn_speed = 1200
                game_speed = 300

        if event.type == SPAWN_OBSTACLE and game_active:
            obstacle_list.append(create_obstacle(obstacle_image))

    draw_background_image(screen, bg_image, bg_x_pos, bg_y_pos)
    if bg_x_pos <= -1534:
        bg_x_pos = 0
    bg_x_pos -= 1

    if game_active:
        player_movement += GRAVITY
        player_rect.centery += player_movement
        screen.blit(player_image, player_rect)
        game_active = check_collision(player_rect, obstacle_list)

        obstacle_list = move_obstacles(obstacle_list)
        draw_obstacles(screen, obstacle_image, obstacle_list)

        score_display(screen, game_font, score, 'game_main')
        score += 0.01
    else:
        screen.blit(game_over_image, game_over_image.get_rect(center=(SCREEN_WIDTH // 2, 220)))
        score_display(screen, game_font, score, 'game_over')

    secret_password(screen, secret_code, secret_code_image)
    quit_game(game_exit)

    pygame.display.update()
    clock.tick(GAME_SPEED)
#winner_score
