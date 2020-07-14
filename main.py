import pygame
from pygame import mixer
import random
import math
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

# Initialize the game
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Wars")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Background
background = pygame.image.load("background.jpg")

# Background music
mixer.music.load("background.wav")
mixer.music.play(-1)

# Player
playerImg = pygame.image.load("spaceshipImage.png")
playerX = 368
playerY = 490
playerX_change = 0
playerY_change = 0

# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 368
bulletY = 490
bulletX_change = 0
bulletY_change = 4
bullet_state = "ready"

# Enemies
enemy1Img = pygame.image.load("enemy1.png")
enemy1X = random.randint(0, 736)
enemy1Y = random.randint(-50, 50)
enemy1Y_change = 0.35

enemy2Img = pygame.image.load("enemy2.png")
enemy2X = random.randint(0, 736)
enemy2Y = random.randint(-50, 50)
enemy2Y_change = 0.5

enemy3Img = pygame.image.load("enemy3.png")
enemy3X = random.randint(0, 736)
enemy3Y = random.randint(-50, 50)
enemy3Y_change = 0.45

enemy4Img = []
enemy4X = []
enemy4Y = []
enemy4Y_change = []
num_of_enemies4 = 2

for i in range(num_of_enemies4):
    enemy4Img.append(pygame.image.load("enemy4.png"))
    enemy4X.append(random.randint(0, 736))
    enemy4Y.append(random.randint(-50, 50))
    enemy4Y_change.append(0.4)

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
scoreX = 10
scoreY = 10

# Game Over
font2 = pygame.font.Font("freesansbold.ttf", 64)


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    game_over = font2.render("GAME OVER!", True, (255, 0, 0))
    screen.blit(game_over, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 20))


def isCollision1(enemy1X, enemy1Y, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemy1X - bulletX, 2) + math.pow(enemy1Y - bulletY, 2))
    if distance < 28:
        return True
    else:
        return False


def isCollision2(enemy2X, enemy2Y, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemy2X - bulletX, 2) + math.pow(enemy2Y - bulletY, 2))
    if distance < 28:
        return True
    else:
        return False


def isCollision3(enemy3X, enemy3Y, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemy3X - bulletX, 2) + math.pow(enemy3Y - bulletY, 2))
    if distance < 28:
        return True
    else:
        return False


def isCollision4(enemy4X, enemy4Y, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemy4X - bulletX, 2) + math.pow(enemy4Y - bulletY, 2))
    if distance < 28:
        return True
    else:
        return False


def enemy1(x, y):
    screen.blit(enemy1Img, (x, y))


def enemy2(x, y):
    screen.blit(enemy2Img, (x, y))


def enemy3(x, y):
    screen.blit(enemy3Img, (x, y))


def enemy4(x, y, i):
    screen.blit(enemy4Img[i], (x, y))


# Game Loop
running = True
while running:
    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))

    # Background
    screen.blit(background, (0, 0))

    # Quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If key is pressed check what key it is and do the action
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2.3
            if event.key == pygame.K_RIGHT:
                playerX_change = +2.3
            if event.key == pygame.K_UP:
                playerY_change = -1
            if event.key == pygame.K_DOWN:
                playerY_change = +1
            if event.key == pygame.K_SPACE:
                # Shoot the bullet ONLY when is in state ready
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    # Get the x coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    # Player movement
    playerX += playerX_change
    playerY += playerY_change

    # Enemy movement and collisions

    # All the enemies are appearing only once while
    # Enemy4 is appearing twice ;)

    # Game over
    for i in range(1):
        if enemy1Y > 420:
            enemy1Y = 1000
            enemy2Y = 1000
            enemy3Y = 1000
            for j in range(num_of_enemies4):
                enemy4Y[j] = 1000
            game_over_text()
            game_over_sound = mixer.Sound("gameover.wav")
            game_over_sound.play(1)
            break

    enemy1Y += enemy1Y_change  # enemy1 movement
    collision1 = isCollision1(enemy1X, enemy1Y, bulletX, bulletY)
    if collision1:
        explosion_sound = mixer.Sound("explosion.wav")
        explosion_sound.play()
        bulletY = 490
        bullet_state = "ready"
        score_value += 5
        enemy1X = random.randint(0, 736)
        enemy1Y = random.randint(-50, 50)
    enemy1(enemy1X, enemy1Y)

    for i in range(1):
        if enemy2Y > 420:
            enemy1Y = 1000
            enemy2Y = 1000
            enemy3Y = 1000
            for j in range(num_of_enemies4):
                enemy4Y[j] = 1000
            game_over_text()
            break

    enemy2Y += enemy2Y_change  # enemy2 movement
    collision2 = isCollision2(enemy2X, enemy2Y, bulletX, bulletY)
    if collision2:
        bulletY = 490
        bullet_state = "ready"
        score_value += 5
        enemy2X = random.randint(0, 736)
        enemy2Y = random.randint(-50, 50)
    enemy2(enemy2X, enemy2Y)

    for i in range(1):
        if enemy3Y > 420:
            enemy1Y = 1000
            enemy2Y = 1000
            enemy3Y = 1000
            for j in range(num_of_enemies4):
                enemy4Y[j] = 1000
            game_over_text()
            break

    enemy3Y += enemy3Y_change  # enemy3 movement
    collision3 = isCollision3(enemy3X, enemy3Y, bulletX, bulletY)
    if collision3:
        bulletY = 490
        bullet_state = "ready"
        score_value += 5
        enemy3X = random.randint(0, 736)
        enemy3Y = random.randint(-50, 50)
    enemy3(enemy3X, enemy3Y)

    # Enemy4 is appearing twice! We use a for loop on that
    for i in range(num_of_enemies4):
        if enemy4Y[i] > 420:
            enemy1Y = 1000
            enemy2Y = 1000
            enemy3Y = 1000
            for j in range(num_of_enemies4):
                enemy4Y[j] = 1000
            game_over_text()
            break

        enemy4Y[i] += enemy4Y_change[i]  # enemy4 movement
        collision4 = isCollision4(enemy4X[i], enemy4Y[i], bulletX, bulletY)
        if collision4:
            bulletY = 490
            bullet_state = "ready"
            score_value += 5
            enemy4X[i] = random.randint(0, 736)
            enemy4Y[i] = random.randint(-50, 50)
        enemy4(enemy4X[i], enemy4Y[i], i)

    # Boundaries
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    elif playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    # Bullet movement
    if bulletY <= -40:
        bullet_state = "ready"
        bulletY = 490
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Player appearing on screen
    player(playerX, playerY)

    # Score appearing on screen
    show_score(scoreX, scoreY)

    # Updating every event that is occurring on the screen
    pygame.display.update()
