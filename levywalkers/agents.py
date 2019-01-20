"""
Simulation agents collection.
"""

#
# IMPORTS
#
from agent import Agent

#
# CODE
#
class Agents(object):
    """
    I am a simulation agents collection.
    """
    
    def __init__(self, params):
        """
        I initialize myself.
        
        :param params: simulation parameter
        :type  params: dict
        
        :returns: nothing
        :rtype: None
        """
        # simulation parameters
        self.params = params
        
        # number of agents in simulation
        self.number = self.params['agentsNumber']
        
        # simulation agents
        self.agents = self.createAgents(self.number)
        
    def createAgents(self, number):
        """
        I create the simulation agents.
        
        :param number: number of created agents
        :type  number: int
        
        :returns: created agentes
        :rtype: list
        """
        # initial empty agents list
        agents = []
        
        # create agents and append to agents list
        for _ in range(self.number):
            agents.append(Agent(self.params, agents))
        
        # return created agents
        return agents
                
    def draw(self):
        """
        I draw all simulation agents.
        
        :returns: nothing
        :rtype: None
        """
        # draw agents
        for agent in self.agents:
            agent.draw()
            
    def move(self):
        """
        I make all simulation agents move one step.
        
        :returns: nothing
        :rtype: None
        """
        # move agents
        for agent in self.agents:
            agent.move()
