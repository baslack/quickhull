# http://www.geeksforgeeks.org/quickhull-algorithm-convex-hull/
# https://stackoverflow.com/questions/17478779/make-scatter-plot-from-set-of-points-in-tuples
# b = ((a[min_x][1] - a[max_x][1]) / ((a[min_x][0] - a[max_x][0]))) * (-a[max_x][0]) + a[max_x][1]
# slope = (a[min_x][1] - a[max_x][1]) / (a[min_x][0] - a[max_x][0])


# beginnings of 2D quick hull to later adapt to 3D

import matplotlib.pyplot as plt

hull = []
stale = []


def main():
    a = ([(1.0, 2.0), (2.0, 3.0), (4.0, 3.0), (9.0, 3.0), (2.0, 7.0), (6.0, 8.0), (1.0, 9.0), (5.0,1.0)])
    x, y = zip(*a)
    plt.scatter(x, y, marker='o', color='black')
    plt.show()
    quick_hull(a)


def quick_hull(a):
    # 1. find max and min x values and add them to convex hull: points A and B.
    min = 0
    max = 0
    i = 0
    while i < len(a):
        if a[i] < a[min]:
            min = i
        if a[i] > a[max]:
            max = i
        i += 1
    hull.append(a[min])
    hull.append(a[max])
    min_x = [a[min]]
    max_x = [a[max]]
    if max > min:
        del a[max]
        del a[min]
    else:
        del a[min]
        del a[max]


    # 2. put all remaining points into s1 and s2, where s1 is all
    #    points on the right side of line A -> B, and
    #    s2 are all points on the right side of line B -> A
    top = []
    bot = []
    i = 0
    slope = ((min_x[0][1] - max_x[0][1]) / (min_x[0][0] - max_x[0][0]))
    b = ((((min_x[0][1] - max_x[0][1]) / (min_x[0][0] - max_x[0][0])) * (-max_x[0][0])) + max_x[0][1])
    while i < len(a):
        y = (slope * a[i][0]) + b
        if y >= a[i][1]:
            top.append(a[i])
        elif y < a[i][1]:
            bot.append(a[i])
        i += 1

    x, y = zip(*top)
    plt.scatter(x,y, marker = 'x', color = 'green')
    xhull, yhull = zip(*hull)
    plt.plot(xhull, yhull, marker = 'o', color='orange')
    x1,y1 = zip(*bot)
    plt.scatter(x1, y1, marker = 'x', color = 'blue')
    plt.show()
    # 3. find_hull(s1, A, B)
    # 4. find_hull(s2, B, A)



def find_hull(s, p, q):
    s1 = []
    s2 = []
    i=0
    min=0
    while i < len(s):
        if s[i] > s[min]:
            min = i
    hull.append(s[min])
    min_x = [s[min]]
    del s[min]

    # find points on the convex hull that are on the right side of p -> q.
    # 1. find point furthest away from p -> q
    # 2. add the point to the convex hull between p and q. p -> new point -> q
    # 3. partition remaining points into s1, s2, and s0. s1 are points on the right of the line from p -> new point
    #    s2 are points ont he right from new point -> q, and s0 are points inside the triangle
    # 4. find_hull(s1, p, c)
    if len(s1) != 0:
        find_hull(s1, p, min_x)
    # 5. find_hull(s2, c, q)
    if len(s2) != 0:
        find_hull(s2, min_x, q)

def split_point(s, p1, p2, p3):
    top = []
    bot = []
    i=0
    slope = ((p1[0][1] - p2[0][1]) / (p1[0][0] - p2[0][0]))
    slope2 = ((p2[0][1] - p3[0][1]) / (p2[0][0] - p3[0][0]))
    b = ((((p1[0][1] - p2[0][1]) / (p1[0][0] - p2[0][0])) * (-p2[0][0])) + p2[0][1])
    b2 = ((((p2[0][1] - p3[0][1]) / (p2[0][0] - p3[0][0])) * (-p3[0][0])) + p3[0][1])
    while i < len(s):
        y = (slope * s[i][0]) + b
        y2 = (slope2 * s[i][0]) + b
        if y >= s[i][1]:
            top.append(s[i])
        elif y < s[i][1]:
            bot.append(s[i])
        i += 1
    return top, bot

if __name__ == "__main__":
    main()

# links for 3D quickhull
# http://algolist.manual.ru/maths/geom/convhull/qhull3d.php
# http://www.cogsci.rpi.edu/~destem/gamearch/quickhull.pdf