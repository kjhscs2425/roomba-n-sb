# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(7)

# Draw the Level 4 version of the room
window = room.draw_room(level = 4, n_alcoves = 1, radius=5)

###
# Start your code here
forward(40)
right(90)
forward(120)
left(90)
for _ in range(1):
    forward(40)
    right(90)
forward(40)
left(90)
forward(120)
right(90)
forward(40)
for _ in range(2):
    left(180)
    forward(40)
    right(90)
    forward(120)
    left(90)
    for _ in range(1):
        forward(40)
        right(90)
    forward(40)
    left(90)
    forward(120)
    right(90)
    forward(40)
forward(160)
left(180)
for _ in range(2):
    forward(40)
    right(90)
    forward(40)
    left(90)




# End your code here
###
 
window.exitonclick()