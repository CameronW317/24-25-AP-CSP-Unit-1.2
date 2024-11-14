#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image)

apple = trtl.Turtle()
pear = trtl.Turtle()
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()
def draw_pear(active_pear):
  active_pear.shape(pear_image)
  pear.penup()
  pear.goto(100,0)
  pear.pendown()
  wn.update()
def apple_down(active_apple):
  apple.goto(active_apple.xcor(), active_apple.ycor())
  apple.down()


#-----function calls-----
draw_apple(apple)
draw_pear(pear)
apple_down(apple)
wn.bgpic("background.gif")
wn.mainloop()