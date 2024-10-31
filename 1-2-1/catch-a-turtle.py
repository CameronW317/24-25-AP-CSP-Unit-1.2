# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand
#-----game configuration----
spot_color = "gray"
spot_size = 2
spot_shape = "circle"
score = 0

font_setup = ("Arial", 20, "bold")

timer = 30
counter_interval = 1000   #1000 represents 1 second
timer_up = False
#-----initialize turtle-----
spot = trtl.Turtle()
score_writer = trtl.Turtle()
counter = trtl.Turtle()

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

spot.shape(spot_shape)
spot.shapesize(spot_size)
spot.fillcolor(spot_color)
spot.pencolor("gold")


#-----game functions--------

def change_position():
    new_xpos = rand.randint(-400, 400)
    new_ypos = rand.randint(-300, 300)
    spot.goto(new_xpos,new_ypos)
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
def spot_clicked(x,y):
    global timer_up
    if timer_up == False:
        update_score()
        change_position()
    else:
        spot.hideturtle()


#-----events----------------

spot.onclick(spot_clicked)


wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)

wn.mainloop()