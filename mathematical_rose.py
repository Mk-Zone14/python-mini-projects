
import turtle
import math
import time

# ============================================================
# 🌹 MATHEMATICAL ROSE
# Elegant Generative Art
# ============================================================

screen = turtle.Screen()
screen.setup(900, 900)
screen.bgcolor("#0B0508")
screen.title("Mathematical Rose")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# ------------------------------------------------------------
# Refined palette
# ------------------------------------------------------------

PETAL_LIGHT = "#FFB3C1"
PETAL_MID = "#E94B6A"
PETAL_DEEP = "#9E1638"
PETAL_DARK = "#5A0A20"

HIGHLIGHT = "#FFD9E0"
CENTER = "#F6C453"


# ------------------------------------------------------------
# Smooth easing
# ------------------------------------------------------------

def ease(x):
    return x * x * (3 - 2 * x)


# ------------------------------------------------------------
# Rotate a point
# ------------------------------------------------------------

def rotate(x, y, angle):
    c = math.cos(angle)
    s = math.sin(angle)

    return (
        x * c - y * s,
        x * s + y * c
    )


# ------------------------------------------------------------
# Petal curve
# ------------------------------------------------------------

def petal_point(t_value, width, length, curl):
    """
    Creates a smooth, tapered petal.

    The curve starts narrow at the center,
    expands toward the middle,
    then curls inward near the tip.
    """

    # Smooth horizontal progression
    x = length * t_value

    # Natural petal expansion
    envelope = math.sin(math.pi * t_value)

    # Slightly fuller lower half
    envelope *= (
        0.78 + 0.22 * t_value
    )

    y = width * envelope

    # Curl toward the tip
    x += curl * math.sin(
        math.pi * t_value
    )

    # Slight downward tip
    y -= (
        12
        * t_value
        * t_value
    )

    return x, y


# ------------------------------------------------------------
# Draw an outlined petal
# ------------------------------------------------------------

def draw_petal(
    width,
    length,
    rotation,
    color,
    progress,
    curl
):

    steps = max(
        8,
        int(75 * progress)
    )

    t.color(color)
    t.pensize(1.5)

    # Left edge
    t.penup()

    for i in range(steps + 1):

        p = i / 75

        x, y = petal_point(
            p,
            width,
            length,
            curl
        )

        x, y = rotate(
            x,
            y,
            rotation
        )

        if i == 0:
            t.goto(x, y)
            t.pendown()
        else:
            t.goto(x, y)

    # Right edge
    for i in range(steps, -1, -1):

        p = i / 75

        x, y = petal_point(
            p,
            -width,
            length,
            curl
        )

        x, y = rotate(
            x,
            y,
            rotation
        )

        t.goto(x, y)

    t.penup()


# ------------------------------------------------------------
# Petal vein
# ------------------------------------------------------------

def draw_vein(
    width,
    length,
    rotation,
    progress
):

    steps = max(
        5,
        int(35 * progress)
    )

    t.color("#FF8097")
    t.pensize(1)

    t.penup()

    for i in range(steps + 1):

        p = i / 35

        x = (
            length
            * 0.82
            * p
        )

        y = (
            math.sin(math.pi * p)
            * width
            * 0.18
        )

        x, y = rotate(
            x,
            y,
            rotation
        )

        if i == 0:
            t.goto(x, y)
            t.pendown()
        else:
            t.goto(x, y)

    t.penup()


# ------------------------------------------------------------
# Center spiral
# ------------------------------------------------------------

def draw_center(progress):

    t.color(CENTER)
    t.pensize(2)

    steps = int(
        110 * progress
    )

    t.penup()

    for i in range(steps):

        theta = i * 0.34

        radius = (
            1.2
            * math.sqrt(i)
        )

        x = (
            radius
            * math.cos(theta)
        )

        y = (
            radius
            * math.sin(theta)
        )

        if i == 0:
            t.goto(x, y)
            t.pendown()
        else:
            t.goto(x, y)

    t.penup()


# ============================================================
# ANIMATION
# ============================================================

start_time = time.time()

while True:

    elapsed = (
        time.time()
        - start_time
    )

    t.clear()

    # --------------------------------------------------------
    # Repeating bloom cycle
    # --------------------------------------------------------

    cycle = (
        elapsed % 9
    ) / 9

    bloom = ease(
        0.5
        - 0.5
        * math.cos(
            cycle
            * math.pi
            * 2
        )
    )

    bloom = (
        0.30
        + bloom
        * 0.70
    )

    # Very subtle breathing
    breathing = (
        1
        + 0.018
        * math.sin(
            elapsed * 1.3
        )
    )

    bloom *= breathing

    # --------------------------------------------------------
    # OUTER PETALS
    # --------------------------------------------------------

    outer_count = 14

    for i in range(
        outer_count
    ):

        angle = (
            i
            * 2
            * math.pi
            / outer_count
        )

        # Controlled irregularity
        angle += (
            0.025
            * math.sin(i * 2.7)
        )

        length = (
            245
            * bloom
        )

        width = (
            47
            * bloom
        )

        draw_petal(
            width,
            length,
            angle,
            PETAL_DEEP,
            bloom,
            28 * bloom
        )

    # --------------------------------------------------------
    # MIDDLE PETALS
    # --------------------------------------------------------

    middle_count = 11

    for i in range(
        middle_count
    ):

        angle = (
            i
            * 2
            * math.pi
            / middle_count
            + 0.15
        )

        length = (
            190
            * bloom
        )

        width = (
            55
            * bloom
        )

        draw_petal(
            width,
            length,
            angle,
            PETAL_MID,
            bloom,
            23 * bloom
        )

        draw_vein(
            width,
            length,
            angle,
            bloom
        )

    # --------------------------------------------------------
    # INNER PETALS
    # --------------------------------------------------------

    inner_count = 9

    for i in range(
        inner_count
    ):

        angle = (
            i
            * 2
            * math.pi
            / inner_count
            + 0.32
        )

        length = (
            125
            * bloom
        )

        width = (
            58
            * bloom
        )

        draw_petal(
            width,
            length,
            angle,
            PETAL_LIGHT,
            bloom,
            -18 * bloom
        )

    # --------------------------------------------------------
    # INNER CURLS
    # --------------------------------------------------------

    curl_count = 7

    for i in range(
        curl_count
    ):

        angle = (
            i
            * 2
            * math.pi
            / curl_count
        )

        length = (
            78
            * bloom
        )

        width = (
            45
            * bloom
        )

        draw_petal(
            width,
            length,
            angle,
            PETAL_DARK,
            bloom,
            -28 * bloom
        )

    # --------------------------------------------------------
    # CENTER
    # --------------------------------------------------------

    if bloom > 0.55:

        center_progress = (
            bloom - 0.55
        ) / 0.45

        draw_center(
            center_progress
        )

    # --------------------------------------------------------
    # Tiny highlight
    # --------------------------------------------------------

    if bloom > 0.75:

        t.color(HIGHLIGHT)
        t.penup()

        glow = (
            4
            + 2
            * math.sin(
                elapsed * 2
            )
        )

        t.goto(
            -6,
            10
        )

        t.dot(
            glow
        )

    # --------------------------------------------------------
    # Update
    # --------------------------------------------------------

    screen.update()

    time.sleep(
        0.035
    )