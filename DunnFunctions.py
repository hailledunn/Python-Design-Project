#function file
import turtle
bob=turtle.Turtle()
bob.speed(0)

        
def polygon(sides,distance,color):
    angle=360/sides
    bob.color(color)
    for times in range(sides):
        bob.forward(distance)
        bob.right(angle)

def jump(x,y):
  bob.penup()
  bob.goto(x,y)
  bob.pendown()
 

def star(distance,c):
    bob.color(c)
    for times in range(5):
        bob.forward(distance)
        bob.right(144)

def explosion(d,c):
    bob.color(c)
    bob.begin_fill()
    for times in range(8):
        bob.forward(d)
        bob.right(135)
    bob.end_fill()

def line(d):
    bob.forward(d)



