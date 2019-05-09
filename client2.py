import socket
import struct
from os.path import sep

import pygame
from random import randint

# Define Colors - RGB
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 500))

s.send(str.encode("CanIStart"))

while True:
    data = s.recv(2048)
    reply = data.decode('utf-8')
    if reply == "Start":
        pygame.init()
        break

# Screen Size
size = 700, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Bird in Python by @KartikKannapur")

done = False
clock = pygame.time.Clock()


def ball(x, y):
    # Radius of 20 px
    pygame.draw.circle(screen, black, [x, y], 20)


def gameover():
    font = pygame.font.SysFont(None, 55)
    text = font.render("Game Over! Try Again", True, red)
    screen.blit(text, [150, 250])



def obstacle(xloc, yloc, xsize, ysize):
    pygame.draw.rect(screen, green, [xloc, yloc, xsize, ysize])
    pygame.draw.rect(screen, green, [xloc, int(yloc + ysize + space), xsize, ysize + 500])


# If the ball is between 2 points on the screen, increment score
def Score(score):
    font = pygame.font.SysFont(None, 55)
    text = font.render("Score: " + str(score), True, black)
    screen.blit(text, [0, 0])

def Score2(score2):
    font = pygame.font.SysFont(None, 55)
    text = font.render("Score2: " + str(score2), True, black)
    screen.blit(text, [200, 0])



x = 350
y = 250
x_speed = 0
y_speed = 0
ground = 477
xloc = 700
yloc = 0
xsize = 70
ysize = randint(0, 350)
# Size of space between 2 blocks
space = 150
obspeed = 2
score = 0
score2 = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                y_speed = -10

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                y_speed = 5

    screen.fill(white)
    obstacle(xloc, yloc, xsize, ysize)
    ball(x, y)
    Score(score)

    Score2(score2)

    y += y_speed
    xloc -= obspeed

    if y > ground:
        gameover()
        y_speed = 0
        obspeed = 0

    if x + 20 > xloc and y - 20 < ysize and x - 15 < xsize + xloc:
        gameover()
        y_speed = 0
        obspeed = 0

    if x + 20 > xloc and y + 20 < ysize and x - 15 < xsize + xloc:
        gameover()
        y_speed = 0
        obspeed = 0

    if xloc < -80:
        xloc = 700
        ysize = randint(0, 350)

    if x > xloc and x < xloc + 3:
        score = score + 1


    pygame.display.flip()
    clock.tick(60)

pygame.quit()