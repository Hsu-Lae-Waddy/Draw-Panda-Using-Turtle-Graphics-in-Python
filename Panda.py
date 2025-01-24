#1.Import Turtle
# Draw a Panda using Turtle Graphics
# Import turtle package

import turtle

#2Make Turtle Object
# Creating a turtle object(pen)
pen = turtle.Turtle()

#3Define a method to draw a circle with dynamic radius and color.
# Defining method to draw a colored circle
# with a dynamic radius
def ring(col, rad):
    # Set the fill
    pen.fillcolor(col)

    # Start filling the color
    pen.begin_fill()

    # Draw a circle
    pen.circle(rad)

    # Ending the filling of the color
    pen.end_fill()

##########################Main Section#############################

# pen.up             --> move turtle to air
# pen.down           --> move turtle to ground
# pen.setpos         --> move turtle to given position
# ring(color, radius) --> draw a ring of specified color and radius
###################################################################

#4Draw ears of Panda with black color circles.
##### Draw ears #####
# Draw first ear
pen.up()
pen.setpos(-35, 95)
pen.down
ring('black', 15)

# Draw second ear
pen.up()
pen.setpos(35, 95)
pen.down()
ring('black', 15)

#5Draw face of Panda with white color circle.
##### Draw face #####
pen.up()
pen.setpos(0, 35)
pen.down()
ring('white', 40)
##### Draw eyes black #####

#6Draw eyes of Panda with black and white color concentric circles.
##### Draw eyes black #####

# Draw first eye
pen.up()
pen.setpos(-18, 75)
pen.down
ring('black', 8)

# Draw second eye
pen.up()
pen.setpos(18, 75)
pen.down()
ring('black', 8)

##### Draw eyes white #####

# Draw first eye
pen.up()
pen.setpos(-18, 77)
pen.down()
ring('white', 4)

# Draw second eye
pen.up()
pen.setpos(18, 77)
pen.down()
ring('white', 4)

#7Draw nose of Panda with black color circle.
##### Draw nose #####
pen.up()
pen.setpos(0, 55)
pen.down
ring('black', 5)

#8Draw two semicircle for mouth below nose.
##### Draw mouth #####
pen.up()
pen.setpos(0, 55)
pen.down()
pen.right(90)
pen.circle(5, 180)
pen.up()
pen.setpos(0, 55)
pen.down()
pen.left(360)
pen.circle(5, -180)
pen.hideturtle()