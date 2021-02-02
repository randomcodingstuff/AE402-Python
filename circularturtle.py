import turtle
a=turtle.Turtle()
a.shape("turtle")
a.penup()
for i in range(0,100,5):
    a.forward(10+i)
    a.left(30)
    a.stamp()