import random
import math

# returns an array of size points with points within the x, y graphs min and max axis's
def get_points(points, min_axis, max_axis):
    a = []
    b = []
    s = []
    i = 0
    while i < points:
        a.append(round(random.uniform(min_axis, max_axis),1))
        b.append(round(random.uniform(min_axis, max_axis),1))
        s.append((a[i], b[i]))
        i += 1
    return s

# returns the initial hull with the extreme values p1 and p2, and the remaining points in s
def get_initial_hull(s):
    i = 0
    max_x = 0
    min_x = 0
    while i < len(s):
        if s[i][0] > s[max_x][0]:
            max_x = i
        if s[i][0] < s[min_x][0]:
            min_x = i
        i += 1
    x = dist_between_two_points(s, max_x, min_x)
    p2 = [(s[max_x])]
    p1 = [(s[min_x])]
    if max_x > min_x:
        del s[max_x]
        del s[min_x]
    else:
        del s[min_x]
        del s[max_x]
    return p1, p2, s

# sqrt((x - x1)^2 + (y - y1)^2) gives points distance from line given by max, min
def dist_between_two_points(s, max, min):
    x = math.pow(s[min][0] - s[max][0], 2)
    y = math.pow(s[min][1] - s[max][1], 2)
    return math.sqrt(x+y)
