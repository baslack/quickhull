import matplotlib.pyplot as plt
import initial_hull
import quick_hull_helper as help

nil = []
hull = []
max_axis = 10.0
min_axis = 0.0
num_points = 25
 # sdfasdh

"""
2D convex hull works fine. Just need to comment code and cleanup sections by adding function calls. 
"""


def main(s = None):
    s1 = []
    s2 = []
    if( s == None):
        s = initial_hull.get_points(num_points, min_axis, max_axis)
        print "No points were passed. Generating random points"
    #s = initial_hull.get_points(num_points, min_axis, max_axis)
    #s = [(.83,2.5),(1.0,5.0),(1.3,6.5),(4.0,4.0),(6.7,3.2),(6.6,7.1),(6.5,9.1),(8.0,7.6),(9.6,7.5)]
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
        y = (m1 * s[i][0]) + b1 # y = mx + b
        if s[i][1] > y:
            s1.append(s[i])
        elif s[i][1] < y:
            s2.append(s[i])
        else:
            nil.append(s[i])
        i += 1
    print_all(s1, s2)

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    quick_hull(s1, p1, p2)
    quick_hull(s2, p2, p1)
    print_hull()
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


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




def print_all(s1,s2):
    if len(nil) != 0:
        x3, y3 = zip(*nil)
        plt.scatter(x3, y3, marker='o', color='black')
    if len(s1) != 0:
        x1, y1 = zip(*s1)
        plt.scatter(x1, y1, marker='x', color='blue')
    if len(s2) != 0:
        x2, y2 = zip(*s2)
        plt.scatter(x2, y2, marker='x', color='green')
    x4, y4 = zip(*hull)
    plt.scatter(x4, y4, marker='o', color='orange')
    plt.axis([min_axis, max_axis, min_axis, max_axis])
    plt.grid(True)
    plt.show()

def print_hull():
    if len(nil) != 0:
        x3, y3 = zip(*nil)
        plt.scatter(x3, y3, marker='o', color='black')
    x4, y4 = zip(*hull)
    plt.scatter(x4, y4, marker='o', color='orange')
    plt.axis([min_axis, max_axis, min_axis, max_axis])
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()