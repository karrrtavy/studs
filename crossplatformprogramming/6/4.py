from turtle import *
t = Turtle()
t.screen.setup(800, 800)
def sq_cr(side):
    for i in range(4):
        t.left(90)
        t.fd(side)
    t.bk(side / 2)
    t.circle(side / 2, 360)
    t.left(180)
    t.circle(side / 2, 360)
sq_cr(250)
t.screen.exitonclick()
t.screen.mainloop()