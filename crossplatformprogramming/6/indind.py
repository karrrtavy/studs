# from turtle import *
# import math
# t = Turtle()
# t.screen.setup(1000, 1000)
# t.speed(0)

# def talloval(r, angle):
#     t.left(angle)
#     for i in range(2):      
#         t.circle(r,90)    
#         t.circle(r/2,90)  

# talloval(100, -45); 
# t.up(); t.goto(xcor() + 100, ycor() + 0); t.down()
# talloval(100, -60)
# t.up(); t.goto(xcor() + 150, ycor() - 75); t.down()
# talloval(100, -75)
# t.up(); t.goto(xcor() + 75, ycor() - 175); t.down()
# talloval(100, -90)
# t.up(); t.goto(xcor() - 25, ycor() - 125); t.down()
# talloval(100, -75)

# def draw_star():
#     t.up(); t.right(-20)
    
#     radius = 270
    
#     t.goto(-30, -radius + 70)
#     t.down()
#     angle = 180 - 180 / 5
#     for _ in range(5):
#         t.forward(radius * 2 * math.sin(math.pi / 5))
#         t.left(angle)

# draw_star()

# t.penup()


# t.screen.exitonclick()
# t.screen.mainloop()

##################################################################################

from turtle import *
import math
t = Turtle()
t.screen.setup(1000, 1000)
t.speed(0)

button = Turtle()
button.shape('circle')
button.shapesize(10 )
button.up()
button.goto(0, 0)

t.hideturtle()
t.up()
t.color('black')
t.pensize(10)
t.down()



def draw_star():
    def talloval(r, angle):
        t.left(angle)
        for _ in range(2):      
            t.circle(r,90)    
            t.circle(r/2,90)  

    talloval(100, -45); 
    t.up(); t.goto(xcor() + 100, ycor() + 0); t.down()
    talloval(100, -60)
    t.up(); t.goto(xcor() + 150, ycor() - 75); t.down()
    talloval(100, -75)
    t.up(); t.goto(xcor() + 75, ycor() - 175); t.down()
    talloval(100, -90)
    t.up(); t.goto(xcor() - 25, ycor() - 125); t.down()
    talloval(100, -75)
    
    t.up(); t.right(-20)
    radius = 270
    t.goto(-30, -radius + 70)
    t.down()
    angle = 180 - 180 / 5
    for i in range(5):
        t.forward(radius * 2 * math.sin(math.pi / 5))
        t.left(angle)

def on_click(x, y):
    button.hideturtle()
    draw_star()

button.onclick(on_click)

t.screen.mainloop()