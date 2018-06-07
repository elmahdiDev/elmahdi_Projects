'''
APP Control:
Use up , down , right ad left keys to move with the pencil
Use Space bar to pen up and down
Use r key to change to red color
Use b key to change to blue color
Use g key to change to green color
Use y key to change to yellow color
Use w key to change to white color
To close the app write any thing on the console
<<<  this app should be started with a console not a text editor because it will crash use gitbash if you have it >>>
'''
import turtle
import os

#creating screen
wn=turtle.Screen()
wn.bgcolor("black")

#creating pencil
pencil = turtle.Turtle()
pencil.color("white")
pencil.speed(0)
pencil.setheading(90)
pencil.penup()
penupy=True

#creating movement functions
def move_left():
	pencil.left(10)
def move_right():
	pencil.right(10)
def move_up():
	pencil.fd(10)
def move_down():
	pencil.back(10)

#changing color functions
def red():
	pencil.color("red")
def blue():
	pencil.color("blue")
def yellow():
	pencil.color("yellow")
def green():
	pencil.color("green")
def white():
	pencil.color("white")

#penup and down function
def pen_up_down():
	global penupy
	if penupy==True:
		pencil.pendown()
		penupy=False
	elif penupy==False:
		pencil.penup()
		penupy=True

#pencil system
turtle.listen()
turtle.onkey(move_right,"Right")
turtle.onkey(move_up,"Up")
turtle.onkey(move_left,"Left")
turtle.onkey(move_down,"Down")
turtle.onkey(red,"r")
turtle.onkey(blue,"b")
turtle.onkey(yellow,"y")
turtle.onkey(green,"g")
turtle.onkey(white,"w")
turtle.onkey(pen_up_down,"space")

#this input to make the app open
raw_input("promt: ")
