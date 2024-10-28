# Tim Fisher
# 10/28/2024
# P4LAB1
# While loop to make a square using Turtle

# Import turtle library to use in code
import turtle
window = turtle.Screen()
zipper = turtle.Turtle()

# Set up the window and turtle shape
zipper.pensize(8)
zipper.pencolor("red")
zipper.shape("arrow")

# USE WHILE LOOP TO DRAW FOUR SIDES OF A SQUARE

line = 0
while line < 4:
    zipper.right(90)
    zipper.forward(100)
    line += 1
# For loop to draw triangle

for line1 in range(3):
    zipper.left(120)
    zipper.forward(100)
    
