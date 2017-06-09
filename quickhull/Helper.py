import random


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


def get_initial_points(s):
    i = 0
    max_x = 0
    min_x = 0
    while i < len(s):
        if s[i][0] > s[max_x][0]:
            max_x = i
        i += 1
    i = 0
    p2 = [(s[max_x])]
    del s[max_x]
    while i < len(s):
        if s[i][0] < s[min_x][0]:
            min_x = i
        i += 1
    p1 = [(s[min_x])]
    del s[min_x]
    return p1, p2, s


def get_max(s, pos):
    i = 0
    max_y = 0
    while i < len(s):
        if pos*s[i][1] > pos*s[max_y][1]:
            max_y = i
        i += 1
    return max_y
