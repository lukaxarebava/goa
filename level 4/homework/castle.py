from turtle import *



#square

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

#door


forward(70)
color("grey")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)


#roof

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

#wall right

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



exitonclick()