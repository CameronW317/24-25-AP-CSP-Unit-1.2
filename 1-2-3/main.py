##############################################################################
#   a123_TR_apple_typing_3.py
#   Run code in VS Code to be able to access the images.
#   Example soulution:
#      Code connects to the image of an apple.
#      The apple is located on the image of a tree.
#      The apple does not draw a line as it falls.
#      When A is pressed, the letter A appears on the apple.
#      The apple falls to the ground when the A key is pressed.
#      The apple and letter dissapear after the apple hits the ground.
##############################################################################
import turtle as trtl
import random as rand
apple_image = "apple.gif" # Store the file name of your shape
ground_height = -200
apple_letter_x_offset = -25
apple_letter_y_offset = -50


wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file


wn.bgpic("background.gif")
apple = trtl.Turtle()
apple.penup()
wn.tracer(False)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

number_of_apples = len(letters)
# given a turtle, active_apple, set that turtle to be shaped
# by the image file
def draw_apple(active_apple, letter):
  active_apple.shape(apple_image)
  draw_letter(letter, active_apple)
  apple.showturtle()
  wn.update()

# This function moves the apple to the ground and hides it.
def drop_apple():
  wn.tracer(True)
  apple.goto(apple.xcor(), ground_height)
  apple.clear()
  apple.hideturtle()
  wn.tracer(False)
  reset_apple(apple)


#   a123_apple_letters.py
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the
# turtle with a new letter selected at random from the list of letters

def reset_apple(apple):
  if len(letters) > 0:
    newX = rand.randint(-200, 200)
    newY = 0
    new_letter = rand.randint(0, len(letters))
    apple.goto(newX, newY)
    draw_apple(apple,letters.pop(new_letter))


#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)




#TODO Create a function that takes a turtle (apple) and its corresponding ltter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen

#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
#for i in range(0, number_of_apples):
  #Your code here

#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the
# apple and letter have dropped, call the apple reseting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.




# letter is of type str
# active_apple is a turtle
def draw_letter(letter, active_apple):
  active_apple.color("white")
  remember_position = active_apple.position()
  active_apple.setpos(active_apple.xcor() + apple_letter_x_offset,active_apple.ycor() + apple_letter_y_offset)
  active_apple.write(letter, font=("Arial", 74, "bold"))
  active_apple.setpos(remember_position)

draw_apple(apple, "A")
wn.onkeypress(drop_apple, 'a')

wn.listen()
trtl.mainloop()