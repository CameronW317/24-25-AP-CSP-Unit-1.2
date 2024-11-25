import turtle

wn=turtle.Screen()
drawer = turtle.Turtle()



length_of_walls = 40
for iterations in range(25):
    drawer.left(90)
    drawer.forward(length_of_walls)
    length_of_walls += 20



wn.mainloop()