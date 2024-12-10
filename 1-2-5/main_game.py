import turtle

# Add game elements
weakpoint = turtle.Turtle()
wn = turtle.Screen()
boxer_trtl = turtle.Turtle()

weakpoint_shape = "circle"
weakpoint_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
boxer_shape = "giphy.gif"
weakpoint_xcoor = [0, -200, -25, 25, -100, 0, -100]
weakpoint_ycoor = [75, 50, 25, 25, -25, -25, -150]
# Establish setting
wn.bgcolor("#A9A9A9")
wn.addshape(boxer_shape)


# Add opponent
def draw_boxer(active_boxer):
  active_boxer.shape(boxer_shape)
  boxer_trtl.showturtle()
  wn.update()

# Incorporate weak points
#def generate_weakpoint(xcoor, ycoor):



draw_boxer(boxer_trtl)
wn.mainloop()