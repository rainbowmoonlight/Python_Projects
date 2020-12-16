import turtle

def petal(t, r, angle):
    for i in range(2):
        t.circle(r,angle)
        t.left(180-angle)

def flower(t, n, r, angle):
    for i in range(n):
        petal(t,r,angle)
        t.left(360/n)

def move(t, length):
    window = turtle.Screen()
    window.bgcolor("Yellow")
    t.pu()
    t.fd(length)
    t.pd()

tim = turtle.Turtle()
tim.speed("fastest")
tim.shape("turtle")
tim.color("green")
move(tim, -150)
tim.begin_fill()
flower(tim, 7, 60, 60)
tim.end_fill()

tim.color("red")
move(tim, 150)
tim.begin_fill()
flower(tim, 25, 30, 100)
tim.end_fill()

tim.color("blue")
move(tim, 150)
tim.begin_fill()
flower(tim, 14, 70, 50)
tim.end_fill()


screen = turtle.Screen()
screen.exitonclick()