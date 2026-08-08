
import math
import turtle
import time

# -----------------------------------
# Screen setup
# -----------------------------------
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Glowing Mathematical Heart")
screen.tracer(0)

# -----------------------------------
# Turtle setup
# -----------------------------------
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# -----------------------------------
# Heart equation
# -----------------------------------
def heart_x(t):
    return 15 * math.sin(t) ** 3


def heart_y(t):
    return (
        12 * math.cos(t)
        - 5 * math.cos(2 * t)
        - 2 * math.cos(3 * t)
        - math.cos(4 * t)
    )


# -----------------------------------
# Draw the heart slowly
# -----------------------------------
points = []

total_points = 500

for i in range(total_points):
    angle = (2 * math.pi * i) / total_points

    x = heart_x(angle) * 20
    y = heart_y(angle) * 20

    points.append((x, y))

# -----------------------------------
# Glowing colors
# -----------------------------------
glow_colors = [
    "#3b0015",
    "#660022",
    "#990033",
    "#cc0044",
    "#ff0066",
    "#ff3385",
    "#ff6699",
]

# -----------------------------------
# Draw glow layers
# -----------------------------------
for glow_width, glow_color in [
    (10, glow_colors[0]),
    (8, glow_colors[1]),
    (6, glow_colors[2]),
    (4, glow_colors[3]),
]:

    glow = turtle.Turtle()
    glow.hideturtle()
    glow.speed(0)
    glow.penup()
    glow.pensize(glow_width)
    glow.color(glow_color)

    for i, (x, y) in enumerate(points):

        if i == 0:
            glow.goto(x, y)
            glow.pendown()
        else:
            glow.goto(x, y)

        # Slow drawing effect
        if i % 5 == 0:
            screen.update()
            time.sleep(0.005)

    glow.penup()


# -----------------------------------
# Main bright heart
# -----------------------------------
t.pensize(2)
t.color("#ff4d88")

for i, (x, y) in enumerate(points):

    if i == 0:
        t.goto(x, y)
        t.pendown()
    else:
        t.goto(x, y)

    # Slowly reveal the heart
    if i % 4 == 0:
        screen.update()
        time.sleep(0.01)

t.penup()


# -----------------------------------
# Pulsing effect
# -----------------------------------
pulse = 0

while True:

    pulse += 0.08

    # Smooth pulse between 1 and 1.12
    scale = 1 + 0.06 * math.sin(pulse)

    t.clear()
    t.pensize(2)

    # Slightly changing pink shade
    brightness = int(100 + 80 * (math.sin(pulse) + 1) / 2)

    red = 255
    green = max(0, 80 - int(30 * math.sin(pulse)))
    blue = brightness

    color = f"#{red:02x}{green:02x}{blue:02x}"
    t.color(color)

    for i, (x, y) in enumerate(points):

        px = x * scale
        py = y * scale

        if i == 0:
            t.goto(px, py)
            t.pendown()
        else:
            t.goto(px, py)

    t.penup()

    screen.update()
    time.sleep(0.03)
    
