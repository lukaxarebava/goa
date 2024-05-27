#lets draw a castle in python.
#first of all we need to type from turtle import* to draw in python turtle graphics
from turtle import *



#first lets draw square for the house.

speed(12)
width(7)
color("black")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#lets draw a door for the house.


forward(70)
color("grey")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)


#now lets draw roof.

penup()
goto(200, 200)
pendown()

color("grey")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#now we need a wall for the castle, first lets draw right wall.

penup()
goto(200, 160)
pendown()

color("grey")
begin_fill()
left(120)
forward(140)
left(90)
forward(100)
right(30)
forward(50)
right(115)
forward(50)
right(33)
forward(270)
right(94)
forward(200)
end_fill()

#left wall.

penup()
goto(1, 160)
pendown()

color("grey")
begin_fill()
left(2)
forward(140)
right(90)
forward(100)
left(30)
forward(50)
left(115)
forward(50)
left(35)
forward(260)
left(90)
forward(190)
end_fill()

#now lets draw a flag.

penup()
goto(1, 200)
pendown()

left(90)
forward(150)
left(90)
forward(60)
left(90)
forward(40)
left(90)
forward(60)

#python will automaticly close our drawing. to stop this action we need to type exitonclick(). so when we click on our drawing it will close only then.

exitonclick()