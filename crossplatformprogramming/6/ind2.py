from turtle import *
t = Turtle()
t.screen.setup(1000, 1000)
t.speed(0)

t.up(); t.goto(-350, 200); t.down()
for i in range(4):
    t.fd(100); t.left(90)
t.left(45); t.fd(141); t.up()

t.goto(-220, 200); t.right(45); t.down()
for i in range(4):
    t.fd(100); t.left(90)
t.left(90); t.fd(100); t.right(45)
for i in range(3):
    t.down(), t.fd(100); t.up(); 
    if i == 0: t.goto( -120, 300); t.down()
    if i == 1: t.up(), t.goto(-120, 200)
for i in range(2):
    t. down()
    t.left(45) if i == 0 else t.left(90)
    t.fd(100)

t.up(), t.goto(150,  200); t.right(45); t.down()
for i in range(2):
    t.fd(200); t.right(180)
    if i == 0: t.fd(100); t.right(90); t.up(); t.fd(100); t.down(); t.right(180)

for i in range()


t.screen.exitonclick()
t.screen.mainloop()