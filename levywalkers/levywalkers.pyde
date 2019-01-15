"""
Simulation main file.
"""

#
# IMPORTS
#
from simulation import Simulation

import simulation


#
# CONSTANTS AND DEFINITIONS
#
walkersSimulation = Simulation()


#
# CODE
#
def draw():
    """
    I am the Processing default drawing function.

    :returns: nothing
    :rtype: None    
    """
    # pass one time step
    walkersSimulation.step()
    
    # draw current simulation state
    walkersSimulation.draw()
    

def setup():
    """
    I am the Processing default setup functon.

    :returns: nothing
    :rtype: None
    """
    # set screen size and background color
    size(simulation.WIDTH, simulation.HEIGHT)
    background(200)
