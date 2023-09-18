import turtle
import winsound
from pathlib import Path

# Making the Window
wn = turtle.Screen()
wn.title("Pong with turtle")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid = 5, stretch_len =1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid = 5, stretch_len =1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0
ball.dy = 0
# True means ball moves right False means the ball moves the left
ball.move = True

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=('Courier', 20, 'bold'))

# Start text
start = turtle.Turtle()
start.speed(0)
start.color('white')
start.hideturtle()
start.penup()
start.goto(0,20)
start.write("Press Space to Play", align='center', font = ('Courier', 20, 'bold'))

# Movement Functions
def paddle_a_up():
    ycor = paddle_a.ycor()
    ycor += 25
    paddle_a.sety(ycor)

def paddle_a_down():
    ycor = paddle_a.ycor()
    ycor -= 25
    paddle_a.sety(ycor)

def paddle_b_up():
    ycor = paddle_b.ycor()
    ycor += 25
    paddle_b.sety(ycor)

def paddle_b_down():
    ycor = paddle_b.ycor()
    ycor -= 25
    paddle_b.sety(ycor)

def game_start():
    start.clear()
    # ball.move = not(ball.move)
    if ball.dx == 0:
        if ball.move:
            ball.dx = 0.2
            ball.dy = 0.2
        else:
            ball.dx = -0.2
            ball.dy = -0.2
    
        
def game_pause():
    start.write("Press Space to Start", align='center', font = ('Courier', 20, 'bold'))
    ball.goto(0,0)
    ball.move = not(ball.move)
    ball.dx = 0
    ball.dy = 0

# Key bindings
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')
wn.onkeypress(game_start,'space')

# Scoring
score_a =0
score_b = 0

# Game Loop
while True:
    # Updates the screen
    wn.update()

    # Moves the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Control the movement of the ball and Sets the boundaries of the ball
    if ball.ycor() >= 290:
        ball.dy *= -1
        winsound.PlaySound(str(Path("sounds/bullet_fire.wav")), winsound.SND_ASYNC)
    if ball.ycor() <= -290:
        ball.dy *= -1
        winsound.PlaySound(str(Path("sounds/bullet_fire.wav")), winsound.SND_ASYNC)

    # If a player scores
    if ball.xcor() >= 390:
        score_a +=1
        game_pause()
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=('Courier', 20, 'bold'))
    
    if ball.xcor() <= -390:
        score_b +=1
        game_pause()
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=('Courier', 20, 'bold'))

    # Collision interactions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+45 and ball.ycor()>paddle_b.ycor()-45 ):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound(str(Path("sounds/bullet_fire.wav")), winsound.SND_ASYNC)

    
    if (ball.xcor() <- 340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+45 and ball.ycor()>paddle_a.ycor()-45 ):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound(str(Path("sounds/bullet_fire.wav")), winsound.SND_ASYNC)

    