import turtle as t
import random as rand

# Initialize Variables
wn = t.Screen()
maze_painter = t.Turtle()

path_width = 30
wall_color = "black"
wall_length = 35





# Setup Turtle
maze_painter.pencolor(wall_color)
maze_painter.speed(0)
maze_painter.pensize(5)
maze_painter.hideturtle()
maze_painter.left(90)


#Draw Maze
'''
Process:
Draw a line
Turn Left
Increment Length
Repeat
'''
def draw_barrier():
    maze_painter.right(90)
    maze_painter.forward(path_width)
    maze_painter.back(path_width)
    maze_painter.left(90)

for wall in range(21):
    gap_space = rand.randint(0, wall_length - path_width)
    door_space = 0
    maze_painter.forward(gap_space)
    maze_painter.penup()
    maze_painter.forward(path_width)
    maze_painter.pendown()
    if(wall > 5):
        door_space = rand.randint(0, wall_length - path_width - gap_space)
        maze_painter.forward(door_space)
        draw_barrier()
    maze_painter.forward(wall_length - gap_space - path_width - door_space)
    maze_painter.left(90)
    wall_length += 15



wn.mainloop()