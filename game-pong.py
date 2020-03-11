import turtle

window = turtle.Screen()
window.bgcolor("black")
window.title("Pong by Aliza")
window.setup(width=800, height=600)

left_paddle=turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("blue")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-360, 0)


right_paddle=turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("red")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(360, 0)



#keeps the window from closing automatically
import tkinter
import _tkinter
tkinter.mainloop()
