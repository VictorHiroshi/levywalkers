"""
Simulation main file.
"""

#
# IMPORTS
#
from arena import Arena

#
# CONSTANTS AND DEFINITIONS
#

# screen width and height
WIDTH = 500
HEIGHT = 500

# create simulation area
arena = Arena(WIDTH/2, HEIGHT/2, 400, WIDTH/2, HEIGHT/2, 100)

#
# CODE
#
def draw():
    """
    I am the Processing default drawing function.
    
    :returns: nothing
    :rtype: None    
    """
    # draw simulation arena
    arena.draw()


def setup():
    """
    I am the Processing default setup functon.
    
    :returns: nothing
    :rtype: None
    """
    # set screen size and background color
    size(WIDTH, HEIGHT)
    background(200)
