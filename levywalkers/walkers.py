"""
I manage a simulation walkers set.
"""

#
# IMPORTS
#
from walker import Walker

#
# CODE
#
class Walkers(object):
    """
    I am a walkers manager.
    """
    
    def __init__(self, number, aSideMin, aSideMax, bSideMin, bSideMax):
        """
        I initialize myself.
        
        :param number: number of walkers in simulation.
        :type  number: int
        
        :param aSideMin: lower A side boundary to spawn walkers.
        :type  aSideMin: int
        
        :param aSideMax: upper A side boundary to spawn walkers.
        :type  aSideMax: int
        
        :param bSideMin: lower B side boundary to spawn walkers.
        :type  bSideMin: int
        
        :param bSideMax: upper A side boundary to spawn walkers.
        :type  bSideMax: int
        
        :returns: nothing
        :rtype: None
        """
        # number of walkers
        self.number = number
        
        # spawn boundaries
        self.aSideMin = aSideMin
        self.aSideMax = aSideMax
        self.bSideMin = bSideMin
        self.bSideMax = bSideMax
        
        # initialize walkers
        self.agents = self.createAgents()
        
        
    def createAgents(self):
        """
        I create this simulation walkers.
        
        :returns: crated walkers
        :rtype: list
        """
        # create empty agents list
        agents = []
        
        # create and append walkers
        for _ in range(self.number):
            agents.append(Walker(self.aSideMin, self.aSideMax, self.bSideMin, self.bSideMax))
        
        # return list to manager
        return agents

    
    def draw(self):
        """
        I invoke the drawing function for each managed walker.
        
        :returns: nothing
        :rtype: None
        """
        # draw each walker
        for agent in self.agents:
            agent.draw()

            
    def move(self):
        """
        I invoke the update position method for each managed walker.
        
        :returns: nothing
        :rtype: None
        """
        # update each walker position
        for agent in self.agents:
            agent.move(self.agents)
