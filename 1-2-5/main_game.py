import turtle
import random

# Add game elements
weakpoint = turtle.Turtle()
wn = turtle.Screen()
boxer_trtl = turtle.Turtle()
score_writer = turtle.Turtle()
counter = turtle.Turtle()
message_tutle = turtle.Turtle()

weakpoint_shape = "circle"
weakpoint_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
boxer_shape = "giphy.gif"
weakpoint_size = 2
weakpoint_xcoor = [0, -200, -25, 25, -100, 0, -100]
weakpoint_ycoor = [75, 50, 25, 25, -25, -25, -150]

score = 0

font_setup = ("Arial", 20, "bold")

timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
# Establish setting

counter.speed("fastest")
counter.penup()
counter.goto(300,300)
counter.pendown()
counter.hideturtle()

score_writer.speed("fastest")
score_writer.penup()
score_writer.goto(-400,300)
score_writer.pendown()
score_writer.hideturtle()

weakpoint.speed("fastest")
weakpoint.shape(weakpoint_shape)
weakpoint.color(random.choice(weakpoint_colors))
weakpoint.shapesize(weakpoint_size)
weakpoint.penup()
weakpoint.goto(0, 75)


wn.bgcolor("#A9A9A9")
wn.addshape(boxer_shape)


# Add opponent
def draw_boxer(active_boxer):
  active_boxer.shape(boxer_shape)
  boxer_trtl.showturtle()
  wn.update()

def update_score():
  global score
  score_writer.clear()
  score += 100
  score_writer.write(score, font=font_setup)
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)
def click_weakpoint():
  global timer_up
  if timer_up == False:
    update_score()
    countdown()
    draw_weakpoint()
  else:
    weakpoint.hideturtle()
    weakpoint.penup()
    weakpoint.goto(-200, 0)
    weakpoint.pendown()
    boxer_trtl.hideturtle()
    if score > 3000:
      weakpoint.write("You are a champion!", font=font_setup)
    else:
      weakpoint.write("You put up a good fight", font=font_setup)
def draw_weakpoint():
  global weakpoint_xcoor, weakpoint_ycoor
  random_coordinate = random.randint(0,6)
  weakpoint.hideturtle()
  weakpoint.goto(weakpoint_xcoor[random_coordinate], weakpoint_ycoor[random_coordinate])
  weakpoint.showturtle()

# Incorporate weak points
#def generate_weakpoint(xcoor, ycoor):



draw_boxer(boxer_trtl)
weakpoint.onclick(click_weakpoint)
wn.mainloop()