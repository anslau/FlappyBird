## Library
import turtle
import random
import time
import math

# set up screen
wn = turtle.Screen()
wn.setup(700, 400)

## Set up
t = turtle.Turtle()
wn = t.getscreen()
wn.bgcolor("sky blue")

# bird set up; bird facing up north
t.speed(0)
t.penup()
t.hideturtle()
t.goto(-170, 0)
t.showturtle()
t.left(90)
t.shape('circle')
t.color('yellow')

colors = ['lime green', 'gold', 'light salmon', 'plum', 'aquamarine', 'teal', 'dark orchid']
randColor = random.randrange(0, len(colors))

## Functions
#start game
def start_game():
  t.speed(3)

# flap
def flap():
  t.speed(3)
  t.forward(75)

# collides with obstacles
def obj_collide(a, b):
  return abs(a.xcor() - b.xcor()) < 17 and abs(a.ycor() - b.ycor()) < 17

# score counting by the obstacle the bird passes
def obj_pass(a, b):
  if (abs(a.xcor() - b.xcor()) or abs(b.xcor() - a.xcor()) == 0) and (obj_collide(a, b) == False):
    return True

##Explain Rules
print("Welcome to Flappy Bird! Press the enter key to continue.")
input()
print("Throughout this game, your yellow bird will face obstacles that it will have to cross. Press the space bar to make the bird jump and either go over or under the obstacles. If the bird doesn't jump for a long time, it will fall and you will lose a life! If the bird hits an obstacle, you will lose a life as well. You will have three lives to play the game & your total score will be displayed to you at the end of the game. Press the enter key to start the game and happy flapping!")
input()
wn.listen()
wn.onkey(start_game, 'enter')

## Generate Obstacles
# obj1:
obj1 = turtle.Turtle()
obj1.color("red")
obj1.hideturtle()
obj1.shape('triangle')
obj1.penup()
obj1.speed(0)
obj1.goto(150, -5)
obj1.showturtle()
# obj2
obj2 = turtle.Turtle()
obj2.color("lime green")
obj2.hideturtle()
obj2.shape('triangle')
obj2.penup()
obj2.speed(0)
obj2.goto(230, -80)
obj2.showturtle()
#obj3
obj3 = turtle.Turtle()
obj3.color("medium blue")
obj3.hideturtle()
obj3.shape('triangle')
obj3.penup()
obj3.speed(0)
obj3.goto(260, 60)
obj3.showturtle()
#obj4
obj4 = turtle.Turtle()
obj4.color("white")
obj4.hideturtle()
obj4.shape('triangle')
obj4.penup()
obj4.speed(0)
obj4.goto(390, -30)
obj4.showturtle()
#obj5
obj5 = turtle.Turtle()
obj5.color("moccasin")
obj5.hideturtle()
obj5.shape('triangle')
obj5.penup()
obj5.speed(0)
obj5.goto(450, -60)
obj5.showturtle()
#obj6
obj6 = turtle.Turtle()
obj6.color("spring green")
obj6.hideturtle()
obj6.shape('triangle')
obj6.penup()
obj6.speed(0)
obj6.goto(550, 20)
obj6.showturtle()
#obj7
obj7 = turtle.Turtle()
obj7.color("pink")
obj7.hideturtle()
obj7.shape('triangle')
obj7.penup()
obj7.speed(0)
obj7.goto(670, 70)
obj7.showturtle()
#objS
objS = turtle.Turtle()
objS.hideturtle()
objS.shape('turtle')
objS.penup()
objS.speed(0)
objS.left(180)
objS.goto(random.randrange(100, 301, 10), random.randrange(-160, 161, 10))

## Text display for lives
text = turtle.Turtle()
text.penup()
text.speed(0)
text.goto(-280, 150)
text.pendown()
style = ('Courier', 25, )
text.color("red") 
text.write('<3' * 3, font=style, align = 'left')
text.hideturtle()

# Pre-loop setting
keepGoing = True
lives = 3
score = 0

