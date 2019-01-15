"""
Simulation walkers.
"""

#
# IMPORTS
#
import math
import random

#
# CONSTANTS AND DEFINITIONS
#
WALKER_SIZE = 16
OPACITY = 200
ARENA_CENTER = 250
INNER_RADIUS = 58
OUTER_RADIUS = 192


#
# CODE
#
class Walker(object):
    """
    I am a simulation walker.
    """
    
    def __init__(self, aSideMin, aSideMax, bSideMin, bSideMax):
        """
        I initialize myself.
        
        :param aSideMin: arena A size lower coordinate limitation
        :type  aSideMin: int
        
        :param aSideMax: arena A size upper coordinate limitation
        :type  aSideMax: int
        
        :param bSideMin: arena B size lower coordinate limitation
        :type  bSideMin: int
        
        :param bSideMax: arena B size upper coordinate limitation
        :type  bSideMax: int
        """    
        # walker color
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), OPACITY)
        
        # arena coordinate limitations
        self.aSideMin = aSideMin
        self.aSideMax = aSideMax
        self.bSideMin = bSideMin
        self.bSideMax = bSideMax
        
        # walker coordinates
        self.x = self.generateValidCoordinate()
        self.y = self.generateValidCoordinate()
        
        # perlin noise parameters
        self.perlinTx = random.randint(0, 100000)
        self.perlinTy = random.randint(100000, 10000000000)


    def draw(self):
        """
        I draw a representation of this walker position.
        
        :returns: nothing
        :rtype: None
        """
        # draw walker representation
        stroke(0)
        fill(self.color[0], self.color[1], self.color[2], self.color[3])
        ellipse(self.x, self.y, WALKER_SIZE, WALKER_SIZE)
        
    
    def generateValidCoordinate(self):
        """
        I generate valid initial coordinates for this walker.
        
        :returns: coordinate value
        :rtype: int
        """
        # select if walker will spawn in left/right or up/down
        side = random.choice([True, False])
        
        # walker will spawn in left/up: generate his coordinates
        if side:
            return random.randint(self.aSideMin + WALKER_SIZE, self.aSideMax - WALKER_SIZE)
        
        # walker will spawn in right/down: generate his coordinates
        else:
            return random.randint(self.bSideMin + WALKER_SIZE, self.bSideMax - WALKER_SIZE) 
        
        
    def move(self):
        """
        I update this walker coordinates.
        
        :returns: nothing
        :rtype: None
        """
        # get step size from perlin noise values generator
        xStep = noise(self.perlinTx)
        yStep = noise(self.perlinTy)
        
        # increase perlin noise time interval
        self.perlinTx += 0.1
        self.perlinTy += 0.1
        
        # compute agent future position
        x = self.x + map(xStep, 0, 1, -1, 1)
        y = self.y + map(yStep, 0, 1, -1, 1)
        
        # find distance to arena center
        distToCenter = math.sqrt(math.pow(x - ARENA_CENTER, 2) + math.pow(y - ARENA_CENTER, 2))
        
        # walker is in a valid position: update his coordinates
        if distToCenter > INNER_RADIUS and distToCenter < OUTER_RADIUS:
            self.x = x
            self.y = y
