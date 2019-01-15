"""
Simulation instance abstraction.
"""

#
# IMPORTS
#
from arena import Arena
from walkers import Walkers


#
# CONSTANTS AND DEFINITIONS
#
WIDTH = 500
HEIGHT = 500


#
# CODE
#
class Simulation(object):
    """
    I abstract a simulation instance.
    """
    
    def __init__(self):
        """
        I initialize myself.
        
        :returns: nothing
        :rtype: None
        """
        # simulation arena
        self.arena = Arena(WIDTH / 2, HEIGHT / 2, 400, WIDTH / 2, HEIGHT / 2, 100)
        
        # simulation agents
        self.agents = Walkers(32, 100, 200, 300, 400)
        
        # simulation current step
        self.timestep = 0
        
    
    def step(self):
        """
        I pass one step in an ongoing simulation.
        
        :returns: nothing
        :rtype: None
        """
        # increase time counter
        self.timestep += 1
        
        # update walkers positions
        self.agents.move()
        
    
    def draw(self):
        """
        I draw an ongoing simulation current state.
        """
        # draw simulation arena
        self.arena.draw()
        
        # draw agents
        self.agents.draw()
        
        # draw current time step info
        textSize(14)
        fill(0)
        text('Step #{}'.format(self.timestep), 10, 20);
