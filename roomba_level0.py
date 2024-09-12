# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Niksa <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward
import room

# Draw the Level 0 version of the room
window = room.draw_room(level = 0)

###
# Start your code here
for _ in range(3):  
    forward(160)
    left(90)
for _ in range(2):
    forward(120)
    left(90)
for _ in range(2):
    forward(80)
    left(90)
forward(40)
left(90)
forward(40)
 
# End your code here
###
 
window.exitonclick()