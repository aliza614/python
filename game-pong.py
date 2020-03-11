import turtle

window = turtle.Screen()
window.bgcolor("black")
window.title("Pong by Aliza")
window.setup(width=800, height=600)

#score
left_score=0
right_score=0

#left_paddle
left_paddle=turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("blue")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-360, 0)

#right paddle
right_paddle=turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("red")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(360, 0)

#ball
ball=turtle.Turtle()
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=2
ball.dy=2

#scoreboard
scoreboard=turtle.Turtle()
scoreboard.color("black")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0,260)
scoreboard.clear()
scoreboard.write("Player A: 0 || Player B: 0",align="center", font=("Arial", 24, "normal"))

#functions
##left paddle up
def left_paddle_up():
    y=left_paddle.ycor()
    if y<=240:
        y+=20
    left_paddle.sety(y)
                 
##left paddle down
def left_paddle_down():
     y=left_paddle.ycor()
     if y>=-220:
         y-=20
     left_paddle.sety(y)
##right paddle up
def right_paddle_up():
     y=right_paddle.ycor()
     if y<=240:
         y+=20
     right_paddle.sety(y)
## right paddle down
def right_paddle_down():
     y=right_paddle.ycor()
     if y>=-220:
         y-=20
     right_paddle.sety(y)
#keyboard listeners
window.onkeypress(left_paddle_up, "q")
window.onkeypress(left_paddle_down, "a")
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_down, "Down")
                 
#main game loop
while True:
    window.update()
    #move ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #bounce ball
    if ball.ycor()>290:
         ball.sety(290)
         ball.dy*=-1
    if ball.ycor()<-290:
         ball.sety(-290)
         ball.dy*=-1
    
    #ball goes off screen
    if ball.xcor()>390:
         ball.goto(0,0)
         ball.dx*=-1
         left_score+=1
    if ball.ycor()<-390:
         ball.got(0,0)
         ball.dx*=-1
         right_score+=1
    #ball collides with paddles
    if ball.xcor()>340 and ball.xcor()<350 and (ball.ycor()<right_paddle.ycor()+40 and ball.ycor()>right_paddle.ycor()-40):
         ball.dx*=-1
    if ball.xcor()<-340 and ball.xcor()>-350 and (ball.ycor()<left_paddle.ycor()+40 and ball.ycor()>left_paddle.ycor()-40):
         ball.dx*=-1
#keeps the window from closing automatically
#import tkinter
#import _tkinter
#tkinter.mainloop()
