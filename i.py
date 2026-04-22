import turtle
import random

def randomfractaltree(n, length, angle, scale):
    """ 
    Recursive function to draw a fractal tree with random variation.
    Uses random.randint() and random.random() for natural-looking variation.
    """
    if n < 1:                    # Base case
        return
    
    turtle.forward(length)       # Draw current branch
    
    # Random variation for LEFT branch
    rand_angle_l = random.randint(-8, 8)
    rand_scale_l = random.random() * 0.14 - 0.07     # small random change
    
    turtle.left(angle + rand_angle_l)
    randomfractaltree(n - 1, length * (scale + rand_scale_l), angle, scale)
    
    # Random variation for RIGHT branch
    rand_angle_r = random.randint(-8, 8)
    rand_scale_r = random.random() * 0.14 - 0.07
    
    turtle.right((angle + rand_angle_l) + (angle + rand_angle_r))
    randomfractaltree(n - 1, length * (scale + rand_scale_r), angle, scale)
    
    # Go back to starting position
    turtle.left(angle + rand_angle_r)
    turtle.backward(length)


# ==================== Setup ====================
turtle.speed(0)
turtle.pensize(3)
turtle.color("darkgreen")

turtle.penup()
turtle.goto(0, -350)           # Start lower to prevent tree from going off screen
turtle.setheading(90)
turtle.pendown()

# ==================== Test as required ====================
randomfractaltree(10, 80, 30, 0.8)

turtle.done()