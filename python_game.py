import os
import random

import turtle
turtle.fd(0)
turtle.speed(0)
turtle.bgcolor("black")
turtle.ht()
turtle.setundobuffer(1)
turtle.tracer(1)

class Sprite(turtle.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)
        self.speed = 1

    def move(self):
        self.fd(self.speed)

        if self.xcor() > 255:
            self.setx(255)
            self.rt(60)

        if self.xcor() < -235:
            self.setx(-235)

            self.rt(60)

        if self.ycor() > 255:
            self.sety(255)
            self.rt(60)

        if self.ycor() < -235:
            self.sety(-235)
            self.rt(60)

    def is_collision(self, other):
        if (self.xcor() >= (other.xcor() - 20)) and \
        (self.xcor() <= (other.xcor() + 20)) and \
        (self.ycor() >= (other.ycor() - 20)) and \
        (self.ycor() >= (other.ycor() - 20)):
            return True
        else:
            return False

class Player(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        self.lt(45)

    def turn_right(self):
        self.rt(45)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1

class Enemy(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 6
        self.setheading(random.randint(0, 360))

class Ally(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.speed = 8
        self.setheading(random.randint(0, 360))

    def move(self):
        self.fd(self.speed)

        if self.xcor() > 255:
            self.setx(255)
            self.lt(60)

        if self.xcor() < -235:
            self.setx(-235)
            self.lt(60)

        if self.ycor() > 255:
            self.sety(255)
            self.lt(60)

        if self.ycor() < -235:
            self.sety(-235)
            self.lt(60)

class Missile(Sprite):
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_len=0.4, stretch_wid=0.3, outline=None)
        self.speed = 40
        self.status = "ready"
        self.goto(-1000, 1000)

    def fire(self):
        if self.status == "ready":
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"

    def move(self):

        if self.status == "ready":
            self.goto(-1000, 1000)

        if self.status == "firing":
            self.fd(self.speed)

        if self.xcor() < -235 or self.xcor() > 255 or \
            self.ycor() < -235 or self.ycor() > 255:
            missile.goto(-1000, 1000)
            self.status = "ready"

class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-250, 265)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(520)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()

    def show_status(self):
        self.pen.undo()
        msg = "Score: %s" %(self.score)
        self.pen.penup()
        self.pen.goto(-245, 280)
        self.pen.write(msg, font=("Arial", 16, "normal"))

game = Game()

game.draw_border()

game.show_status()

player = Player("triangle", "white", 0, 0)
enemy = Enemy("circle", "red", -100, 0)
missile = Missile("triangle", "yellow", 0, 0)
ally = Ally("square", "blue", 0, 0)


turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(missile.fire, "space")
turtle.listen()


while True:
    player.move()
    enemy.move()
    missile.move()
    ally.move()


    if player.is_collision(enemy):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        enemy.goto(x, y)

    if missile.is_collision(enemy):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        enemy.goto(x, y)
        game.score += 100
        game.show_status()


    if missile.is_collision(ally):
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        ally.goto(x, y)
        game.score -= 50
        game.show_status()





delay = raw_input("Press enter to finish. >")