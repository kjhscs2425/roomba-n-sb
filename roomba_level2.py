# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Niksa <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(7)

# Draw the Level 2 version of the room
window = room.draw_room(level = 2)

###
# Start your code here
for _ in range(1):
    forward(560)
    left(90)
    forward(760)
    left(90)
for _ in range (1):
    forward(560)
    left(90)
    forward(720)
    left (90)
for _ in range (1):
    forward(520)
    left(90)
    forward(680)
    left(90)
    forward(640) #x
    left(90)
    forward(480) #y
    left(90)
    
 
 
# End your code here
###
 
window.exitonclick()