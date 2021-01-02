# First Semester -> 2018
# -------------------------------------------------------------------
# Use the turtle to fill your screen with a simple crosshatch pattern.
# Use the turtle to write your name.
# Bonus point for a name written with the turtle which looks like handwritten
# Pasero Christian
# -------------------------------------------------------------------

import turtle
screen = turtle.Screen()
screen.title("Write your name")
turtle.setup(600,400)   #Screen size
pencil = turtle.Turtle()
pencil.speed("fastest")
pencil.width(1)
pencil.color(0.7,0.7,0.7)

name1_pos_X = -200
name2_pos_X = -200
name1_pos_Y = 100
name2_pos_Y = -100
name1_height = 25
letter_distance = 10

##--Pattern
pattern_position_X = 250
for i in range(11):
    pencil.penup()
    pencil.home()
    pencil.setposition(pattern_position_X, 200)
    pencil.right(45)
    pencil.pendown()
    while pencil.xcor()<300:
        pencil.forward(20)
    pattern_position_X = pattern_position_X - 50

pattern_position_Y = 200
for i in range(8):
    pencil.penup()
    pencil.home()
    pencil.setposition(-300, pattern_position_Y)
    pencil.right(45)
    pencil.pendown()
    while pencil.ycor()>-200:
        pencil.forward(20)
    pattern_position_Y = pattern_position_Y - 50


pattern_position_X = -250
for i in range(12):
    pencil.penup()
    pencil.home()
    pencil.setposition(pattern_position_X, 200)
    pencil.right(135)
    pencil.pendown()
    while pencil.xcor()> -300:
        pencil.forward(20)
    pattern_position_X = pattern_position_X + 50

pattern_position_Y = 150
for i in range(7):
    pencil.penup()
    pencil.home()
    pencil.setposition(300, pattern_position_Y)
    pencil.right(135)
    pencil.pendown()
    while pencil.ycor()>-200:
        pencil.forward(20)
    pattern_position_Y = pattern_position_Y - 50
##Pattern-end

pencil.width(3)
pencil.color(0,0,0)

##--C
pencil.penup()
pencil.home()
pencil.setposition(name1_pos_X,name1_pos_Y)
for x in range(2):
    pencil.forward(10)
    pencil.right(5)
pencil.right(180)
pencil.pendown()

for x in range(50):
    pencil.forward(2)
    pencil.left(5)
for x in range(12):
    pencil.forward(3)
    pencil.left(2)
for x in range(5):
    pencil.forward(2)
    pencil.left(37)
pencil.forward(45)
pencil.right(180)
pencil.forward(16)
for x in range(8):
    pencil.forward(3)
    pencil.right(22)
pencil.forward(13)
for x in range(8):
    pencil.forward(2)
    pencil.left(20)
pencil.forward(20)
pencil.right(163)
for x in range(8):
    pencil.forward(2)
    pencil.left(25)
pencil.right(190)
pencil.forward(17)
for x in range(8):
    pencil.forward(2)
    pencil.left(21.25)
pencil.forward(20)
pencil.penup()
pencil.forward(10)
pencil.pendown()
pencil.forward(2)
pencil.right(180)
pencil.penup()
pencil.forward(10)
pencil.pendown()
pencil.forward(17)
for x in range(8):
    pencil.forward(2)
    pencil.left(18)
pencil.forward(20)
pencil.right(180)
for x in range(4):
    pencil.forward(2)
    pencil.left(18)
for x in range(8):
    pencil.forward(2)
    pencil.right(18)
pencil.right(150)
pencil.forward(10)
for x in range(4):
    pencil.forward(2)
    pencil.left(19.5)
pencil.forward(40)
pencil.right(180)
pencil.forward(10)
pencil.right(90)
pencil.forward(10)
pencil.right(180)
pencil.forward(20)
pencil.right(180)
pencil.forward(10)
pencil.left(90)
pencil.forward(30)
for x in range(12):
    pencil.forward(2)
    pencil.left(15)
pencil.forward(20)
pencil.penup()
pencil.forward(10)
pencil.pendown()
pencil.forward(2)
pencil.right(180)
pencil.penup()
pencil.forward(10)
pencil.pendown()
pencil.forward(17)
#a
for x in range(12):
    pencil.forward(2)
    pencil.left(15)
for x in range(60):
    pencil.forward(2)
    pencil.right(9)
pencil.forward(5)

for x in range(15):
    pencil.forward(2)
    pencil.left(15)
pencil.right(45)
pencil.forward(15)
pencil.right(180)
pencil.forward(5)
pencil.left(135)
for x in range(12):
    pencil.forward(2)
    pencil.right(10)
pencil.right(20)
pencil.forward(10)
for x in range(8):
    pencil.forward(2)
    pencil.left(20)
pencil.penup()
pencil.home()

#######Ende Handschrift######


##Grosssbuchstaben
CstartX = -200
##C
pencil.penup()
pencil.setposition(CstartX,-100)
for x in range(2):
    pencil.forward(10)
    pencil.right(5)
pencil.right(180)
pencil.pendown()
for x in range(50):
    pencil.forward(2)
    pencil.left(4.5)
pencil.penup()
pencil.home()
##H
pencil.setposition(CstartX+35,-100)
pencil.pendown()
pencil.right(90)
pencil.forward(50)
pencil.left(180)
pencil.forward(25)
pencil.right(90)
pencil.forward(20)
pencil.right(90)
pencil.forward(25)
pencil.right(180)
pencil.forward(50)
pencil.penup()
pencil.home()
##R
pencil.setposition(CstartX+70,-100)
pencil.right(90)
pencil.pendown()
pencil.forward(50)
pencil.right(180)
pencil.forward(50)
pencil.right(90)
for x in range(35):
    pencil.forward(1)
    pencil.right(5)
pencil.left(110)
pencil.forward(30)
pencil.penup()
pencil.home()
##I
pencil.setposition(CstartX+100,-100)
pencil.pendown()
pencil.right(90)
pencil.forward(50)
pencil.penup()
pencil.home()
##S
pencil.setposition(CstartX+110,-100)
pencil.forward(20)
for x in range(5):
    pencil.forward(1)
    pencil.right(5)
pencil.right(180)
pencil.pendown()
for x in range(42):
    pencil.forward(1)
    pencil.left(4.5)
for x in range(44):
    pencil.forward(1)
    pencil.right(4.5)
pencil.penup()
pencil.home()
##T
pencil.setposition(CstartX+145,-100)
pencil.pendown()
pencil.forward(20)
pencil.right(180)
pencil.forward(10)
pencil.left(90)
pencil.forward(50)
pencil.penup()
pencil.home()
##I
pencil.setposition(CstartX+180,-100)
pencil.pendown()
pencil.right(90)
pencil.forward(50)
pencil.penup()
pencil.home()
##A
pencil.setposition(CstartX+200,-150)
pencil.pendown()
pencil.left(80)
pencil.forward(52)
pencil.right(160)
pencil.forward(52)
pencil.right(180)
pencil.forward(20)
pencil.left(80)
pencil.forward(10)
pencil.penup()
pencil.home()
##N
pencil.setposition(CstartX+230,-150)
pencil.left(90)
pencil.pendown()
pencil.forward(50)
pencil.right(160)
pencil.forward(53)
pencil.left(160)
pencil.forward(53)
pencil.penup()
pencil.home()



turtle.mainloop()
