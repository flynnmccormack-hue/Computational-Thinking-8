# ###############################################
# ### SETUP ###
import turtle
# ###############################################
turtle.Screen().bgcolor("MidnightBlue")#I changed this color so that you could see everything clearly.
t = turtle.Turtle()
t.speed(10)
t.penup()
t.goto(-250, 10)#perfect
t.color("PaleGreen")
t.pendown()
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)

t = turtle.Turtle()
t.penup()
t.goto(100,10)
t.color("Silver")
t.pendown()
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)#I made these two shapes for eyes

t = turtle.Turtle()
t.penup()
t.goto(-180,-50)
t.color("Silver")
t.pendown()
t.left(350)
t.forward(175)
t.left(20)
t.forward(175)#This was my smile

t = turtle.Turtle()
t.penup()
t.goto(-150,-150)
t.write("Go Mariners!",font = ("Arial", 40, "normal"))

t= turtle.Turtle()
t.penup()
t.goto(-150,230)
t.pendown()
t.right(75)
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(40)

t= turtle.Turtle()
t.penup()
t.goto(150,230)
t.pendown()
t.right(75)
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(40)
t.left(90)
t.forward(40)
t=turtle.Turtle()
t.penup()
t.goto(-90,180)
t.write("Go #29!",font = ("Arial", 40, "normal"))#Cal raleigh's number!

# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################
