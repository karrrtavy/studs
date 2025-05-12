import turtle

window = turtle.Screen()
window.title('Screen & Button')
window.setup(500, 500)

btnl = turtle.Turtle()
btnl.hideturtle()
for i in range(2):
    btnl.fd(80)
    btnl.left(90)
    btnl.fd(30)
    btnl.left(90)
btnl.penup()
btnl.goto(11, 7)
btnl.write('Push me', font=('Arial', 12, 'normal'))

def btnclick(x, y):
    if 0 < x < 80 and 0 < y < 30:
        print('Кнопка нажата!')
        btnl.clear()
        ball = turtle.Turtle()
        turtle.fillcolor('orange')
        turtle.pencolor('purple')
        turtle.shape('circle')
turtle.listen()
turtle.onscreenclick(btnclick, 1)
turtle.done()