from turtle import *


screen = Screen()

screen.bgcolor("lightblue")

color("green")

speed(1000000000000000000000000000)

penup()

width(3)

goto(-480, -200)

pendown()
begin_fill()
#start of grass
forward(950)
right(90)
forward(200)
right(90)
forward(950)
right(90)
forward(200)
end_fill()
#end of grass

#start of castle
right(90)
#start of tower 1
forward(300)
color("gray")
left(90)
forward(300)


color("darkred")
begin_fill()
left(90)
forward(20)
right(120)
forward(150)
right(120)
forward(150)
right(120)
forward(150)
end_fill()
right(180)
forward(130)
right(90)
color("gray")
begin_fill()
forward(300)
right(90)
forward(110)
right(90)
forward(300)
right(90)
forward(110)
end_fill()
color("black")
right(90)
forward(300)
right(90)
forward(110)
right(90)
forward(300)
right(90)
forward(130)
left(120)
forward(150)
left(120)
forward(150)
left(120)
forward(130)
right(90)
forward(70)
left(90)
#end of tower 1

#start of middle
color("gray")
forward(350)
#end of middle

#start of tower 2
left(90)
begin_fill()
forward(70)
right(90)
forward(110)
right(90)
forward(300)
right(90)
forward(110)
right(90)
forward(300)
end_fill()

color("darkred")
begin_fill()
left(90)
forward(20)
right(120)
forward(150)
right(120)
forward(150)
right(120)
forward(130)
end_fill()

#filling middle and making the door
color("gray")
left(90)
forward(70)
begin_fill()
forward(230)
right(90)
forward(350)
right(90)
forward(230)
end_fill()

#start of outlines
color("black")
right(180)
forward(230)
left(90)
forward(350)
forward(110)
left(90)
forward(300)
left(90)
forward(110)
left(90)
forward(300)
right(180)
forward(300)
left(90)
forward(20)
right(120)
forward(150)
right(120)
forward(150)
right(120)
forward(130)
left(90)
forward(70)
right(90)
forward(350)
right(180)
forward(120)
left(90)

#start of main tower
forward(2)
color("gray")
begin_fill()
forward(130)
right(90)
forward(110)
right(90)
forward(130)
right(90)
forward(110)
end_fill()
right(90)
forward(130)
color("darkred")
begin_fill()
left(90)
forward(20)
right(120)
forward(150)
right(120)
forward(150)
right(120)
forward(130)
end_fill()

color("black")
forward(20)
right(120)
forward(150)
right(120)
forward(150)
right(120)
forward(130)
left(90)
forward(130)
left(90)
forward(110)
left(90)
forward(130)
right(90)
#start of door
penup()
goto(70, -200)
pendown()
color("orange")
begin_fill()
left(90)
forward(90)
right(90)
forward(70)
right(90)
forward(90)
right(90)
forward(70)
end_fill()
color("black")
right(90)
forward(90)
right(90)
forward(70)
right(90)
forward(90)
right(90)
forward(70)
right(180)
forward(35)
left(90)
forward(90)
#end of door

#start of right window
penup()
goto(310, 70)
pendown()
color("orange")
begin_fill()
right(90)
forward(50)
right(90)
forward(70)
right(90)
forward(50)
right(90)
forward(70)
end_fill()
color("black")
right(90)
forward(50)
right(90)
forward(70)
right(90)
forward(50)
right(90)
forward(70)
right(90)
forward(25)
right(90)
forward(70)
right(90)
forward(25)
right(90)
forward(35)
right(90)
forward(50)
#end of right window


#start of left window
penup()
goto(-150, 70)
pendown()

color("orange")
begin_fill()
forward(50)
right(90)
forward(70)
right(90)
forward(50)
right(90)
forward(70)
end_fill()
color("black")
right(90)
forward(50)
right(90)
forward(70)
right(90)
forward(50)
right(90)
forward(70)
right(90)
forward(25)
right(90)
forward(70)
right(90)
forward(25)
right(90)
forward(35)
right(90)
forward(50)
#end of left window


#start of GOA flag
penup()
goto(0, 30)
forward(50)
left(90)
forward(130)
left(90)
forward(20)
right(120)
pendown()
forward(70)
begin_fill()
left(30)
forward(160)
left(90)
forward(200)
left(90)
forward(130)
left(90)
forward(200)
end_fill()
penup()
color("white")
left(90)
forward(60)
left(90)
forward(160)
right(180)
pendown()
forward(25)
right(90)
forward(40)
right(90)
forward(60)
right(90)
forward(80)
right(90)
forward(60)
penup()
color("green")
forward(20)
pendown()
forward(45)
right(90)
forward(80)
right(90)
forward(45)
right(90)
forward(80)
penup()
color("white")
right(180)
forward(80)
left(90)
forward(65)
left(65)
pendown()
forward(90)
right(155)
forward(80)
right(180)
forward(40)
left(90)
forward(20)
#end of GOA flag

#start of king
color("black")
penup()
goto(-300, -100)
pendown()
left(90)
forward(70)
right(30)
forward(35)
right(180)
forward(35)
right(120)
forward(35)
left(180)
forward(35)
right(30)
forward(60)
left(120)
forward(30)
right(180)
forward(30)
right(50)
forward(30)
right(180)
forward(30)
right(70)
forward(20)
right(90)
circle(20)
penup()
left(90)
forward(40)
pendown()
color("yellow")
begin_fill()
left(90)
forward(30)
right(90)
forward(25)
right(120)
forward(20)
left(90)
forward(20)
right(110)
forward(25)
right(250)
forward(25)
right(150)
forward(35)
right(90)
forward(50)
end_fill()
#end of king

#start of queen
penup()
color("black")
goto(-400, -100)
pendown()
left(90)
forward(70)
right(30)
forward(35)
right(180)
forward(35)
right(120)
forward(35)
left(180)
forward(35)
right(30)
forward(60)
left(120)
forward(30)
right(180)
forward(30)
right(50)
forward(30)
right(180)
forward(30)
right(70)
forward(18)
right(90)
circle(20)
penup()
goto(-380, -80)
right(90)
pendown()
forward(30)
right(180)
forward(50)
penup()
goto(-420, -80)
pendown()
forward(20)
right(180)
forward(50)

exitonclick()


