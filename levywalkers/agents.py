"""
Simulation agents collection.
"""

#
# IMPORTS
#
from random import randint
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
            agentParams = self.randomizeAgentParams()
            agents.append(Agent(self.params, agentParams, agents))
        
        # return created agents
        return agents
    
    def randomizeAgentParams(self):
        minSpeedInterval = self.params["minSpeedInterval"]
        maxSpeedInterval = self.params["maxSpeedInterval"]
        drunkenFactor = self.params["drunkenFactor"]
        
        minSpeed = randint(minSpeedInterval[0], minSpeedInterval[1])
        maxSpeed = randint(maxSpeedInterval[0], maxSpeedInterval[1])
        drunkenFactor = randint(drunkenFactor[0], drunkenFactor[1])

        return {
            "minSpeed": minSpeed,
            "maxSpeed": maxSpeed,
            "drunkenFactor": drunkenFactor
        }
    
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
            agent.move(self.agents)
