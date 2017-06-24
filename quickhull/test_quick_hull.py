import initial_hull
import quick_hull_helper as help

hull = []
nil = []

# unit testing algorithm for quickhull
# if the algorithm obtains the correct hull nothing is printed
# if the algorithm doesnt obtain the correct hull "Test <test number> failed" will be printed

def main():
    # first test: circle
    s1 = [(0.1,4.0), (0.5,2.0), (0.5,5.0), (0.7,6.0), (1.1,1.1), (2.0,0.5), (3.0,.1), (4.0,.3), (5.0,.5),
         (5.8,1.0), (6.5,2.0), (6.9,3.0), (7.0,3.9), (6.5,5.0), (6.0,5.7), (5.0,6.3), (4.0,6.9), (3.0,7.0),
         (2.0,6.5)]
    step_1(s1)
    s1solution = [(6.9, 3.0), (0.5, 2.0), (3.0, 7.0), (0.7, 6.0), (0.5, 5.0), (6.0, 5.7),
                  (4.0, 6.9), (6.5, 5.0), (3.0, 0.1), (5.8, 1.0), (6.5, 2.0), (5.0, 0.5),
                  (1.1, 1.1), (2.0, 0.5)]
    if(sorted(hull) == sorted(s1solution)):
        i=0
        # good
    else:
        print "Test 1 failed"
    # second test: cloud of points
    del hull[:]
    s2 = [(9.3, 2.8), (5.9, 4.3), (3.3, 5.0), (5.9, 2.5), (0.7, 8.1), (10.0, 2.9), (5.7, 4.8), (8.2, 5.7),
          (1.8, 4.1), (5.1, 7.3), (7.6, 5.1), (5.8, 2.8), (5.0, 1.8), (9.3, 5.7), (7.8, 3.4), (6.9, 4.2),
          (4.1, 5.1), (8.5, 7.2), (7.9, 7.5), (7.7, 3.8), (4.6, 4.1), (2.2, 7.9), (1.5, 2.6), (0.9, 1.7), (4.0, 9.8)]

    step_1(s2)
    s2solution = [(0.9, 1.7), (2.2, 7.9), (4.0, 9.8), (5.0, 1.8), (8.5, 7.2), (9.3, 2.8), (9.3, 5.7)]
    if (sorted(hull) == sorted(s2solution)):
        i = 0
        # good
    else:
        print "Test 2 failed"
    # third test: cloud of points
    del hull[:]
    s3 = [(1.0, 4.7), (9.5, 0.1), (6.2, 9.8), (0.1, 5.2), (9.4, 6.2), (2.7, 3.4), (8.6, 1.4), (3.8, 8.5),
          (5.2, 7.4), (1.9, 1.9), (3.8, 3.5), (9.6, 6.1), (1.9, 7.6), (0.4, 7.8), (0.3, 2.8), (6.3, 4.1),
          (3.1, 3.7), (9.2, 8.6), (5.2, 6.5), (8.7, 7.1), (4.5, 3.2), (5.6, 1.8), (2.6, 4.3), (8.1, 4.9), (7.4, 1.6)]
    step_1(s3)
    s3solution = [(9.5, 0.1), (0.3, 2.8), (6.2, 9.8), (0.4, 7.8), (9.2, 8.6), (9.4, 6.2), (1.9, 1.9)]
    if (sorted(hull) == sorted(s3solution)):
        i = 0
        # good
    else:
        print "Test 2 failed"


def step_1(s):

    p1, p2, s = initial_hull.get_initial_hull(s)
    s1 = []
    s2 = []
    p1, p2, s = initial_hull.get_initial_hull(s)

    hull.append(p2[0])
    hull.append(p1[0])

    i = 0
    if (p1[0][0] - p2[0][0]) == 0:
        m1 = 0
    else:
        m1 = ((p1[0][1] - p2[0][1]) / (p1[0][0] - p2[0][0]))
    b1 = (-(m1 * p2[0][0]) + p2[0][1])
    while i < len(s):
        y = (m1 * s[i][0]) + b1  # y = mx + b
        if s[i][1] > y:
            s1.append(s[i])
        elif s[i][1] < y:
            s2.append(s[i])
        else:
            nil.append(s[i])
        i += 1
    #main.print_all(s1, s2, -10, 10, -10, 10)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    quick_hull(s1, p1, p2)
    quick_hull(s2, p2, p1)
    #main.print_hull(-10, 10, -10, 10)


def quick_hull(s, p1, p2):
    i=0
    s1 = []
    s2 = []
    # if s is empty return
    if len(s) == 0:
        return
    # if s has 1 element, add it to the hull
    elif len(s) == 1:
        hull.append(s[0])
        del s[0]
        return
    # else get the max distance point from the hull being looked at, add to hull, divide remaining points
    else:
        index = 0
        max_point = -1
        p3 = []
        while i < len(s):
            p3.append(s[i])
            dist = help.get_furthest_point_from_line(p1, p2, p3)
            del p3[0]
            if dist > max_point:
                max_point = dist
                index = i

            i += 1
    p3.append(s[index])
    hull.append(s[index])
    del s[index]
    i = 0
    temp = 1
    while temp == 1:
        temp = -1
        i=0
        while i < len(s) and temp == -1:
            point = []
            point.append(s[i])
            if help.point_location(p1, p3, point) == 1:
                s1.append(s[i])
                del s[i]
                temp = 1
            del point[0]
            i += 1
    i = 0
    temp = 1
    while temp == 1:
        temp = -1
        i=0
        while i < len(s) and temp == -1:
            point = []
            point.append(s[i])
            if help.point_location(p3, p2, point) == 1:
                s2.append(s[i])
                del s[i]
                temp = 1
            del point[0]
            i += 1
    i = 0
    temp = 1
    while temp == 1:
        temp = -1
        i = 0
        while i < len(s) and temp == -1:
            nil.append(s[i])
            del s[i]
            temp = 1
        i += 1
    quick_hull(s1, p1, p3)
    quick_hull(s2, p3, p2)

if __name__ == "__main__":
    main()