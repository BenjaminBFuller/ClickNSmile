#ClickAndSmile.py
import random
import turtle
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")
colors = ["red", "blue", "green", "purple", "maroon", "aqua"]

def draw_smiley(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    draw_face()
    draw_righteye()
    draw_lefteye()
    draw_mouth()

def draw_face():
    t.penup()
    t.goto(x,y)
    t.setheading(0)
    t.pendown()
    t.pencolor(random.choice(colors))
    t.fillcolor(random.choice(colors))
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    
def draw_lefteye():
    t.penup()
    t.goto(x-15, y+60)
    t.pendown()
    t.fillcolor(random.choice(colors))
    t.begin_fill()
    t.circle(10)
    t.end_fill()

def draw_righteye():
    t.penup()
    t.goto(x+15, y+60)
    t.pendown()
    t.fillcolor(random.choice(colors))
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    
def draw_mouth():
    t.penup()
    t.goto(x-25, y+35)
    t.pencolor("black")
    t.setheading(300)
    t.width(3)
    t.pendown()
    t.circle(30, 120)
    t.penup()

def getcoordinates():
    turtle.onscreenclick(gatherdata)
    # when click on screen, points to mo

def gatherdata(rawx,rawy):
    global x, y # declares for global use throughout program
    x = int(rawx//1) # sets x to x coord of mouse click
    y = int(rawy//1) # sets y to y coord of mouse click
    draw_smiley(x,y) # draw smiley function

getcoordinates()
