import turtle
import math
wn = turtle.Screen()
wn.title("Shape")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer()

circle = turtle.Turtle()
circle.hideturtle()
color = ['white', 'red', 'blue', 'green']
radius = 50

while True:
    circle.penup()
    circle.goto(0, radius)
    circle.color(color[int(radius/50)-1])
    circle.pendown()
    for x in range(radius +1):
        y = math.sqrt(pow(radius,2)-pow(x,2))
        circle.goto(x,y)
    for x in range(radius,-1,-1):
        y = -(math.sqrt(pow(radius,2)-pow(x,2)))
        circle.goto(x,y)
    for x in range(0,-radius-1,-1):
        y = -math.sqrt(pow(radius,2)-pow(x,2))
        circle.goto(x,y)
    for x in range(radius,-1,-1):
        y = math.sqrt(pow(radius,2)-pow(x,2))
        circle.goto(-x,y)
    radius += 50
    wn.update()