import turtle  # imports turtle to draw stuff
turtle.speed(0)  # sets turtle speed to the fastest
turtle.setheading(90)  # points turtle upwards
turtle.penup()
turtle.goto(0, -250)  # starts turtle at the bottom centre to fit bigger trees
turtle.pendown()

def simpletree(n, length, angle, scale): # makes a function called simpletree that takes 4 arguments: n, length, angle, and scale.
    # if n is less than 1, the function stops and doesn't draw any more branches
    if n < 1:
        return
    turtle.forward(length) # draws current branch

    turtle.left(angle) # left turn
    simpletree(n-1, length * scale, angle, scale) # calls function to draw left branch
    
    turtle.right(angle * 2)  # right turn (angle * 2 to turn back to original direction and then right again)
    simpletree(n-1, length * scale, angle, scale) # calls function to draw right branch
    
    turtle.left(angle)  # left turn to original direction
    turtle.backward(length)  # moves turtle back to the starting point of current branch to draw the next branch

def menu(): # defines another function called menu to draw a tree based on user input
  # gets user input for tree parameters
    n = int(input("Enter tree level: "))
    length = int(input("Enter starting branch length: "))
    angle = int(input("Enter angle between branches: "))
    scale = float(input("Enter scale factor: "))
    simpletree(n, length, angle, scale)   # calls the function and draws the tree based on user input

menu()  # calls the menu function to start the program
turtle.done()  # keeps turtle window open until user closes it
