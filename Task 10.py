import turtle # imports turtle to draw stuff
import random # imports random to generate random numbers for angles and scales

turtle.speed(0)  # sets turtle speed to the fastest
turtle.setheading(90)   # points turtle upwards
turtle.penup()
turtle.goto(0, -250)  # starts turtle at the bottom of the screen to fit bigger trees
turtle.pendown()

def randomfractaltree(n, length, angle, scale): # defines a function called randomfractaltree with 4 parameters: n, length, angle, and scale.
    if n < 1:  # if n is less than 1, the function stops and doesn't draw any more branches
        return
    turtle.forward(length)  # draws current branch
    
    # left branch
    new_angle_left = random.randint(-8, 8)  # adds random variation to the angle for the left branch
    new_scale_left = random.random() * 0.2 - 0.1   # adds random variation to the scale for the left branch
    turtle.left(angle + new_angle_left)  # turns left by the base angle plus the random variation
    randomfractaltree(n - 1, length * (scale + new_scale_left), angle, scale) # draws left branch with length based on random scale variation
    
    # right branch
    new_angle_right = random.randint(-8, 8)  # adds random variation to the angle for the right branch
    new_scale_right = random.random() * 0.2 - 0.1   # adds random variation to the scale for the right branch
    turtle.right((angle + new_angle_left) + (angle + new_angle_right))  # turns right past the left turn to the new right angle
    randomfractaltree(n - 1, length * (scale + new_scale_right), angle, scale) # draws right branch with length based on random scale variation
    
    # returns to original position to draw the next branch
    turtle.left(angle + new_angle_right)  # turns left to return to original direction  
    turtle.backward(length) # moves turtle back to the starting point of current branch to draw the next branch

randomfractaltree(10, 80, 30, 0.8)
turtle.done()  # keeps turtle window open until user closes it
