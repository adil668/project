import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Burj Khalifa Night View")
screen.bgcolor("black")

# Turtle setup
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

# Draw stars
def draw_stars():
    pen.color("white")
    for _ in range(60):
        x = random.randint(-400, 400)
        y = random.randint(0, 300)

        pen.penup()
        pen.goto(x, y)
        pen.pendown()

        pen.begin_fill()
        pen.circle(2)
        pen.end_fill()

# Draw Burj Khalifa style tower
def draw_burj():
    pen.penup()
    pen.goto(-40, -250)
    pen.setheading(90)
    pen.pendown()

    widths = [80, 70, 60, 50, 40, 30, 20, 10]
    heights = [80, 100, 120, 140, 160, 180, 200, 220]

    colors = ["#555555", "#666666", "#777777", "#888888"]

    for i in range(len(widths)):
        pen.color(random.choice(colors))
        pen.begin_fill()

        for _ in range(2):
            pen.forward(heights[i])
            pen.right(90)
            pen.forward(widths[i])
            pen.right(90)

        pen.end_fill()

        # move upward and slightly center
        pen.penup()
        pen.forward(heights[i])
        pen.right(90)
        pen.forward(widths[i] / 2 - widths[i + 1] / 2 if i < len(widths) - 1 else 0)
        pen.left(90)
        pen.pendown()

# Draw ground lights
def draw_ground():
    pen.penup()
    pen.goto(-500, -250)
    pen.pendown()

    for _ in range(30):
        pen.color("yellow")
        pen.begin_fill()
        pen.circle(3)
        pen.end_fill()

        pen.penup()
        pen.forward(30)
        pen.pendown()

# Title text
def title():
    pen.penup()
    pen.goto(0, 320)
    pen.color("gold")

    pen.write("BURJ KHALIFA",
              align="center",
              font=("Arial", 28, "bold"))

# Draw scene
draw_stars()
draw_ground()
draw_burj()
title()

# Hide turtle
pen.hideturtle()

# Finish
screen.mainloop()