from turtle import*


speed(5)




#we want to paint hous
#step 1 : draw a square 
width(8)
color ("red")

forward(200)
left(90)


forward(200)
left (90)

forward(200)
left (90)


forward (200)
left(90) 
#step 2 door 

width (7)


forward (70)
left (90)
color ("purple") 
begin_fill()

forward (90)
right(90)

forward (60)
right (90)

forward (90)
left (90)
end_fill()


color("red")



#step 3 roof


penup()
goto (200,200)
pendown()


color ("black")
begin_fill()
left(120)
forward(200)
left (120)
forward(200)
end_fill()
# step 3 window 

left(30)
color("red")
forward(50)
color("black")
begin_fill()
left(90)
forward(50)

right(90)
forward(50)
right(90)
forward(50)
end_fill()


penup()
goto(200,200)
left(90)
forward(50)
pendown()

color ("black")
begin_fill()
right(90)
forward(50)
left(90)
forward(50)

left(90)
forward(50)
end_fill()


  














 










exitonclick ()