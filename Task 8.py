import turtle  # imports turtle to draw stuff
turtle.speed(0)  # sets turtle speed to the fastest
turtle.setheading(90)   # points turtle upwards
turtle.penup()
turtle.goto(0, -250)  # starts turtle at the bottom of the screen to fit bigger trees
turtle.pendown()

def fractaltree(n, length, angle, scale):  # defines a function called fractaltree that takes 4 arguments: n, length, angle, and scale.
    # if n is less than 1, the function stops and doesn't draw any more branches
    if n < 1:
        return
    
    turtle.forward(length) # draws current branch

    # draws left branch
    turtle.left(angle) # left turn
    fractaltree(n-1, length * scale, angle, scale) # calls function to draw left branch
    
    # draws right branch
    turtle.right(angle * 2)  # right turn (angle * 2 to turn back to original direction and then right again)
    fractaltree(n-1, length * scale, angle, scale) # calls function to draw right branch
    
    # returns to original position to draw the next branch
    turtle.left(angle)  # left turn to original direction
    turtle.backward(length)  # moves turtle back to the starting point of current branch to draw the next branch

fractaltree(8,100,30,0.75)   # calls function with n as 8, length as 100, angle as 30, and scale as 0.75
turtle.done()  # keeps turtle window open until user closes it
