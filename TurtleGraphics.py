#TurtleGraphics.py
#Name: Jaylen Atsou
#Date: Feburary 15, 2026
#Assignment: Lab 4

import turtle 

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(myTurtle, sides):
    myTurtle.penup()
    myTurtle.goto(-50, 50)
    myTurtle.pendown()

    angle = 360 / sides
    length = 50

    for i in range(sides):
        myTurtle.forward(length)
        myTurtle.right(angle)

def fillCorner(myTurtle, corner):
    size = 200
    half = size / 2

    myTurtle.penup()
    myTurtle.goto(-100, 100)
    myTurtle.pendown()

    drawSquare(myTurtle, size)

    myTurtle.penup()

    if corner == 1:
        myTurtle.goto(-100, 100)
    elif corner == 2:
        myTurtle.goto(0, 100)
    elif corner == 3:
        myTurtle.goto(-100, 0)
    elif corner == 4:
        myTurtle.goto(0, 0)

    myTurtle.pendown()
    myTurtle.begin_fill()
    drawSquare(myTurtle, half)
    myTurtle.end_fill()


def squaresInSquares(myTurtle, num):
    size = 200

    myTurtle.penup()
    myTurtle.goto(-100, 100)
    myTurtle.pendown()

    for i in range(num):
        drawSquare(myTurtle, size)

        myTurtle.penup()
        myTurtle.forward(10)
        myTurtle.right(90)
        myTurtle.forward(10)
        myTurtle.left(90)
        myTurtle.pendown()

        size -= 20

def main():
    myTurtle = turtle.Turtle()
    myTurtle.hideturtle()
    myTurtle.speed(0)

    drawPolygon(myTurtle, 5) 

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


def drawPolygon(myTurtle, sides):
    myTurtle.penup()
    myTurtle.goto(-50, 50)
    myTurtle.pendown()

    angle = 360 / sides
    length = 50

    for i in range(sides):
        myTurtle.forward(length)
        myTurtle.right(angle)

def fillCorner(myTurtle, corner):
    size = 200
    half = size / 2

    myTurtle.penup()
    myTurtle.goto(-100, 100)
    myTurtle.pendown()

    drawSquare(myTurtle, size)

    myTurtle.penup()

    if corner == 1:
        myTurtle.goto(-100, 100)
    elif corner == 2:
        myTurtle.goto(0, 100)
    elif corner == 3:
        myTurtle.goto(-100, 0)
    elif corner == 4:
        myTurtle.goto(0, 0)

    myTurtle.pendown()
    myTurtle.begin_fill()
    drawSquare(myTurtle, half)
    myTurtle.end_fill()

def squaresInSquares(myTurtle, num):
    size = 200

    myTurtle.penup()
    myTurtle.goto(-100, 100)
    myTurtle.pendown()

    for i in range(num):
        drawSquare(myTurtle, size)

        myTurtle.penup()
        myTurtle.forward(10)
        myTurtle.right(90)
        myTurtle.forward(10)
        myTurtle.left(90)
        myTurtle.pendown()

        size -= 20


def main():
    myTurtle = turtle.Turtle()
    myTurtle.hideturtle()
    myTurtle.speed(0)

    fillCorner(myTurtle, 2) 
 

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


def drawPolygon(myTurtle, sides):
    myTurtle.penup()
    myTurtle.goto(-50, 50)
    myTurtle.pendown()

    angle = 360 / sides
    length = 50

    for i in range(sides):
        myTurtle.forward(length)
        myTurtle.right(angle)


def fillCorner(myTurtle, corner):
    size = 200
    half = size / 2

    myTurtle.penup()
    myTurtle.goto(-100, 100)
    myTurtle.pendown()

    drawSquare(myTurtle, size)

    myTurtle.penup()

    if corner == 1:
        myTurtle.goto(-100, 100)
    elif corner == 2:
        myTurtle.goto(0, 100)
    elif corner == 3:
        myTurtle.goto(-100, 0)
    elif corner == 4:
        myTurtle.goto(0, 0)

    myTurtle.pendown()
    myTurtle.begin_fill()
    drawSquare(myTurtle, half)
    myTurtle.end_fill()


def squaresInSquares(myTurtle, num):
    size = 200

    myTurtle.penup()
    myTurtle.goto(-100, 100)
    myTurtle.pendown()

    for i in range(num):
        drawSquare(myTurtle, size)

        myTurtle.penup()
        myTurtle.forward(10)
        myTurtle.right(90)
        myTurtle.forward(10)
        myTurtle.left(90)
        myTurtle.pendown()

        size -= 20


def main():
    myTurtle = turtle.Turtle()
    myTurtle.hideturtle()
    myTurtle.speed(0)

    squaresInSquares(myTurtle, 5)


main()
