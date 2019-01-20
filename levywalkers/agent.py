"""
Simulation agents abstraction.
"""

#
# IMPORTS
#
import random
import uuid

#
# CODE
#
class Agent(object):
    """
    I am a simulation agent abstraction.
    """
    
    def __init__(self, params, others):
        """
        I initialize myself.
        
        :param params: simulation parameters
        :type  params: dict
        
        :param others: other agents already on simulation
        :type  others: list
        
        :returns: nothing
        :rtype: None
        """
        # simulation parameters
        self.params = params
        
        # agent uuid
        self.uuid = str(uuid.uuid1())
        
        # agent representation circle color
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 200)
        
        # agent representation circle radius
        self.radius = self.params['agentRadius']
        
        # agent coordinates
        self.coord = self.generateInitialCoordinates(others)
        
        # agent target coordinate
        self.target = self.generateTarget()
        
        # agent speed
        self.velocity = PVector(0, 0)
        
        # agent acceleration
        self.acc = PVector(0, 0)
        
        
    def detectCollision(self, coord, others):
        """
        I detect if a generated initial coordinate will incur in a collision.
        
        :param coord: future coordinate
        :type  coord: PVector
        
        :param others: other agents in simulation
        :type  others: list
        
        :returns: collision checking result
        :rtype: bool
        """
        # for every other agent
        for other in others:
            
            # agents are colliding: return true
            if coord.dist(other.coord) < self.params['agentRadius']:
                return True
        
        # return false
        return False  
        
    def draw(self):
        """
        I draw myself.
        
        :returns: nothing
        :rtype: None
        """
        # draw agent representation
        stroke(0)
        fill(self.color[0], self.color[1], self.color[2], self.color[3])
        ellipse(self.coord.x, self.coord.y, self.radius, self.radius)
        
        # draw agent velocity vector direction representation
        velocityX = self.coord.x + 2 if self.target.x > self.coord.x else self.coord.x - 2
        velocityY = self.coord.y + 2 if self.target.y > self.coord.y else self.coord.y - 2
        ellipse(velocityX, velocityY, 8, 8)
        
    def generateInitialCoordinates(self, others):
        """
        I generate valid initial agent coordinates.
        
        :param others: other agents in simulation
        :type  others: list
        
        :returns: valid initial coordinates
        :rtype: PVector
        """
        # distance to arena center (initially invalid)
        distance = 0
        
        # agent coordinates (initially invalid)
        coord = PVector(0, 0)
        
        # arena center
        center = PVector(self.params['arenaSize'] / 2, self.params['arenaSize'] / 2)
        
        # arena valid boundaries
        outerBoundary = (self.params['outerRadius'] / 2) - (self.radius / 2)
        innerBoundary = (self.params['innerRadius'] / 2) + (self.radius / 2)        
                
        # agent position is out of bounds: guess another initial position
        while distance > outerBoundary or distance < innerBoundary or self.detectCollision(coord, others):
            
            # guess an initial coordinate
            coord = PVector(random.randint(0, self.params['arenaSize']), random.randint(0, self.params['arenaSize']))
            
            # compute distance to arena center
            distance = coord.dist(center)
        
        # return valid coordinates
        return coord
    
    def generateTarget(self):
        """
        I generate valid target locations.
        
        :returns: valid target
        :rtype: PVector
        """
         # distance to arena center (initially invalid)
        distance = 0
        
        # agent target (initially invalid)
        target = PVector(0, 0)
        
        # arena center
        center = PVector(self.params['arenaSize'] / 2, self.params['arenaSize'] / 2)
        
        # arena valid boundaries
        outerBoundary = (self.params['outerRadius'] / 2) - (self.radius / 2)
        innerBoundary = (self.params['innerRadius'] / 2) + (self.radius / 2)        
                
        # agent target is out of bounds: guess another target position
        while distance > outerBoundary or distance < innerBoundary:
            
            # guess another target coordinate
            target = PVector(random.randint(0, self.params['arenaSize']), random.randint(0, self.params['arenaSize']))
            
            # compute distance to arena center
            distance = target.dist(center)
        
        # return valid coordinates
        return target
        
    
    def move(self):
        """
        I make this agent give his next step.
        
        :returns: nothing
        :rtype: none
        """
        # update agent target if so
        self.moveTarget()
        
        # find unit vector pointing to target
        direction = PVector.sub(self.target, self.coord)
        direction.normalize()
        
        # compute accelaration
        self.acc = direction.mult(0.01)
        
        # update velocity
        self.velocity.add(self.acc)
        self.velocity.limit(0.8)  
        
        # update coordinates
        newCoord = PVector.add(self.coord, self.velocity)
        
        # compute arena physical limitation parameters
        center = PVector(self.params['arenaSize'] / 2, self.params['arenaSize'] / 2)
        outerBoundary = (self.params['outerRadius'] / 2) - (self.radius / 2)
        innerBoundary = (self.params['innerRadius'] / 2) + (self.radius / 2)
        
        # next coordinate is valid: update it
        if newCoord.dist(center) < outerBoundary and newCoord.dist(center) > innerBoundary:
            self.coord = newCoord
        
    def moveTarget(self):
        """
        I update this agent target coordinate.
        
        :return: nothing
        :rtype: none
        """
        # draw random chance of changing target coordinates
        moveChance = random.uniform(0, 1)
        
        # should change target: update it
        if moveChance < self.params['moveTargetChance']:
            
            # update target
            self.target = self.generateTarget()
        
