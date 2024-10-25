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
forward(220)
left(90)
forward(150)
left(90)
forward(70)
left(90)
forward(150)

#now we need GOA sign on our flag, so lets draw it.

penup()
goto(-110, 400)
pendown()

width(1)
left(180)
forward(30)
left(90)
forward(42)
left(90)
forward(30)
left(90)
forward(20)
left(90)
forward(20)

penup()
goto(-80, 400)
pendown()

circle(20)

penup()
goto(-55, 358)
pendown()

right(115)
forward(50)
right(140)
forward(50)

penup()
goto(-45, 378)
pendown()
left(75)
forward(20)

#now lets draw king

penup()
goto(-150, -100)
pendown()

circle(10)

penup()
goto(-150, -100)
pendown()

right(90)
forward(50)

left(30)
forward(40)


penup()
goto(-150, -100)
pendown()

right(30)
forward(50)
right(30)
forward(40)

penup()
goto(-150, -125)
pendown()

right(110)
forward(40)

penup()
goto(-150, -125)
pendown()

right(90)
forward(40)

#now lets draw queen

penup()
goto(-50, -125)
pendown()

circle(10)
right(120)

penup()
goto(-56, -126)
pendown()

right(10)
forward(50)
left(30)
forward(40)

penup()
goto(-56, -175)
pendown()

right(60)
forward(40)

penup()
goto(-56, -150)
pendown()

right(100)
forward(40)

penup()
goto(-56, -150)
pendown()

left(250)
forward(40)



#python will automaticly close our drawing. to stop this action we need to type exitonclick(). so when we click on our drawing it will close only then.

exitonclick()