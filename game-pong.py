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
ball.shape=("square")
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
scoreboard.write("Player A: 0 || Player B: 0",align="center", font=("Arial", 24, "normal")

#functions
##left paddle up
##left paddle down
##right paddle up
## right paddle down

#keyboard listeners
                 
#main game loop
    #move ball
    #bounce ball
    #ball goes off screen
    #ball collides with paddles


#keeps the window from closing automatically
import tkinter
import _tkinter
tkinter.mainloop()
