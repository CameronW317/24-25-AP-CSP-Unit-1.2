import turtle as t



num_walls = 20
path_width = 10
wall_color = "black"
wall_length = 20
barrier_length = (path_width * 2)

maze_painter = t.Turtle()
maze_painter.pencolor(wall_color)
maze_painter.speed(0)
maze_painter.hideturtle()


for num in range(num_walls):
    maze_painter.left(90)
    maze_painter.forward(wall_length)
    wall_length += path_width
    if num in range(num_walls):
        maze_painter.forward(10)
        maze_painter.penup()
        maze_painter.forward(10)
        maze_painter.pendown()



wn = t.Screen()
wn.mainloop()