# STARFIELD

import random
import turtle
import math

# Set up the turtle
turtle.speed(0)
turtle.bgcolor("black")
turtle.ht()
# This saves memory
turtle.setundobuffer(20)
# This speeds up drawing
turtle.tracer(900)


def pos2frac(x, y):
    r = 802
    f = ((x ** 2) + (y ** 2)) ** (0.5)
    return (f / r)


class Streak(turtle.Turtle):
    def __init__(self, color,):
        turtle.Turtle.__init__(self)
        self.ht()


class Stars(turtle.Turtle):
    def __init__(self, starshape, size, color, x, y, z):
        turtle.Turtle.__init__(self, shape=starshape)
        self.shapesize(0.01)
        self.speed(0)
        self.penup()
        self.color(color)
        self.x = x
        self.y = y
        self.shapesize(size / 10)
        self.goto(x, y)
        self.speed = 10
        # self.arctan = math.atan2(y, x)
        # self.degree = (180 / 3.14) * self.arctan
        # self.setheading(self.degree)

    def move(self):
        self.arctan = math.atan2(self.ycor(), self.xcor())
        self.degree = (180 / 3.14) * self.arctan
        self.setheading(self.degree)

        self.shapesize((.2) * pos2frac(self.xcor(), self.ycor()))

        self.speed = 15 * pos2frac(self.xcor(), self.ycor())
        self.fd(self.speed)

        # Boundary Checking
        if self.xcor() > 750:
            self.setposition(random.randint(-300, 300), random.randint(-300, 300))
        if self.xcor() < -750:
            self.setposition(random.randint(-300, 300), random.randint(-300, 300))
        if self.ycor() > 450:
            self.setposition(random.randint(-300, 300), random.randint(-300, 300))
        if self.ycor() < -450:
            self.setposition(random.randint(-300, 300), random.randint(-300, 300))


number = 400

stars = []
for i in range(number):
    stars.append(Stars("circle", 1, "white", random.randint(-700, 700), random.randint(-400, 400), 0))


while True:
    for star in stars:
        star.move()


turtle.mainloop()
