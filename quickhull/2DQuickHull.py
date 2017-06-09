
import matplotlib.pyplot as plt
import Helper

nil = []
hull = []
"""
2D convex hull works fine. Just need to comment code and cleanup sections by adding function calls. 
"""


def main():
    s1 = []
    s2 = []
    s = Helper.get_points()
    p1, p2, s = Helper.get_initial_points(s)

    hull.append(p2[0])
    hull.append(p1[0])

    i = 0
    if (p1[0][0] - p2[0][0]) == 0:
        m1 = 0
    else:
        m1 = ((p1[0][1] - p2[0][1]) / (p1[0][0] - p2[0][0]))
    b1 = (-(m1 * p2[0][0]) + p2[0][1])
    while i < len(s):
        y = (m1 * s[i][0]) + b1
        if s[i][1] > y:
            s1.append(s[i])
        elif s[i][1] < y:
            s2.append(s[i])
        else:
            nil.append(s[i])
        i += 1

    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
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
    plt.axis([-5, 50, -5, 50])
    plt.grid(True)
    plt.show()
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    split_point(s1, p1, p2, 1)
    split_point(s2, p1, p2, -1)
    x4, y4 = zip(*hull)
    plt.scatter(x4, y4, marker='o', color='orange')
    if len(nil) != 0:
        x3, y3 = zip(*nil)
        plt.scatter(x3, y3, marker='o', color='black')
    plt.axis([-5, 50, -5, 50])
    plt.grid(True)
    plt.show()


def split_point(s, p1, p2, pos):
    p3 = []
    index = Helper.get_max(s, pos)
    p3.append(s[index])
    del s[index]
    hull.append(p3[0])
    s1 = []
    s2 = []
    i = 0
    if (p1[0][0] - p3[0][0]) == 0:
        m1 = 0
    else:
        m1 = ((p1[0][1] - p3[0][1]) / (p1[0][0] - p3[0][0]))
    if (p3[0][0] - p2[0][0]) == 0:
        m2 = 0
    else:
        m2 = ((p3[0][1] - p2[0][1]) / (p3[0][0] - p2[0][0]))
    b1 = (-(m1 * p3[0][0]) + p3[0][1])
    b2 = (-(m2 * p2[0][0])) + p2[0][1]
    if pos == 1:
        while i < len(s):
            y = (m1 * s[i][0]) + b1
            y2 = (m2 * s[i][0]) + b2
            if s[i][1] >= y and s[i][1] <= y2:
                s1.append(s[i])
            elif s[i][1] <= y and s[i][1] >= y2:
                s2.append(s[i])
            elif s[i][1] > y and s[i][1] > y2 and ((s[i][1] - y) < (s[i][1] - y2)):
                s2.append(s[i])
            elif s[i][1] > y and s[i][1] > y2 and ((s[i][1] - y) > (s[i][1] - y2)):
                s1.append(s[i])
            else:
                nil.append(s[i])
            i += 1
    if pos == -1:
        while i < len(s):
            y = (m1 * s[i][0]) + b1
            y2 = (m2 * s[i][0]) + b2
            if s[i][1] < y:
                s1.append(s[i])
            elif s[i][1] < y2:
                s2.append(s[i])
            else:
                nil.append(s[i])
            i += 1
    if len(s1) != 0:
        split_point(s1, p1, p3, pos)
    if len(s2) != 0:
        split_point(s2, p3, p2, pos)


if __name__ == "__main__":
    main()