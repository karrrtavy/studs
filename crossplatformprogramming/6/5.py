from turtle import *
t = Turtle()
t.screen.setup(800, 800)
def circ(d, r, rBig):
    for i in range(d):
        t.circle(rBig, 360 / d)
        t.dot(r, 'red')
t.up()
t.goto(350, 0)
t.setheading(90)
t.down()
circ(45, 10, 350)
t.screen.exitonclick()
t.screen.mainloop()