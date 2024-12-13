#Cameron and Gio
import turtle
import random

# Add game elements
weakpoint = turtle.Turtle()
wn = turtle.Screen()
boxer_trtl = turtle.Turtle()
score_writer = turtle.Turtle()
counter = turtle.Turtle()
message_turtle = turtle.Turtle()

#Variables
weakpoint_shape = "circle"
weakpoint_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
boxer_shape = "giphy.gif"
weakpoint_size = 2
weakpoint_xcoor = [0, -175, -25, 25, -100, 0, -60]
weakpoint_ycoor = [75, 50, 25, 25, -25, -25, -125]

messages = ["WOW!", "NICE!", "EXCELLENT!", "CRITICAL!", "AMAZING!", "DESTRUCTIVE!", "INSANE!", "GREAT!", "POWERFUL!", "EXPLOSIVE!", "BOOM!", "DEVASTATING!", "SHOCKING!", "SPOT ON!", "ALRIGHT!", "SLICK!", "DEADLY!"]
message_colors = ['red' , 'orange' , 'yellow' , 'blue' , 'gold' , 'cyan' , 'magenta']
score = 0

font_setup = ("Impact", 20, "bold")
final_message_font_setup = ("Impact", 30, "bold")
timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
# Prepare Turtles
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

message_turtle.speed("fastest")
message_turtle.hideturtle()

wn.bgcolor("#A9A9A9")
wn.addshape(boxer_shape)


# Add opponent

def draw_boxer(active_boxer):
  active_boxer.shape(boxer_shape)
  boxer_trtl.showturtle()
  wn.update()
# Updating the score every hit
def update_score():
  global score
  score_writer.clear()
  score += 100
  score_writer.write(score, font=font_setup)
# The timer in top right
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
# When the weak point is clicked
def click_weakpoint(x, y):

  global timer_up
  if timer_up == False:
    update_score()
    draw_weakpoint()
    hit_messages()
  else:
    message_turtle.clear()
    weakpoint.hideturtle()
    weakpoint.penup()
    weakpoint.goto(-200, 0)
    weakpoint.pendown()
    boxer_trtl.hideturtle()
    if score > 3500:
      wn.bgcolor("#B59410")
      weakpoint.color("Yellow")
      weakpoint.write("You are a champion!", font=final_message_font_setup)
    else:
      wn.bgcolor("#0071B6")
      weakpoint.color("#89CFF0")
      weakpoint.write("You put up a good fight", font=final_message_font_setup)
# Drawing weak points after every hit
def draw_weakpoint():
  global weakpoint_xcoor, weakpoint_ycoor
  random_coordinate = random.randint(0,6)
  weakpoint.hideturtle()
  weakpoint.color(random.choice(weakpoint_colors))
  weakpoint.goto(weakpoint_xcoor[random_coordinate], weakpoint_ycoor[random_coordinate])
  weakpoint.showturtle()
# Drawing the messages on screen
def hit_messages():

  message_turtle.clear()
  random_message = random.choice(messages)
  random_color = random.choice(message_colors)
  message_turtle.penup()
  message_turtle.goto(random.randint(150, 300), random.randint(-300, 200))
  message_turtle.color(random_color)
  message_turtle.write(random_message, font=font_setup)

# Incorporate weak points
#def generate_weakpoint(xcoor, ycoor):

draw_boxer(boxer_trtl)
weakpoint.onclick(click_weakpoint)
wn.ontimer(countdown, counter_interval)
wn.mainloop()