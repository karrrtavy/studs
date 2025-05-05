import turtle

turtle.title('Turtle Circles')
circ = turtle.Turtle()
circ.pencolor('purple')
circ.fillcolor('orange')
circ.shape('circle')
circ.pensize(5)
circ.speed(10)
circ.fd(150)
circ.begin_fill()
circ.circle(90)
circ.end_fill()

n = 10
t = turtle.Turtle()
while n <= 50:
    t.circle(n)
    n += 10
turtle.exitonclick()