# Game Loop
while keepGoing:
  # Keyboard binding
  wn.listen() # listen for keyboard input
  # bind the player<>_up and player<>_down functions to keys on the keyboard
  # for example:
  wn.onkey(flap,"space") # when user presses "_" on keyboard call function player1_up

  # Constant falling motion of the bird
  t.speed(0)
  t.left(360) # To create some delay
  t.speed(2)
  t.backward(3)
 
  # Obstacles moving
  obj1.speed(4)
  obj1.backward(7.4)
  if obj1.xcor() <= -350:
    obj1.speed(0)
    # obj1 x y coords and colors randomized
    randColor = random.randrange(0, len(colors))
    obj1.color(colors[randColor])
    obj1.goto(random.randrange(80, 301, 4), random.randrange(-160, 161, 5))

  obj2.speed(4)
  obj2.backward(7.4)
  if obj2.xcor() <= -350:
    obj2.speed(0)
    # obj2 x y coords and colors randomized
    randColor = random.randrange(0, len(colors))
    obj2.color(colors[randColor])
    obj2.goto(random.randrange(80, 301, 4), random.randrange(-160, 161, 5))
  
  obj3.speed(4)
  obj3.backward(7.4)
  if obj3.xcor() <= -350:
    obj3.speed(0)
    # obj3 x y coords and colors randomized
    randColor = random.randrange(0, len(colors))
    obj3.color(colors[randColor])
    obj3.goto(random.randrange(80, 301, 4), random.randrange(-160, 161, 5))

  obj4.speed(random.randrange(4, 11))
  obj4.backward(8)
  if obj4.xcor() <= -350:
    obj4.speed(0)
    # obj4 x y coords and colors randomized
    randColor = random.randrange(0, len(colors))
    obj4.color(colors[randColor])
    obj4.goto(random.randrange(80, 301, 4), random.randrange(-160, 161, 5))

  obj5.speed(random.randrange(4, 11))
  obj5.backward(8)
  if obj5.xcor() <= -350:
    obj5.speed(0)
    # obj5 x y coords and colors randomized
    randColor = random.randrange(0, len(colors))
    obj5.color(colors[randColor])
    obj5.goto(random.randrange(80, 301, 4), random.randrange(-160, 161, 5))
  
  obj6.speed(random.randrange(4, 11))
  obj6.backward(8)
  if obj6.xcor() <= -350:
    obj6.speed(0)
    # obj6 x y coords and colors randomized
    randColor = random.randrange(0, len(colors))
    obj6.color(colors[randColor])
    obj6.goto(random.randrange(80, 301, 4), random.randrange(-160, 161, 5))
  
  obj7.speed(4)
  obj7.backward(7.4)
  if obj7.xcor() <= -350:
    obj7.speed(0)
    # obj7 x y coords and colors randomized
    randColor = random.randrange(0, len(colors))
    obj7.color(colors[randColor])
    obj7.goto(random.randrange(80, 301, 4), random.randrange(-160, 161, 5))

  # Surprise Obstacle (When Score >= 200)
  if score >= 200:
    randColor = random.randrange(0, len(colors))
    objS.color('red')
    objS.showturtle()
    objS.speed(16)
    objS.forward(20)
    if objS.xcor() <= -350:
      objS.speed(0)
      objS.goto(random.randrange(100, 301, 10), random.randrange(-160, 161, 10))

  # Calculate scores by counting the obstacles the bird passes
  if obj_pass(t, obj1) or obj_pass(t, obj2) or obj_pass(t, obj3) or obj_pass(t, obj4) or obj_pass(t, obj5) or obj_pass(t, obj6) or obj_pass(t, obj7) or obj_pass(t, objS):
    score += 1

  # Bottom Line & Collision detecting
  birdFall = t.ycor()

  if birdFall <= -200 or birdFall >= 200 or obj_collide(t, obj1) or obj_collide(t, obj2) or obj_collide(t, obj3) or obj_collide(t, obj4) or obj_collide(t, obj5) or obj_collide(t, obj6) or obj_collide(t, obj7) or obj_collide(t, objS):
    lives -= 1
    t.color('red')
    print("You have {} lives left.".format(lives))
    text.clear()
    text.write('<3' * lives, font=style, align = 'left')
    time.sleep(1)

  # lives detecting
    if lives < 1:
      print("Game Over.")
      print("Your total score is {} ".format(score))
      print("bye bye <3")
      keepGoing = False 
    else:
      retry = input('''Do you want to try again? ('yes' or 'no')\n''')
      time.sleep(1)
      t.speed(0)
      t.goto(-170, 150)
      if retry == 'yes':
        t.color("yellow")
        keepGoing = True
      if retry == 'no':
        print("Your total score is {} ".format(score))
        print("Ok Bye")
        keepGoing = False
      

input() # to keep the program running after the game finishes