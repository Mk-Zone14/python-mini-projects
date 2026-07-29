import turtle
import math
import random

# --------------------
# Screen setup
# --------------------
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Spiral Flower")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(1)

colors = [
    "red",
    "orange",
    "yellow",
    "lime",
    "cyan",
    "blue",
    "magenta",
    "violet",
    "pink",
    "white"
]

# --------------------
# Spiral drawing
# --------------------

for i in range(220):

    angle = i * 0.35
    radius = 2 + i * 0.8

    x = radius * math.cos(angle)
    y = radius * math.sin(angle)

    t.penup()
    t.goto(0, 0)
    t.pendown()

    t.color(random.choice(colors))
    t.goto(x, y)

    # tiny flower at every point
    for _ in range(12):
        t.forward(6)
        t.backward(6)
        t.right(30)

turtle.done()