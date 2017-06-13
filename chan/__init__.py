# Benjamin Slack
# CS 5310
# Chan's Minimalist Convex Hull in R^3

import array
import random
import geo

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
        return "({0},{1},{2})".format(
            self.x,
            self.y,
            self.z)


    def act(self):
        if self.prv.nxt != self:
            # insertion
            self.prv.nxt = self
            self.nxt.prv = self
        else:
            # deletion
            self.prv.nxt = self.nxt
            self.nxt.prv = self.prv

    def y_prime(self, t):
        return self.z - t*self.y

    def proj_2d(self, t):
        return tuple(self.x, self.y_prime(t))



CONST_INF = float("1e99")

__nil = Point(CONST_INF, CONST_INF, CONST_INF)


def turn(p, q, r):
    """
    Determins the rotational orientation of a
    tripet of given points, p,q,r.
    Returns a float, if return < 0, orientation
    is clockwise, return 0 = colinear, r >
    0 implies counter clockwise
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
    """
    calculates the time at which a given
    triplet of points changes its orientation
    from clockwise to counterclockwise or vice
    versa
    :type p: Point
    :param p: first pt
    :type q: Point
    :param q: second pt
    :type p: Point
    :param r: third pt
    :rtype : float
    :return: time
    """
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

    P.sort(key=lambda i: i.x)
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

def hull(p_list, list_q, list_r, n, A, B, s_ab, t_ab):
    """
    :type p_list: list[Point]
    :param p_list: list of points
    :param list_q, list_r: int indexes of p_list to work
    :type n: int
    :param n: number of points
    :type A: list[Point]
    :param A: list of points in L hull
    :type B: list[Point]
    :param B: list of points in R hull
    :param s,t : int indexes of A & B to work
    :return: void
    """
    #u = Point()
    #v = Point()
    #mid = Point()
    t = array.array("d", [0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
    #old_t = 0.0
    #new_t = 0.0
    i, j, k, l, min_l = [0, 0, 0, 0, 0]

    #base case
    if n == 1:
        A[s_ab] = __nil
        p_list[list_q].prv = __nil
        p_list[list_q].nxt = __nil
        return

    #step through p_list to find
    #a middle point to partition from
    i = 0
    u = p_list[list_q]
    while (i < n//2 - 1):
        u = u.nxt
        i += 1
    #u should now point to the middle of the
    #set of points
    mid = u.nxt
    v = u.nxt

    #recurse with each half of the partition
    hull(p_list, list_q, p_list.index(mid), n // 2, B, A, s_ab, s_ab + n // 2 * 2)
    hull(p_list, p_list.index(mid), list_r, n - n // 2, B, A, s_ab + n // 2 * 2, t_ab)

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
        t[0] = time(B[s_ab + i].prv, B[s_ab + i], B[s_ab + i].nxt)
        t[1] = time(B[s_ab + j].prv, B[s_ab + j], B[s_ab + j].nxt)
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
            if B[s_ab + i].x < u.x:
                A[s_ab + k] = B[s_ab + i]
                k += 1
            B[s_ab + i].act()
            i += 1
        #case 1
        elif min_l == 1:
            if B[s_ab + j].x > v.x:
                A[s_ab + k] = B[s_ab + j]
                k +=1
            B[s_ab + j].act()
            j += 1
        #case 2
        elif min_l == 2:
            A[s_ab + k] = u.nxt
            u = u.nxt
            k += 1
        #case 3
        elif min_l == 3:
            A[s_ab + k] = u
            k += 1
            u = u.prv
        #case 4
        elif min_l == 4:
            A[s_ab + k] = v.prv
            k += 1
            v = v.prv
        #case 5
        elif min_l == 5:
            A[s_ab + k] = v
            k += 1
            v = v.nxt
        else:
            pass
        #end cases
        #increment old_t
        old_t = new_t

    #after loop
    A[s_ab + k] = __nil

    #update pointers
    u.nxt = v
    v.prv = u

    k -= 1
    while k >= 0:
        if (A[s_ab + k].x <= u.x) or (A[s_ab + k].x >= v.x):
            A[s_ab + k].act()
            if A[s_ab + k] == u:
                u = u.prv
            elif A[s_ab + k] == v:
                v = v.nxt
        else:
            u.nxt = A[s_ab + k]
            A[s_ab + k].prv = u
            v.prv = A[s_ab + k]
            A[s_ab + k].nxt = v
            if A[s_ab + k].x < mid.x:
                u = A[s_ab + k]
            else:
                v = A[s_ab + k]
        k -= 1


def chan(raw_pts, filename="chan.obj"):
    """
    :type raw_pts: list[tuple[float]]
    :param raw_pts: a list of raw tuples of 3 floats
    :type filename: str
    :param filename: a filename (path) to the obj
    :return: void
    """
    #setup a list of Points
    p_list = list()
    for pt in raw_pts:
        p_list.append(Point(pt[0], pt[1], pt[2]))
    #sort the points on X coord
    x_sort(p_list)

    i = 0
    for this_pt in p_list:
        print("v[{0}] {1}".format(i + 1, str(this_pt)))
        i += 1

    A = list()
    B = list()
    for i in range(2*len(p_list)):
        A.append(None)
        B.append(None)

    hull(p_list, 0, len(p_list), len(p_list), A, B, 0, len(A))


    # i = 0
    # while A[i] != __nil:
    #     print("f[{0}] {1} {2} {3}".format(
    #         i+1,
    #         p_list.index(A[i].prv) + 1,
    #         p_list.index(A[i]) + 1,
    #         p_list.index(A[i].nxt) + 1))
    #     A[i].act()
    #     i += 1

    #output the lower hull
    test_mesh = geo.Mesh()
    for this_pt in p_list:
        test_mesh.add_vert((this_pt.x, this_pt.y, this_pt.z))

    i = 0
    while A[i] != __nil:
        #use turn to determine the normal orientation
        if turn(A[i].prv, A[i], A[i].nxt) < 0:
            test_mesh.add_face((p_list.index(A[i].prv) + 1,
                                p_list.index(A[i]) + 1,
                                p_list.index(A[i].nxt) + 1))
        else:
            test_mesh.add_face((p_list.index(A[i].nxt) + 1,
                                p_list.index(A[i]) + 1,
                                p_list.index(A[i].prv) + 1))
        A[i].act()
        i += 1

    #rerun the hull algo, with the data flipped
    #on z. Then flip the point order on the the
    #face on rebuild to reverse the mirror

    A = list()
    B = list()
    for i in range(2 * len(p_list)):
        A.append(None)
        B.append(None)

    x_sort(p_list)
    for this_pt in p_list:
        this_pt.z *= -1

    hull(p_list, 0, len(p_list), len(p_list), A, B, 0, len(A))


    i = 0
    while A[i] != __nil:
        #just flip the sign on turn switch to mirror
        if turn(A[i].prv, A[i], A[i].nxt) > 0:
            test_mesh.add_face((p_list.index(A[i].prv) + 1,
                                p_list.index(A[i]) + 1,
                                p_list.index(A[i].nxt) + 1))
        else:
            test_mesh.add_face((p_list.index(A[i].nxt) + 1,
                                p_list.index(A[i]) + 1,
                                p_list.index(A[i].prv) + 1))
        A[i].act()
        i += 1

    test_mesh.generate_obj(filename)



if __name__ == "__main__":
    test = list()

    # test.append((1.0, 0.0, 0.0))
    # test.append((0.1, 0.1, 1.0))
    # test.append((-1.0, 0.2, 0.1))
    # test.append((0.4, 0.3, -1.0))
    # test.append((0.3, 2.1, -0.5))
    # test.append((0.2, 1.44, 0.2))

    # test.append((5.0, 5.0, -5.0))
    # test.append((4.0, -2.0, 4.0))
    # test.append((3.0, -4.0, -3.0))
    # test.append((2.0, 1.0, 2.0))
    # test.append((1.0, 3.0, -1.0))
    # test.append((-1.0, 4.0, 1.0))
    # test.append((-2.0, 0.0, -2.0))
    # test.append((-3.0, -5.0, 3.0))
    # test.append((-4.0, 1.0, -4.0))
    # test.append((-5.0, 4.0, 5.0))

    for i in range(100):
        test.append((random.random()*20-10, random.random()*20-10, random.random()*20-10))

    chan(test)