import turtle

wn = turtle.Screen()
wn.title("Pinball")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.shapesize(stretch_wid=0.75, stretch_len=0.75)
ball.penup()
ball.goto(0, -260)
ball.dx = 0
ball.dy = 0

# pad
pad = turtle.Turtle()
pad.speed(0)
pad.color("white")
pad.shape("square")
pad.shapesize(stretch_wid=0.5, stretch_len=5)
pad.penup()
pad.goto(0, -280)

# Text
game_text = turtle.Turtle()
game_text.speed(0)
game_text.color("white")
game_text.penup()
game_text.hideturtle()
game_text.write("Press the space to start", align='center',
                font=("Courier", 24, 'bold'))
game_text.goto(0, 0)

# Lives
lives = 3
life = turtle.Turtle()
life.color("white")
life.shape("circle")
life.shapesize(stretch_wid=0.5, stretch_len=0.5)
life.penup()
life.goto(-390, 290)

# Functions


def start():
    # Start the game
    game_text.clear()
    if ball.dx == 0:
        ball.dx = 0.2
        ball.dy = 0.2


def pad_right():
    # Moves the pad to right
    x = pad.xcor()
    x += 20
    pad.setx(x)


def pad_left():
    # Moves the pad to left
    x = pad.xcor()
    x += -20
    pad.setx(x)


# Keybindings
wn.listen()
wn.onkeypress(start, 'space')
wn.onkeypress(pad_right, 'Right')
wn.onkeypress(pad_left, 'Left')
while True:

    # Movement of the ball in the game
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # When the ball hits the boundaries of the window
    # On hitting right wall
    if ball.xcor() >= 390:
        ball.dx *= -1
    # On hitting the top
    if ball.ycor() >= 290:
        ball.dy *= -1
    # On hitting the left wall
    if ball.xcor() <= -390:
        ball.dx *= -1
    # On hitting the floor
    if ball.ycor() <= -290:
        lives -= 1
        ball.goto(pad.xcor(), pad.ycor()+20)
        ball.dx = 0
        ball.dy = 0

    # Collisions with the pad
    if (ball.xcor() < pad.xcor()+40 and ball.xcor()> pad.xcor()-40) and (( ball.ycor() < -270 and ball.ycor() > -290)):
        ball.sety(-270)
        ball.dy *= -1
    if lives <= 0:
        game_text.write("Game Over, Press space \n again to start",
                        align='center', font=("Arial", 16, 'bold'))
    wn.update()
