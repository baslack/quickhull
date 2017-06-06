#Benjamin Slack
#CS 5310
#Chan's Minimalist Convex Hull in R^3

class Point():
    """
    Generalized point class
    """
    def __init__(self, x=0.0, y=0.0, z=0.0, n=None, p=None):
        """
        Creates a point. Optional attributes
        given as the parameters below.
        :param x: float default 0.0
        :param y: float default 0.0
        :param z: float default 0.0
        :param n: Point nxt default None
        :param p: Point prv default None
        """
        self.x = x
        self.y = y
        self.z = z
        self.nxt = n
        self.prv = p

    def act(self):
        if self.prv.nxt != self:
            #insertion
            self.prv.nxt = self
            self.nxt.prv = self
        else:
            #deletion
            self.prv.nxt = self.nxt
            self.nxt.prv = self.prv


CONST_INF = float("1e99")


__nil = Point()


def turn(p, q, r):
    """
    Determins the rotational orientation of a
    facet defined by three given points, p,q,r.
    Returns a float, if return < 0, orientation
    is clockwise, else, counterclockwise
    :param p: Point
    :param q: Point
    :param r: Point
    :return: float
    """
    if (p == __nil) or (q == __nil) or (r == __nil):
        return 1.0
    else:
        return (q.x-p.x)*(r.y-p.y) - (r.x-p.x)*(q.y-p.y)


def time(p, q, r):
    if (p == __nil) or (q == __nil) or (r == __nil):
        return CONST_INF
    else:
        



if __name__ == "__main__":
    print(CONST_INF)
    a = Point(1,2,3)
    b = Point(-1,-2,-3)
    c = Point(2,-3,1)
    print(turn(a,b,c))
    print(dir(a))
    print(a.__doc__)