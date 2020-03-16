# Author: Christopher Sozio
# Created: 3/14/2020
# Description: Simple Turtle graphics program that will allow students to understand the importance of functions

# Needed imports
import tkinter
import turtle

# Draws a rectangle with the provided parameters.
def draw_rectangle(x, y, width, height, color):
    turtle.color(color, color) # Set the background and foreground color of the line
    turtle.setposition(x, y) # Set the x and y position
    turtle.setheading(90) # Set direction of the point to North
    # Begin drawing
    turtle.begin_fill()
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.end_fill()

# Draws a triangle with the provided parameters. 
def draw_triangle(x, y, width, color):
    turtle.color(color, color) # Set the background and foreground color of the line
    turtle.setposition(x, y) # Set the x and y position
    turtle.setheading(90) # Set the direction of the point to North
    # Begin drawing
    turtle.begin_fill()
    turtle.right(45)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(width)
    turtle.end_fill()

# Draws a house with the provided parameters.
def draw_house(x, y, width, height, house_color, door_color, roof_color):
    # Draw the base of the house
    draw_rectangle(x, y, width, height, house_color)
    
    # Draw the door
    door_x = x + width / 3
    door_width = width / 3
    door_height = height / 2
    draw_rectangle(door_x, y, door_width, door_height, door_color)
    
    # Finally draw the roof
    roof_y = y + height
    roof_width = height + 5
    draw_triangle(x, roof_y, roof_width, roof_color)


""" --------------------------------------------------------------------------------
This is phase three of drawing houses using Turtle graphics.

This final phase will solidify the importance of functions and how students can create
easier and more readable code as programmers.

------------------------------------------------------------------------------------
"""
first_x = 0
first_y = 0
second_x = -100
second_y = -150
width = 150
height = 100
house_color = 'brown'
door_color = 'red'
roof_color = 'black'
draw_house(first_x, first_y, width, height, house_color, door_color, roof_color)
draw_house(second_x,second_y,width, height, house_color, door_color, roof_color)


""" --------------------------------------------------------------------------------
This is phase two of drawing houses using Turtle graphics.

Taking from their previous blocks of code to draw their houses, students
will learn to find similarities in their code to eventually create functions
out of those similarities. Phase two is the main step in describing why
functions are fundamental to writing code. This phase will also teach students
what parameters are and how useful they are with functions.

------------------------------------------------------------------------------------

# Create variables to pass to the function
x = 0
y = 0
width = 150
height = 100
color = 'brown'

# Draw first house

draw_rectangle(x,y,width,height,color) # Base House

# Also show students that you can pass data directly to functions
draw_rectangle(50,0,50,50,'red') # Door
draw_triangle(0,100,105, 'black') # Roof

# Draw second house

draw_rectangle(-100, -150, width, height, color) # Base House
draw_rectangle(-50, -150, 50, 50, 'red') # Door
draw_triangle(-100, -50, 105, 'black') # Roof
"""


""" --------------------------------------------------------------------------------
This is phase one of drawing houses using Turtle graphics.

Using the Turtle graphics library students will draw two houses
without creating any functions to help them out. This phase is to help
show students how tedious writing the same blocks of code can be for
programmers. This will help start the discussion of creating functions
for these blocks of code.

------------------------------------------------------------------------------------

# Draw the first house.

# Draw the house base
turtle.color('brown', 'brown')
turtle.setposition(0, 0)
turtle.setheading(90)
turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(150)
turtle.end_fill()

# Draw the door
turtle.color('red', 'red')
turtle.setposition(50, 0)
turtle.setheading(90)
turtle.begin_fill()
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.end_fill()

# Drawing the roof
turtle.color('black', 'black')
turtle.setposition(0, 100)
turtle.setheading(90)
turtle.begin_fill()
turtle.right(45)
turtle.forward(105)
turtle.right(90)
turtle.forward(105)
turtle.end_fill()

# Draw the second house.

# Draw house base
turtle.color('brown', 'brown')
turtle.setposition(-100, -150) #-100, -50
turtle.setheading(90)
turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(150)
turtle.end_fill()

# Draw the door
turtle.color('red', 'red')
turtle.setposition(-50, -150)
turtle.setheading(90)
turtle.begin_fill()
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.end_fill()


# Draw the roof
turtle.color('black', 'black')
turtle.setposition(-100, -50)
turtle.setheading(90)
turtle.begin_fill()
turtle.right(45)
turtle.forward(105)
turtle.right(90)
turtle.forward(105)
turtle.end_fill()
"""


# Used to finish Turtle drawing
turtle.done()
