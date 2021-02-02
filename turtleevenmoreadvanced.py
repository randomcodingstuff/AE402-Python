import turtle
n=int(input("Input a number! "))
a=turtle.Turtle()
for i in range(n):
    a.forward(100)
    a.left(360/n)
while i<100: 
    a.forward(10+i)
    a.left(30)
    i=i+1