from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
import pygame
import os

# Initialize Pygame
pygame.init()

# Load sound files
bounce_sound = pygame.mixer.Sound(os.path.join("sounds", "bounce.wav"))


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    # detect if ball hits top or bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        bounce_sound.play()

    # detect collision with right paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (
        ball.distance(l_paddle) < 50 and ball.xcor() < -340
    ):
        ball.bounce_x()
        bounce_sound.play()

    # detect if ball hits the wall on the right or left and adjust the score
    if ball.xcor() > 380 or ball.xcor() < -380:
        pass

screen.exitonclick()
