from turtle import *
t = Turtle()
t.screen.setup(800, 800)
t.up()
t.goto(-450, 0)
t.down()
t.setheading(270)
for i in range(5):
    t.circle(50, 180)
    t.begin_fill()
    t.circle(-50, 180)
    t.end_fill()
t.screen.exitonclick()
t.screen.mainloop()