from turtle import Turtle, Screen
import random

jimmy = Turtle()
screen = Screen()
screen.colormode(255)  # this is used because the screen is not taking the color mode.       Explanation -
# Default Color Mode: The default color mode in Turtle is set to 1.0, which means it expects color values between 0 and 1
# Setting Color Mode: By setting screen.colormode(255), you allow the use of RGB values ranging from 0 to 255



direction = [0, 90, 180, 270]
jim_width = 1
jim_speed = 2

def random_color():

    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    tuple_color = (r,g,b)
    return tuple_color


for _ in range(400):
    jimmy.width(jim_width)
    jimmy.speed(jim_speed)
    jimmy.pencolor((random_color())) # evertime give a random color
    jimmy.forward(20)
    jimmy.setheading(random.choice(direction))
    jim_width += 0.05 # everytime width increases
    jim_speed += 0.5 # everytime speed increases





screen.exitonclick()
