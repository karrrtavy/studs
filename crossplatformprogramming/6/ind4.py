from turtle import *
import math
t = Turtle()
t.screen.setup(width=800, height=600)
t.speed(0)

button = Turtle()
button.shape("circle")
button.shapesize(10 )
button.up()
button.goto(0, 0)

n = int(input('input n = '))

t.hideturtle()
t.up()
t.color("red")
t.pensize(3)

def draw_star(n, radius):
    t.clear()
    t.goto(0, -radius)
    t.down()
    
    angle = 180 - 180 / n
    
    for _ in range(n):
        t.forward(radius * 2 * math.sin(math.pi / n))
        t.left(angle)
    
    t.up()

def on_click(x, y):
    button.hideturtle()
    draw_star(n, 100)

button.onclick(on_click)

t.screen.mainloop()