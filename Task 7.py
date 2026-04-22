import turtle  # imports turtle to draw stuff
turtle.setheading(90)  # points turtle upwards
turtle.penup()
turtle.goto(0, -250)  # starts turtle at the bottom of the screen to fit bigger trees
turtle.pendown()

def simpletree(n):  # defines a function called simpletree to draw a tree with n branches
    if n > 0: # if n is bigger than 0, it will draw the tree, otherwise it will stop
        turtle.forward(50) # draws current branch
    
        # left branch
        turtle.left(20)  # turns turtle left by 15 degrees
        simpletree(n-1)  # calls the function with n-1 to draw the left branch

        # right branch
        turtle.right(40)  # turns turtle right by 30 degrees
        simpletree(n-1)  # calls the function with n-1 to draw the right branch

        # returns to the original position and angle to draw the next branch
        turtle.left(20)
        turtle.backward(50)

simpletree(5)  # calls function with n as 6 as an example
turtle.done()  # keeps the turtle window open until user closes it
