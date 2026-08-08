
import turtle
import math
import time

# ==========================================
# HEART BLOOM
# ==========================================

screen = turtle.Screen()
screen.setup(900, 900)
screen.bgcolor("#050008")
screen.title("❤️ Heart Bloom")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

# Bright, warm colors
colors = [
    "#ff1744",   # Red
    "#ff2d55",   # Pink-red
    "#ff4f81",   # Pink
    "#ff6b6b",   # Coral
    "#ff8c42",   # Orange
    "#ffb000",   # Golden
    "#ffd166",   # Yellow
    "#ffffff"    # White highlight
]


# ==========================================
# Mathematical Heart
# ==========================================

def heart_point(angle, scale):
    x = 16 * math.sin(angle) ** 3

    y = (
        13 * math.cos(angle)
        - 5 * math.cos(2 * angle)
        - 2 * math.cos(3 * angle)
        - math.cos(4 * angle)
    )

    return x * scale, y * scale


# ==========================================
# Draw a Heart
# ==========================================

def draw_heart(scale, rotation, color, x_offset=0, y_offset=0):
    points = 100

    t.color(color)
    t.penup()

    for i in range(points + 1):

        angle = (i / points) * math.pi * 2

        # Rotate the heart
        a = angle + rotation

        x, y = heart_point(a, scale)

        x += x_offset
        y += y_offset

        if i == 0:
            t.goto(x, y)
            t.pendown()
        else:
            t.goto(x, y)

    t.penup()


# ==========================================
# Animation
# ==========================================

start_time = time.time()

while True:

    elapsed = time.time() - start_time

    t.clear()

    # --------------------------------------
    # BIG CENTRAL HEART
    # --------------------------------------

    pulse = 1 + 0.08 * math.sin(elapsed * 2.5)

    draw_heart(
        11 * pulse,
        0,
        "#ff1744"
    )

    # --------------------------------------
    # INNER BLOOM
    # --------------------------------------

    for i in range(12):

        angle = (
            i * (2 * math.pi / 12)
            + elapsed * 0.18
        )

        # Slowly breathe in and out
        distance = (
            85
            + 18 * math.sin(elapsed * 1.2 + i * 0.5)
        )

        x = math.cos(angle) * distance
        y = math.sin(angle) * distance

        scale = (
            2.4
            + 0.25 * math.sin(elapsed * 2 + i)
        )

        draw_heart(
            scale,
            angle,
            colors[i % len(colors)],
            x,
            y
        )

    # --------------------------------------
    # OUTER PETALS
    # --------------------------------------

    for i in range(20):

        angle = (
            i * (2 * math.pi / 20)
            - elapsed * 0.10
        )

        distance = (
            175
            + 15 * math.sin(elapsed + i * 0.4)
        )

        x = math.cos(angle) * distance
        y = math.sin(angle) * distance

        scale = (
            1.25
            + 0.15 * math.sin(elapsed * 1.5 + i)
        )

        draw_heart(
            scale,
            angle,
            colors[(i + 3) % len(colors)],
            x,
            y
        )

    # --------------------------------------
    # SMALL FLOATING HEARTS
    # --------------------------------------

    for i in range(16):

        angle = (
            i * (2 * math.pi / 16)
            + elapsed * 0.08
        )

        distance = (
            260
            + 25 * math.sin(elapsed * 0.7 + i)
        )

        x = math.cos(angle) * distance
        y = math.sin(angle) * distance

        scale = 0.55

        draw_heart(
            scale,
            angle,
            colors[(i + 5) % len(colors)],
            x,
            y
        )

    screen.update()

    # Controls animation speed
    time.sleep(0.025)
