"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Jake Powell.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
first_turtle = rg.SimpleTurtle()
first_turtle.pen = rg.Pen('blue',6)
first_turtle.speed = 7
size = 100
for k in range(8):
    first_turtle.draw_square(size)
    first_turtle.pen_up()
    first_turtle.right(30)
    first_turtle.forward(20)
    first_turtle.left(45)
    first_turtle.pen_down()
    size = size - 5
window.tracer(100)
second_turtle = rg.SimpleTurtle('circle')
second_turtle.pen = rg.Pen('green',4)
second_turtle.speed = 5
for k in range(200):
    second_turtle.forward(35)
    second_turtle.right(35)
    second_turtle.backward(10)
    second_turtle.forward(k)
window.close_on_mouse_click()
