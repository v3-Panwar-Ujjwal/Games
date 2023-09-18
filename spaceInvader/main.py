import pygame
import random
import math
from pathlib import Path
from pygame import mixer

# Initialize the pygame
pygame.init()

# Creates the window/ screen
game_window = pygame.display.set_mode((1600,900))

# Changing the icon and the title
icon = pygame.image.load("images\icons\launch32.png")
pygame.display.set_caption("Space Defender")
pygame.display.set_icon(icon)

# Battleship
battle_ship = pygame.image.load("images\icons\spaceship.png")
battle_ship_x = 800-32
battle_ship_y = 650-32
battle_ship_x_change = 0
battle_ship_y_change = 0

# Enemy
ufo = []
ufo_x = []
ufo_y = []
ufo_x_change = []
ufo_y_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    ufo.append(pygame.image.load("images\icons\cyclops.png"))
    ufo_x.append(random.randint(0,1600-64))
    ufo_y.append(random.randint(0,150-64))
    ufo_x_change.append(6)
    ufo_y_change.append(60)

# Bullet
bullet = pygame.image.load(Path("images/icons/bullet5.png"))
bullet_x = 0
bullet_y = battle_ship_y
bullet_x_change = 0
bullet_y_change = -5
bullet_state = 'ready'

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

# Game over
game_over_text = pygame.font.Font("freesansbold.ttf", 200)

background = pygame.image.load(Path("images/icons/background.jpg"))

# Music
mixer.music.load(Path("game_sounds/background.mp3"))
mixer.music.play(-1)

def show_score(score_value):
    score = font.render("Score : {}".format(score_value), True, (0,0,0))
    game_window.blit(score, (0,0))    
def render_battleship(x,y):
    """ Render the battleship in the game window"""
    game_window.blit(battle_ship, (x, y))

def render_ufo(i,x,y):
    """ Render the ufo in the game window"""
    game_window.blit(ufo[i], (x, y))

def render_bullet(x,y):
    """ Render the bullet in the game window"""
    game_window.blit(bullet, (x,y))

def is_collision(bullet_x, bullet_y, ufo_x, ufo_y):
    distance = math.sqrt(math.pow(bullet_x-ufo_x, 2)+math.pow(bullet_y-ufo_y, 2))
    if distance <= 40:
        return True
    else:
        return False

def load_bullet(bullet_state, bullet_x, bullet_y):
    render_bullet(bullet_x, bullet_y)
    bullet_state = 'fire'
    return bullet_state


running = True
# Game window loop
while running:
    # Change the background colour of the screen
    game_window.fill((255, 255, 255))

    game_window.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handles the mechanics for the battle_ship
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                battle_ship_x_change = -3
            if event.key == pygame.K_RIGHT:
                battle_ship_x_change = +3
            if event.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bullet_sound = mixer.Sound(Path("game_sounds/bullet_fire.wav"))
                    bullet_sound.play()
                    bullet_x = battle_ship_x + 15
                    bullet_state = load_bullet(bullet_state, bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            battle_ship_x_change = 0

    if bullet_state is 'fire':
        bullet_y += bullet_y_change
        render_bullet(bullet_x, bullet_y)
    if bullet_y <=0:
        bullet_state = 'ready'
        bullet_y = battle_ship_y

    for i in range(num_of_enemies):
        if ufo_y[i] >= battle_ship_y-64:
            game_over = font.render("GAME OVER",True, (255,255,255))
            game_window.blit(game_over, (700, 500))
            for j in range(num_of_enemies):
                ufo_y[j] = 2000
        if is_collision(bullet_x, bullet_y, ufo_x[i], ufo_y[i]):
            explosion_sound = mixer.Sound(Path("game_sounds\destoyed.wav"))
            explosion_sound.play()
            ufo_x[i] = random.randint(0,1600-64)
            ufo_y[i] = random.randint(0,150-64)
            bullet_state = 'ready'
            bullet_y = battle_ship_y
            score_value += 1
            break
        if ufo_x[i] <=0:
            ufo_x[i] = 0
            ufo_x_change[i] = 3
            ufo_y[i] += ufo_y_change[i]
        elif ufo_x[i] >= (1600-64):
            ufo_x[i] = 1600 - 64
            ufo_x_change[i] = -3
            ufo_y[i] += ufo_y_change[i]
        ufo_x[i] += ufo_x_change[i] 
        render_ufo(i,ufo_x[i], ufo_y[i])

    battle_ship_x += battle_ship_x_change  
    if battle_ship_x <=0:
        battle_ship_x = 0
    elif battle_ship_x >= (1600-64):
        battle_ship_x = 1600 - 64

    
    render_battleship(battle_ship_x, battle_ship_y)
    show_score(score_value)
    # Update the changes in the window
    pygame.display.update()


# Thanks for the image for background Image by <a href="https://www.freepik.com/free-photo/flat-lay-assortment-creative-paper-planets_12781150.htm#query=colorful%20spaceship%20background%201600%20900&position=4&from_view=search&track=ais">Freepik</a>