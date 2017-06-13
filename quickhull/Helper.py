import random
import math


def get_points():
    a = []
    b = []
    s = []
    i = 0
    while i < 15:
        a.append(random.uniform(0.0, 50.0))
        b.append(random.uniform(0.0, 50.0))
        s.append((a[i], b[i]))
        i += 1
    return s


def get_initial_hull(s):
    i = 0
    max_x = 0
    min_x = 0
    min_y = 0
    max_y = 0
    while i < len(s):
        if s[i][0] > s[max_x][0]:
            max_x = i
        if s[i][0] < s[min_x][0]:
            min_x = i
        if s[i][1] > s[max_y][0]:
            max_y = i
        if s[i][1] < s[min_y][0]:
            min_y = i
        i += 1
    x = dist(s, max_x, min_x)
    y = dist(s, max_y, min_y)
    if x > y:
        p1 = [(s[max_x])]
        p2 = [(s[min_x])]
        if max_x > min_x:
            del s[max_x]
            del s[min_x]
        else:
            del s[min_x]
            del s[max_x]
    else:
        p1 = [(s[max_y])]
        p2 = [(s[min_y])]
        if max_y > min_y:
            del s[max_y]
            del s[min_y]
        else:
            del s[min_y]
            del s[max_y]
    #print x, " ", y, " ", p1, " ", s[max_x], " ", s[max_y]
    return p1, p2, s


def get_max(s, p1, p2):
    i=0
    if (p1[0][0] - p3[0][0]) == 0:
        m1 = 0
    else:
        m1 = ((p1[0][1] - p2[0][1]) / (p1[0][0] - p2[0][0]))
    b1 = (-(m1 * p2[0][0]) + p2[0][1])
    while i < len(s):
        y = (m1 * s[i][0]) + b1
        x = math.pow((s[i][0], y) - s[max][0], 2)
        y = math.pow(s[min][1] - s[max][1], 2)
        line = []
        point = [(s[i])]
        dist(s, line, point)



def dist(s, max, min):
    x = math.pow(s[min][0] - s[max][0], 2)
    y = math.pow(s[min][1] - s[max][1], 2)
    return math.sqrt(x+y)