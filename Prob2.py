########################################
# Name: Sydney Bell
# Collaborators: I worked alone.
# Estimated time spent (hrs): 1 1/4 hr ish.
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15

def draw_pyramid(): # Draws the pyramid.
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """
    gw = GWindow(WIDTH, HEIGHT) # Creates a window to display the pyramid.
    for row in range(BRICKS_IN_BASE): # Iterates through each brick in the base row. 
        n_bricks = BRICKS_IN_BASE - row # Calculates the number of bricks in each row, the number of bricks decrease as you go up the pyramid. The base row = 0, next row = 1, so n_bricks = 14.
        row_y_position = HEIGHT - (row + 1) * BRICK_HEIGHT # Tracks the y-value position of the current row. Places the first row at the bottom of the window then moves each row upwards by BRICK_HEIGHT.
        start_x_position = (WIDTH - n_bricks * BRICK_WIDTH) / 2 # Tracks the x-value position of the first brick in the row so the pyramid can be centered. -> n_bricks * BRICK_WIDTH gies the total width of the row. -> (WIDTH - "total width of the row") / 2 centers the row.
        for i in range(n_bricks): # Iterates through the number of bricks in the current row.
            brick = GRect(start_x_position + i * BRICK_WIDTH, row_y_position, BRICK_WIDTH, BRICK_HEIGHT) # Creates a brick (rectangle) that starts at x-value position and moves to the right by i * BRICK_WIDTH. The y-value position is the same for all bricks in the row and the size of the brick is BRICK_WIDTH and BRICK_HEIGHT.
            gw.add(brick) # Adds the brick to the window. 

    # You got it from here


if __name__ == '__main__':
    draw_pyramid()
