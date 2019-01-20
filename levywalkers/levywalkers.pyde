#
# IMPORTS
#
from arena import Arena
from agents import Agents

#
# CONSTANTS AND DEFINITIONS
#

# simulation parameters
params = {
    "simulationStep": 0,
    "arenaSize": 500,
    "outerRadius": 400,
    "innerRadius": 100,
    
    "agentsNumber": 12,
    "agentRadius": 14,
    "moveTargetChance": 0.0005,
    
    "minSpeedInterval": [95, 98],
    "maxSpeedInterval": [99, 102],
    "drunkenFactor": [4, 14],
    "swing": 22
}

# simulation arena
arena = Arena(params)

# simulation agents
agents = Agents(params)

#
# CODE
#
def draw():
    # increase simulation step
    params['simulationStep'] += 1
    
    # draw arena
    arena.draw()
    
    # draw step info
    textSize(14)
    fill(0)
    text('Step #{}'.format(params['simulationStep']), 10, 20);
    # move agents
    agents.move()
    
    # draw agents
    agents.draw()
    
def setup():
    # set screen size and background color
    size(params['arenaSize'], params['arenaSize'])
    background(200)
