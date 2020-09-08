from turtle import Screen, Turtle
from random import randint, choice
import turtle
import time
s=Screen()
s.bgcolor("white")
track = Turtle()
# track = turtle.Turtle()
track.speed('fastest')
track.penup()
track.goto(-100, 200)
for step in range(15):
    track.write(step, align='center')
    track.right(90)
    track.forward(10)
    track.pendown()
    track.forward(160)
    track.penup()
    track.backward(170)
    track.left(90)
    track.forward(20)

#

track.goto(200, 250)
track.write("Finish Line", align='center')
track.pendown()
track.right(90)
track.forward(300)
time.sleep(10)