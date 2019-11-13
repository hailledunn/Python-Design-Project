#main program file
from DunnFunctions import*
turtle.colormode(255)
bob.speed(0)
turtle.bgcolor("black")
bob.color("gray")
bob.width(20)

bob.penup()
bob.left(180)
bob.forward(975)
bob.right(90)
bob.forward(975)
bob.right(90)
bob.pendown()
for times in range(8):
    bob.forward(1920)
    bob.right(90)
    bob.penup()
    bob.forward(100)
    bob.right(90)
    bob.pendown()
    bob.forward(1920)
    bob.left(90)
    bob.penup()
    bob.forward(100)
    bob.left(90)
    bob.pendown()

bob.penup()
bob.forward(100)
bob.left(90)
bob.forward(1130)
bob.pendown()
bob.left(180)

for times in range(10):
    bob.forward(1920)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.pendown()
    bob.forward(1920)
    bob.right(90)
    bob.penup()
    bob.forward(100)
    bob.right(90)
    bob.pendown()

bob.color("white")
jump(-875,-427)
bob.left(90)

for times in range(5):
    for times in range(18):
        bob.circle(5)
        bob.penup()
        bob.forward(100)
        bob.pendown()
    bob.circle(5)
    bob.left(90)
    bob.penup()
    bob.forward(105)
    bob.pendown()
    bob.left(90)
    for times in range(18):
        bob.circle(5)
        bob.penup()
        bob.forward(100)
        bob.pendown()
    bob.circle(5)
    bob.right(90)
    bob.penup()
    bob.forward(95)
    bob.pendown()
    bob.right(90)
    


