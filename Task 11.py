import turtle # imports turtle to draw stuff
import random # imports random to generate random numbers for angles and scales

turtle.speed(0)  # sets turtle speed to the fastest
turtle.setheading(90)   # points turtle upwards
turtle.penup()
turtle.goto(0, -250)  # starts turtle at the bottom of the screen to fit bigger trees
turtle.pendown()

def randomfractaltree(n, length, angle, scale, randomness): # defines a function called randomfractaltree with 5 parameters: n, length, angle, scale, and randomness.
    if n < 1:  # if n is less than 1, the function stops and doesn't draw any more branches
        return
    
    turtle.forward(length)  # draws current branch
    # left branch
    new_angle_left = random.randint(-randomness, randomness)  # adds random variation to the angle for the left branch
    new_scale_left = random.random()  # adds random variation to the scale for the left branch
    turtle.left(angle + new_angle_left)  # turns left by the base angle plus the random variation
    randomfractaltree(n - 1, length * (scale + new_scale_left), angle, scale, randomness) # draws left branch with length based on random variation
    
    # right branch
    new_angle_right = random.randint(-randomness, randomness)  # adds random variation to the angle for the right branch
    new_scale_right = random.random()  # adds random variation to the scale for the right branch
    turtle.right((angle + new_angle_left) + (angle + new_angle_right))  # turns right past the left turn to the new right angle
    randomfractaltree(n - 1, length * (scale + new_scale_right), angle, scale, randomness) # draws right branch with length based on random variation
    
    # returns to original position to draw the next branch
    turtle.left(angle + new_angle_right)  # turns left to return to original direction  
    turtle.backward(length) # moves turtle back to the starting point of current branch to draw the next branch

def menu(): # defines another function called menu to draw a tree based on user input
  # gets user input for tree parameters
    n = int(input("Enter tree level: "))
    length = int(input("Enter starting branch length: "))
    angle = int(input("Enter angle between branches: "))
    scale = float(input("Enter scale factor: "))
    thickness = int(input("Enter pensize: "))
    pencolour = input("Enter pen colour: ")
    randomness = int(input("Enter randomness level (0 to 20 recommended): "))
    
    turtle.pensize(thickness) # sets the pen thickness based on user input
    turtle.color(pencolour) # sets the pen colour based on user input

    randomfractaltree(n, length, angle, scale, randomness)   # calls the function and draws the tree based on user input
menu()  # calls the menu function to start the program
turtle.done()  # keeps turtle window open until user closes it
