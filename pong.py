import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

display_height = 500
display_width = 700
display = pygame.display.set_mode([display_width, display_height])

class Paddle1:
    width = 25
    height = 75
    x = 0
    y = display_height/2 - height / 2
    speed = 0.25


    def movePaddle(amt):
        Paddle1.y = Paddle1.y + amt

paddle1 = Paddle1

class Paddle2:
    width = 25
    height = 75
    x = display_width - width
    y = display_height/2 - height / 2
    speed = 0.25

    def movePaddle(amt):
        Paddle2.y = Paddle2.y + amt

paddle2 = Paddle2

class Ball:
    radius = 25
    X = display_width / 2
    Y = display_height / 2

ball = Ball


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_DOWN:
        #         movePaddle(paddle2, 25)
        #     elif event.key == pygame.K_UP:
        #         movePaddle(paddle2, -25)
        #     elif event.key == pygame.K_s:
        #         movePaddle(paddle1, 25)
        #     elif event.key == pygame.K_w:
        #         movePaddle(paddle1, -25)


    if pygame.key.get_pressed()[pygame.K_s] and paddle1.y <= display_height - paddle1.height:
        paddle1.movePaddle(paddle1.speed)
    elif pygame.key.get_pressed()[pygame.K_w] and paddle1.y >= 0:
        paddle1.movePaddle(-paddle1.speed)

    if pygame.key.get_pressed()[pygame.K_DOWN] and paddle2.y <= display_height - paddle2.height:
        paddle2.movePaddle(paddle2.speed)
    elif pygame.key.get_pressed()[pygame.K_UP] and paddle2.y >= 0:
        paddle2.movePaddle(-paddle2.speed)



    #                                       Rect(x, y, width, height)
    pygame.draw.rect(display, WHITE, pygame.Rect(paddle1.x, paddle1.y, paddle1.width, paddle1.height))

    #                                       Rect(x, y, width, height)
    pygame.draw.rect(display, WHITE, pygame.Rect(paddle2.x, paddle2.y, paddle2.width, paddle2.height))

    #
    pygame.draw.circle(display, WHITE, (ball.X, ball.Y), ball.radius)




    pygame.display.flip()
    display.fill(BLACK)