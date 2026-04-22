import turtle
import random   # Needed for randomness

def randomfractaltree(n, length, angle, scale):
    """ 
    Draws a fractal tree with random variation in angle and scale factor.
    This makes each tree look slightly different every time it is drawn.
    """
    if n < 1:                      # Base case: stop recursion
        return
    
    turtle.forward(length)         # Draw the current branch
    
    # === Random variation for left branch ===
    random_angle_left = angle + random.uniform(-8, 8)   # ±8 degrees variation
    random_scale_left = scale + random.uniform(-0.08, 0.08)  # small variation in scale
    
    turtle.left(angle + random_angle_left)
    randomfractaltree(n - 1, length * random_scale_left, angle, scale)
    
    # === Random variation for right branch ===
    random_angle_right = angle + random.uniform(-8, 8)
    random_scale_right = scale + random.uniform(-0.08, 0.08)
    
    turtle.right((angle + random_angle_left) + (angle + random_angle_right))   # Return past the left turn
    randomfractaltree(n - 1, length * random_scale_right, angle, scale)
    
    # Return to original position
    turtle.left(angle + random_angle_right)
    turtle.backward(length)


turtle.speed(0)  # Fastest speed
turtle.setheading(90)  # Point upwards 
turtle.penup()
turtle.goto(0, -250)  # Start at the bottom center
turtle.pendown()
randomfractaltree(10, 80, 30, 0.8)  # Draw the tree with specified parameters
turtle.done()  # Keep the window open until closed by the user