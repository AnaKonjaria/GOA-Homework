from turtle import *

#drawing a house

#step1: draw a square
speed(15)
width(7)
color("Purple")
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
#end of square

#step2: draw a door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(120, 60)
pendown()

color("brown")
forward(5)
#end of door

#step3: draw a roof
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
#end of roof

#Step4: draw windows
penup()
goto(50, 150)
pendown()

color("blue")
begin_fill()
right(60)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()

penup()
goto(50, 50)
pendown()

color("blue")
begin_fill()
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()

penup()
goto(150, 150)
pendown()

color("blue")
begin_fill()
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()

penup()
goto(150, 50)
pendown()

color("blue")
begin_fill()
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
right(90)
forward(30)
end_fill()

exitonclick()