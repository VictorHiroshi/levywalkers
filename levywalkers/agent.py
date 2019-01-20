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
    
    def __init__(self, simulationParams, agentParams, others):
        """
        I initialize myself.
        
        :param simulationParams: simulation parameters
        :type  simulationParams: dict
        
        :param agentParams: min and max speed, drunken parameters
        :type  simulationParams: dict
        
        :param others: other agents already on simulation
        :type  others: list
        
        :returns: nothing
        :rtype: None
        """
        # simulation parameters
        self.simulationParams = simulationParams

        # agent movement parameters
        self.agentParams = agentParams
        
        # agent uuid
        self.uuid = str(uuid.uuid1())
        
        # ticks blocked by other agent
        self.blockedTime = 0

        # agent representation circle color
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 200)
        
        # agent representation circle radius
        self.radius = self.simulationParams['agentRadius']
        
        # arena valid boundaries
        self.outerBoundary = (self.simulationParams['outerRadius'] / 2) - (self.radius / 2)
        self.innerBoundary = (self.simulationParams['innerRadius'] / 2) + (self.radius / 2) 

        # initial direction
        self.direction = PVector(0, 0)
        
        # agent coordinates
        self.coord = self.generateInitialCoordinates(others)
        
        # agent target coordinate
        self.target = self.generateTarget()
        
        # agent speed
        self.velocity = PVector(0, 0)

        # agent moving "time"
        self.step = 0

    def detectWallCollision(self, coord):
        """
        I detect if a coordinate will incur in a collision a wall.
        
        :param coord: future coordinate
        :type  coord: PVector
        
        :param others: other agents in simulation
        :type  others: list
        
        :returns: inner/outer wall, None
        :rtype: wall name
        """
        # arena center
        center = PVector(self.simulationParams['arenaSize'] / 2, self.simulationParams['arenaSize'] / 2)
        
        # compute distance to arena center
        distance = coord.dist(center) 
        
        if distance > self.outerBoundary:
            return "outer"
        if distance < self.innerBoundary:
            return "inner"
        return None
        
    def detectAgentCollision(self, coord, others):
        """
        I detect if a coordinate will incur in a collision with another agent.
        
        :param coord: future coordinate
        :type  coord: PVector
        
        :param others: other agents in simulation
        :type  others: list
        
        :returns: collided agent
        :rtype: agent
        """
        # for every other agent
        for other in others:
            if self.uuid == other.uuid:
                continue
            # agents are colliding: return true
            if coord.dist(other.coord) < self.simulationParams['agentRadius']:
                return other
        
        # return false
        return None  
        
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
        
                
        # agent position is out of bounds: guess another initial position
        while self.detectAgentCollision(coord, others) or self.detectWallCollision(coord):
            # guess an initial coordinate
            coord = PVector(random.randint(0, self.simulationParams['arenaSize']), random.randint(0, self.simulationParams['arenaSize']))
            
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
        center = PVector(self.simulationParams['arenaSize'] / 2, self.simulationParams['arenaSize'] / 2)
        
        # arena valid boundaries
        outerBoundary = (self.simulationParams['outerRadius'] / 2) - (self.radius / 2)
        innerBoundary = (self.simulationParams['innerRadius'] / 2) + (self.radius / 2)        
                
        # agent target is out of bounds: guess another target position
        while distance > outerBoundary or distance < innerBoundary:
            
            # guess another target coordinate
            target = PVector(random.uniform(0, self.simulationParams['arenaSize']), random.uniform(0, self.simulationParams['arenaSize']))
            
            # compute distance to arena center
            distance = target.dist(center)
        
        v1 = PVector.sub(target, self.coord)
        if degrees(PVector.angleBetween(self.direction, v1)) > 45:
            self.stop()
        # return valid coordinates
        return target
    
    
    def getNextCoordinate(self):
        """
        I calculate this agent next coordinate.
        
        :returns: coordinate
        :rtype: PVector
        """
        swing = self.simulationParams["swing"]
        current_step = self.step % swing
    
        if current_step == 0 or not self.direction:
            self.direction = PVector.sub(self.target, self.coord)
            self.direction.normalize()
            factor = self.agentParams["drunkenFactor"]
            oscilation = random.uniform(-1 * factor, factor)
            self.direction.rotate(radians(oscilation))

        speed = map(
                        tan(map(current_step, -4, swing, PI / 8, PI / 4)),
                        0.41, 1,
                        self.agentParams["minSpeed"], self.agentParams["maxSpeed"] 
                    )

        self.velocity = self.direction.mult(speed / 100)
        
        newCoord = PVector.add(self.coord, self.velocity)

        self.step += 1
        
        return newCoord
        
    
    def stop(self):
        """
        I stop this agent movement abruptly.
        
        :returns: nothing
        :rtype: none
        """
        self.velocity = PVector(0, 0)
        self.step = 0

    
    def move(self, others):
        """
        I make this agent give his next step.
        
        :returns: nothing
        :rtype: none
        """
        # update agent target if so
        self.moveTarget()
        
        nextCoord = self.getNextCoordinate()

        collidingWall = self.detectWallCollision(nextCoord)
        collidingAgent = self.detectAgentCollision(nextCoord, others)
        
        if collidingWall == "inner" or collidingWall == "outer":
            self.stop()
            self.target = self.generateTarget()
        elif collidingAgent is not None:
            self.stop()
            self.blockedTime += 1
            if self.blockedTime > self.simulationParams["swing"] / 2:
                self.target = self.generateTarget()
        else:
            self.blockedTime = 0
            self.coord = nextCoord
        
        
    def moveTarget(self):
        """
        I update this agent target coordinate.

        :return: nothing
        :rtype: none
        """ 
        # draw random chance of changing target coordinates
        moveChance = random.uniform(0, 1)
        
        # should change target: update it
        if moveChance < self.simulationParams['moveTargetChance']:
            # update target
            self.target = self.generateTarget()
        
