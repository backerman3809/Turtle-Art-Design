import turtle
speed=(0) 
turtle.colormode(255)
bob = turtle.Turtle()
bob.color(255,0,0) 
bob.pensize(5)
for i in range(12):
    bob.circle(100)
    bob.right(30)

exitonclick()
