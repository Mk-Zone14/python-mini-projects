import turtle
import random

# ------------------------
# Screen
# ------------------------
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Bouncing Ball")
screen.tracer(0)

# ------------------------
# Ball
# ------------------------
ball = turtle.Turtle()
ball.shape("circle")
ball.color("cyan")
ball.penup()
ball.shapesize(2)

# Initial position
ball.goto(0, 220)

# Velocity
dx = 3
dy = 0

gravity = -0.30
bounce = 0.90

colors = [
    "red",
    "orange",
    "yellow",
    "lime",
    "cyan",
    "blue",
    "magenta",
    "white",
    "pink"
]

# ------------------------
# Animation loop
# ------------------------
while True:

    x = ball.xcor()
    y = ball.ycor()

    # Apply gravity
    dy += gravity

    x += dx
    y += dy

    # Floor collision
    if y < -260:
        y = -260
        dy *= -bounce
        ball.color(random.choice(colors))

    # Ceiling collision
    if y > 260:
        y = 260
        dy *= -1

    # Side walls
    if x > 380:
        x = 380
        dx *= -1
        ball.color(random.choice(colors))

    if x < -380:
        x = -380
        dx *= -1
        ball.color(random.choice(colors))

    ball.goto(x, y)

    screen.update()