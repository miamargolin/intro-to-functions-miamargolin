import turtle
from turtle import *
t=Turtle()

t.shape('turtle')

""" for i in range(4):
    t.forward(100)
    t.left(90)
print(i)  """



def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
square(200)

for i in range(60):
    square(100)
    t.right(5)

turtle.done()