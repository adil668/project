import turtle

# Screen setup
wn = turtle.Screen()
wn.title("Heart with Arrow")
wn.bgcolor("white")

# Turtle setup
pen = turtle.Turtle()
pen.speed(3)
pen.pensize(5)

# Function to draw heart
def draw_heart():
    pen.color("red")
    pen.fillcolor("red")

    pen.begin_fill()
    pen.left(140)
    pen.forward(180)

    pen.circle(-90, 200)
    pen.left(120)
    pen.circle(-90, 200)

    pen.forward(180)
    pen.end_fill()

# Function to draw arrow
def draw_arrow():
    pen.penup()
    pen.goto(-180, 20)
    pen.setheading(0)
    pen.pendown()

    # Arrow line
    pen.color("brown")
    pen.pensize(8)
    pen.forward(360)

    # Arrow head
    pen.begin_fill()
    pen.right(150)
    pen.forward(25)
    pen.backward(25)

    pen.left(300)
    pen.forward(25)
    pen.backward(25)
    pen.end_fill()

# Function to write text
def write_text():
    pen.penup()
    pen.goto(0, -40)
    pen.color("white")
    pen.write("LOVE", align="center",
              font=("Arial", 24, "bold"))

# Draw everything
draw_heart()
draw_arrow()
write_text()

# Hide turtle
pen.hideturtle()

# Keep window open
wn.mainloop()