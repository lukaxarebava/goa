from turtle import *



#square

speed(8)
width(7)
color("purple")
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
color("yellow")
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

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


exitonclick()