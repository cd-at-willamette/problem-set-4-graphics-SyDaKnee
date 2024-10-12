########################################
# Name: Sydney Bell
# Collaborators: I worked alone.
# Estimate time spent (hrs): 1 1/2 hr ish?
########################################

from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score

def clicky_box():

    # Defining the callback function, which you won't need until Part C
    def on_mouse_down(event):
        if square.get_x() <= event.get_x() <= square.get_x() + SQUARE_SIZE and square.get_y() <= event.get_y() <= square.get_y() + SQUARE_SIZE:
            
            nonlocal click_count # Modifies the "click_count" variable outside of the clicky_box function.
            click_count += 1 # If the click is inside the square, the score increases by one.

            random_x = random.randint(0, GW_WIDTH - SQUARE_SIZE) # Makes sure the x-position is within the window.
            random_y = random.randint(0, GW_HEIGHT - SQUARE_SIZE) # Makes sure the y-position is within the window.
        
            square.set_location(random_x, random_y) # Sets the square to a random position within the window when clicked.

            score_label.set_label(f"Score: {click_count}") # Updates the score count when the box is clicked.

        else: # If clicked outside the box,
            click_count = 0 # Set the click_count to zero, 
        score_label.set_label(f"Score: {click_count}") # Change the score label to reflect the new click_count.

    # Down here you should initialize the window and draw the initial square
    # Make sure you tab it in so that it is part of the clicky_box function

    gw = GWindow(GW_WIDTH, GW_HEIGHT) # Creates a graphics window.

    square = GRect(0, 0, SQUARE_SIZE, SQUARE_SIZE) # Creates the clicky box.
    square.set_filled(True)
    square.set_fill_color("Lavender") # Sets the color of the clicky box to "lavender".
    gw.add(square, (GW_WIDTH - SQUARE_SIZE) / 2, (GW_HEIGHT - SQUARE_SIZE) / 2) # Adds the clicky box to the center of the graphics window.

    click_count = 0 # Starts the click count at zero.
    score_label = GLabel(f"Score: {click_count}") # Makes the score reflect the click count value and sets it as a label to be displayed in the graphics window.
    score_label.set_font(SCORE_FONT) # Sets the score font.
    gw.add(score_label, SCORE_DX, GW_HEIGHT - SCORE_DY) # Adds the score label to the graphics window.

    gw.add_event_listener("click", on_mouse_down) # Adds a listener that looks for when the user's mouse clicks.


if __name__ == '__main__':
    clicky_box()
