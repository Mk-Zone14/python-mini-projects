import turtle
import random

# ----------------------------
# Screen Setup
# ----------------------------
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Kaleidoscope Bounce")

screen.tracer(0)

# ----------------------------
# Drawing Turtle
# ----------------------------
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()
pen.penup()

colors = [
    "#ff4d6d",
    "#ffbe0b",
    "#8ac926",
    "#00f5d4",
    "#4cc9f0",
    "#4361ee",
    "#7209b7",
    "#f72585",
    "white"
]

# ----------------------------
# Ball
# ----------------------------
x = 0
y = 0

dx = 3.2
dy = 2.4

limit = 350

# ----------------------------
# Animation
# ----------------------------
while True:

    x += dx
    y += dy

    if x > limit or x < -limit:
        dx *= -1

    if y > limit or y < -limit:
        dy *= -1

    color = random.choice(colors)
    pen.color(color)

    points = [
        ( x,  y),
        (-x,  y),
        ( x, -y),
        (-x, -y),
        ( y,  x),
        (-y,  x),
        ( y, -x),
        (-y, -x)
    ]

    for px, py in points:
        pen.goto(px, py)
        pen.dot(8)

    screen.update()