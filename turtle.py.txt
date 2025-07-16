import turtle
import time 

# Create a turtle object
tommy = turtle.Turtle()

# Set the shape to "turtle"
tommy.shape("turtle")

# Optionally, customize appearance
tommy.color("green")  
turtle2 = turtle.Turtle()
tommy.penup()
turtle2.penup()
tommy.forward(-150)
tommy.left(90)
tommy.forward(100)
tommy.right(90)
turtle2.forward(-150)
turtle2.right(90)
turtle2.forward(100)
turtle2.left(90)
print ("start")
turtle2.speed(0)
tommy.pendown()
turtle2.pendown()
turtle2.forward(250)
time.sleep(2)
tommy.forward(500)
turtle2.forward(150)


