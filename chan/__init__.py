# Benjamin Slack
# CS 5310
# Chan's Minimalist Convex Hull in R^3

import array

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

def hull(p_list, n, A, B):
    """
    :type p_list: list[Point]
    :param p_list: list of points
    :type n: int
    :param n: number of points
    :type A: list[Point]
    :param A: list of points in L hull
    :type B: list[Point]
    :param B: list of points in R hull
    :return: void
    """
    u = Point()
    v = Point()
    mid = Point()
    t = array.array("d", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    old_t = 0.0
    new_t = 0.0
    i, j, k, l, min_l = [0, 0, 0, 0, 0]

    #base case
    if n == 1:
        A[0] = __nil
        p_list[0].prv = __nil
        p_list[0].nxt = __nil
        return

    #step through p_list to find
    #a middle point to partition from
    i = 0
    u = p_list[0]
    while (i < n/2 - 1):
        u = u.nxt
        i += 1
    #u should now point to the middle of the
    #set of points
    mid = u.nxt
    v = u.nxt

    #recurse with each half of the partition
    hull(p_list[:p_list.index(mid)], n//2, B[:n//2*2], A[:n//2*2])
    hull(p_list[p_list.index(mid):], n//2, B[n//2*2:], A[n//2*2:])

    #find initial bridge
    while True:
        if turn(u, v, v.nxt) < 0:
            v = v.nxt
        elif turn(u.prv, u, v) < 0:
            u = u.prv
        else:
            break

    #merge by tracking bridge uv over time
    i = 0
    k = 0
    j = n//2*2
    old_t = -CONST_INF
    while True:
        t[0] = time(B[i].prv, B[i], B[i].nxt)
        t[1] = time(B[j].prv, B[j], B[j].nxt)
        t[2] = time(u, u.nxt, v)
        t[3] = time(u.prv, u, v)
        t[4] = time(u, v.prv, v)
        t[5] = time(u, v, v.nxt)
        new_t = CONST_INF
        l = 0
        while l < 6:
            if (t[l] > old_t) and (t[l] < new_t):
                min_l = l
                new_t = t[l]
            l += 1

        #loop scape clause
        if new_t == CONST_INF:
            break

        #case 0
        if min_l == 0:
            if B[i].x < u.x:
                A[k] = B[i]
                k += 1
            B[i].act()
            i += 1
            break
        #case 1
        elif min_l == 1:
            if B[j].x > v.x:
                A[k] = B[j]
                k +=1
            B[j].act()
            j += 1
            break
        #case 2
        elif min_l == 2:
            A[k] = u.nxt
            u = u.nxt
            k += 1
            break
        #case 3
        elif min_l == 3:
            A[k] = u
            k += 1
            u = u.prv
            break
        #case 4
        elif min_l == 4:
            A[k] = v.prv
            k += 1
            v = v.prv
            break
        #case 5
        elif min_l == 5:
            A[k] = v
            k += 1
            v = v.nxt
            break
        else:
            break
    A[k] = __nil
    #cont update pointers









    pass

def chan(raw_pts, filename="chan.obj"):
    """
    :type raw_pts: list[tuple[float]]
    :param raw_pts: a list of raw tuples of 3 floats
    :type filename: str
    :param filename: a filename (path) to the obj
    :return: void
    """
    #setup a list of Points
    P = list()
    for pt in raw_pts:
        P.append(Point(pt[0], pt[1], pt[2]))
    #sort the points on X coord
    x_sort(P)

    A = list()
    B = list()
    for i in range(2*len(P)):
        A[i] = None
        B[i] = None

    hull(P, len(P), A, B)




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
