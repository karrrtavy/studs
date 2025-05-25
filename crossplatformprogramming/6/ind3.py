# B = 6, A = 18
from turtle import *
t = Turtle()
t.screen.setup(width=800, height=600)
t.speed(0)

A = 18
B = 6

scale_x = 30
scale_y = 0.001

t.goto(-350, 0)
t.down()
t.goto(350, 0)
t.up()
t.goto(0, -250)
t.down()
t.goto(0, 250)
t.up()

t.down()
t.color("blue")

for x_pixel in range(-350, 350):
    x = x_pixel / scale_x
    y = A * (x ** B)
    y_pixel = y * scale_y
    t.goto(x_pixel, y_pixel)

t.screen.exitonclick()
t.screen.mainloop()