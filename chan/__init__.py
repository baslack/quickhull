# Benjamin Slack
# CS 5310
# Chan's Minimalist Convex Hull in R^3

class Point():
    """
    Generalized point class
    """

    def __init__(self, x=0.0, y=0.0, z=0.0, n=None, p=None):
        """
        Creates a point. Optional attributes
        given as the parameters below.
        :type x: float
        :param x: default 0.0
        :type y: float
        :param y: default 0.0
        :type z: float
        :param z: default 0.0
        :type n: Point
        :param n: default None
        :type p: Point
        :param p: default None
        """
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
        self.nxt = n
        self.prv = p

    def __str__(self):
        return "({0},{1},{2}),  next:{3}, prev:{4}\n".format(
            self.x,
            self.y,
            self.z,
            repr(self.nxt),
            repr(self.prv))

    def compare_x(self, other):
        return int(self.x - other.x)


    def act(self):
        if self.prv.nxt != self:
            # insertion
            self.prv.nxt = self
            self.nxt.prv = self
        else:
            # deletion
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
    :type p: Point
    :type q: Point
    :type r: Point
    :return: float
    """

    if (p == __nil) or (q == __nil) or (r == __nil):
        return 1.0
    else:
        return (q.x - p.x) * (r.y - p.y) - (r.x - p.x) * (q.y - p.y)


def time(p, q, r):
    if (p == __nil) or (q == __nil) or (r == __nil):
        return CONST_INF
    else:
        return ((q.x - p.x) * (r.z - p.z) - (r.x - p.x) * (q.z - p.z)) / turn(p, q, r)

def x_sort(P):
    """
    :type P: list[Point]
    :param P: list of Points
    :return: void
    """

    P.sort(cmp=Point.compare_x)
    for this_p in P:
        if P.index(this_p) == 0:
            this_p.prv = None
            this_p.nxt = P[1]
        elif P.index(this_p) == len(P) - 1:
            this_p.nxt = None
            this_p.prv = P[len(P)-2]
        else:
            this_p.prv = P[P.index(this_p) - 1]
            this_p.nxt = P[P.index(this_p) + 1]


if __name__ == "__main__":
    print(CONST_INF)
    a = Point(1, 2, 3)
    b = Point(-1, -2, -3)
    c = Point(2, -3, 1)
    print(turn(a, b, c))
    print(dir(a))
    print(a.__doc__)
    test = list()
    test.append(a)
    test.append(b)
    test.append(c)
    x_sort(test)
    for this in test:
        print(this)
