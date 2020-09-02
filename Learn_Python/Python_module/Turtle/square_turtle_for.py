import turtle
import time
s = turtle.Screen()
s.bgcolor("light blue")
t=turtle.Turtle()
t.pen(pencolor="red", fillcolor="purple", pensize=10, speed=2)
t.begin_fill()
for i in range(0,4):
    t.fd(100)
    t.rt(90)
t.end_fill()
time.sleep(20)