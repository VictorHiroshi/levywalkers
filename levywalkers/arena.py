"""
Simulation arena abstraction.
"""

#
# CODE
#
class Arena(object):
    """
    I am an arena abstraction.
    """

    def __init__(self, outX, outY, outRadius, inX, inY, inRadius):
        """
        I initialize myself.

        :param outX: outer arena center X coordinate
        :type  outX: int

        :param outY: outer arena center Y coordinate
        :type  outY: int

        :param outRadius: outer arena radius
        :type  outRadius: int

        :param inX: inner arena center X coordinate
        :type  inY: int

        :param inY: inner arena center Y coordinate
        :type  inY: int

        :param inRadius: inner arena circle radius
        :type  inRadius: int
        """
        # outer arena circle parameters
        self.outX = outX
        self.outY = outY
        self.outRadius = outRadius

        # inner arena circle parameters
        self.inX = inX
        self.inY = inY
        self.inRadius = inRadius


    def draw(self):
        """
        I draw the simulation arena.

        :returns: nothing
        :rtype: None
        """
        # clear background
        background(200)
        
        # draw outside circle
        stroke(0)
        fill(255)
        ellipse(self.outX, self.outY, self.outRadius, self.outRadius)

        # draw inside circle
        stroke(0)
        fill(150)
        ellipse(self.inX, self.inX, self.inRadius, self.inRadius)
