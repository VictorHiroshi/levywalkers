"""
Simulation arena abstraction.
"""

#
# CODE
#
class Arena(object):
    """
    I am a simulated experiment arena
    """
    
    def __init__(self, params):
        """
        I initialize myself.
        
        :param params: simulation parameters
        :type  params: dict
        
        :returns: nothing
        :rtype: None
        """
        # arena center
        self.center = params['arenaSize'] / 2
        
        # inner circle radius
        self.innerRadius = params['innerRadius']
        
        # outer circle radius
        self.outerRadius = params['outerRadius']
        
    def draw(self):
        """
        I draw myself.
        
        :returns: nothing
        :rtype: None
        """
        # clear background
        background(200)
        
        # draw outside circle
        stroke(0)
        fill(255)
        ellipse(self.center, self.center, self.outerRadius, self.outerRadius)

        # draw inside circle
        stroke(0)
        fill(150)
        ellipse(self.center, self.center, self.innerRadius, self.innerRadius)
