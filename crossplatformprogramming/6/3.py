from turtle import *
t = Turtle()
t.screen.setup(800, 800)
def rectangle (w, h):
    for i in range (2):
        t.left(90)
        t.fd(h)
        t.left(90)
        t.fd(w)
rectangle(320, 200)
t.screen.exitonclick()
t.screen.mainloop()