############################################################
# Name: Sydney Bell
# Name(s) of anyone worked with: I worked alone. 
# Est time spent (hr): 15 mins. 
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 600
HEIGHT = 600

def draw_image():
    """ Creates a window and draws a student's creation"""

    # Creating the window
    gw = GWindow(WIDTH, HEIGHT)

    rectangle = GRect(WIDTH, WIDTH)
    rectangle.set_color("skyblue")
    rectangle.set_filled(True)
    gw.add(rectangle)

    oval = GOval(WIDTH//2, 150)
    oval.set_color("palegoldenrod")
    oval.set_filled(True)
    gw.add(oval)

    gw.add(GLine(0, WIDTH//4, WIDTH//4, WIDTH))

    gw.add(GLabel("Sun rising over mountainside.", WIDTH//2, WIDTH//2))

    # And now it is your turn! Add your code below! Make sure you meet all the requirements!





if __name__ == '__main__':
    draw_image()
