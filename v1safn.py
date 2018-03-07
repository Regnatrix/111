#Sandra Dögg Kristmundsdóttir
#03.02.2018
import pygame, sys, time, random
from pygame.locals import *

# Set up pygame.
pygame.init ()
mainClock = pygame.time.Clock ()

# Set up the window.
WINDOWWIDTH = 800
WINDOWHEIGHT = 700
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption ('Safnarinn')
myfont = pygame.font.SysFont("monospace", 40)

# Set up the colors.
WHITE = (255, 255, 255)


# Set up the player.
player = pygame.Rect(400, 500, 100, 100)
playerImage = pygame.image.load('spesball.png')
playerStretchedImage = pygame.transform.scale(playerImage, (100, 100))

# Set up the Eye
Eye = pygame.Rect(300, -20, 40, 40)
EyeImage = pygame.image.load('Eye.png')
EyeStretchedImage = pygame.transform.scale(EyeImage, (40, 40))
# Set up the missed line
missed = pygame.Rect(0, 600, 1000, 70)
missedimage = pygame.image.load('red-line.png')
missedStretchedImage = pygame.transform.scale(missedimage, (0, 1000))

score = 0
score1 = 0
maxEye = 100
highScore = maxEye

Eyes = []
for i in range(0, maxEye):
    x = random.randrange(0, 800)
    y = random.randrange(-700, 100)
    Eyes.append(pygame.Rect(x, y, 20, 20))


# Set up keyboard variables.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6

# Set up the music.
pygame.mixer.music.load("bobomb.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Run the game loop.
while True:
    # Check for the QUIT event.
    for event in pygame.event.get ():
        if event.type == QUIT:
            pygame.quit ()
            sys.exit ()
        if event.type == KEYDOWN:
            # Change the keyboard variables.
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True

        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit ()
                sys.exit ()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False

            if event.key == K_x:
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)
            if event.key == K_m:
                if musicPlaying:
                    pygame.mixer.music.stop()
                else:
                    pygame.mixer.music.play(-1, 0.0)
                musicPlaying = not musicPlaying

    # Draw the background onto the surface.
    background = pygame.image.load('nebula.png').convert()
    background = pygame.transform.scale( background, (1280, 720))
    rect = background.get_rect()
    windowSurface.blit(background, rect)

    # Move the player.
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED


        # Process each Eye in the list
    for i in range(len(Eyes)):

        # Draw the Eye
        windowSurface.blit(EyeStretchedImage, Eye)

        #  Make Eye fall.
        Eyes[i][1] += 2


    # Draw the player onto the surface.
    windowSurface.blit(playerStretchedImage, player)

    # Check whether the player has intersected with any Eyes.
    for Eye in Eyes[:]:
        if player.colliderect(Eye):
            Eyes.remove(Eye)
            maxEye -= 1
            score += 1
            finalScore = score
            #if musicPlaying:
             #   pickUpSound.play()

    for Eye in Eyes[:]:
        if missed.colliderect(Eye):
            Eyes.remove(Eye)
            maxEye -= 1
            score1 += 1

    # Draw text.
    scoretext = myfont.render("Score {0}".format(score), 1, (255, 0, 0))
    windowSurface.blit(scoretext, (25, 25))
    score1text = myfont.render("Missed {0}".format(score1), 1, (255, 0, 0))
    windowSurface.blit(score1text, (400, 25))

    # Game Over.
    if maxEye == 0:
        gameover = myfont.render( 'GAME OVER YOUR SCORE WAS {0}'.format(finalScore), 1, (255, 0, 0))
        best = myfont.render('BEST POSSIBLE SCORE = {} '.format(highScore), 1, (255, 0, 0))
        windowSurface.blit(gameover, (100, 350) )
        windowSurface.blit(best, (150, 400))
        pygame.display.update()

    # Draw the Eyes.
    for Eye in Eyes:
        windowSurface.blit(EyeStretchedImage, Eye)

    # Draw the window onto the screen.
    pygame.display.update()
    mainClock.tick(30)