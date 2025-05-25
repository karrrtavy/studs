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

t.up(); t.goto(0, 0); t.down()
for i in range(4):
    t.fd(50); t.left(60); t.fd(140); t.left(150); t.fd(140); t.left(60); t.fd(50)
t.goto(0, 0); t.right(45); t.fd(175); t.left(180); t.fd(350); t.left(180); t.fd(175); t.left(90); t.fd(175); t.left(180); t.fd(350)

t.up(); t.goto(-400, -100); t.down()

for i in range(8):
    t.fd(50); t.right(150); t.fd(50); t.left(150)
print(t.position())
t.left(15) 
for i in range(8):
    t.fd(50); t.right(150); t.fd(40); t.left(150)
t.up(); t.goto(-220, -203); t.down(); t.right(120)
for i in range(8):
    t.down()
    t.fd(50); t.right(150); t.fd(85); t.right(150); t.fd(50); t.right(60)
    t.up(); t.goto(t.xcor() - 30, t.ycor() - 30)

t.goto(0, -250); t.down()
for i in range(8):
    t.up(); t.goto(t.xcor() + 30, t.ycor()); t.down()
    for j in range(4):
        t.fd(30 + i * 5); t.right(90)


t.screen.exitonclick()
t.screen.mainloop()






# по 6 лабе: сначала нужна кнопка в виде треугольника, затем нарисровать пентаграмму

#  