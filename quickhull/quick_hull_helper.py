import math


def get_furthest_point_from_line(p1, p2, p3):
    p4 = []
    if (p1[0][0] - p2[0][0]) == 0:
        m = 0
        p_m = 0
    else:
        m = (p1[0][1] - p2[0][1]) / (p1[0][0] - p2[0][0]) # slope of hull points
        p_m = -(1.0 / m)                                # slope of line perpendicular to hull
    b = p2[0][1] - (m * p2[0][0]) # b for slope points (y = mx + b)
    p_b = p3[0][1] - (p_m * p3[0][0]) # b for perpendicular line to hull
    x = (b - p_b) / (p_m - m) # x intersection of lines
    y = (m*x) + b             # y intersection of lines
    p4.append((x,y))
    xs = pow(p3[0][0] - p4[0][0], 2)
    ys = pow(p3[0][1] - p4[0][1], 2)
    return math.sqrt(xs + ys)


def point_location(p1, p2, p3):
    cp1 = ((p2[0][0] - p1[0][0]) * (p3[0][1] - p1[0][1])) - ((p2[0][1] - p1[0][1]) * (p3[0][0] - p1[0][0]))
    if cp1 > 0:
        ret = 1
    elif cp1 == 0:
        ret = 0
    else:
        ret = -1
    return ret
