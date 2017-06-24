import initial_hull
import quick_hull_helper as help
import matplotlib as plty

hull = []
nil = []

def main():
    s = [(10,1), (9,2), (8,3), (7,4), (6,5), (6,5), (7,4), (8,3), (9,2), (10,1), (9,9), (10,5), (8,1),
         (6,1), (7,2), (4,2), (2,2), (1,7)]
    step_1(s)
    i=0
    print_hull()




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


def print_hull():
    if len(nil) != 0:
        x3, y3 = zip(*nil)
        plty.scatter(x3, y3, marker='o', color='black')
    x4, y4 = zip(*hull)
    plty.scatter(x4, y4, marker='o', color='orange')
    plty.show()

if __name__ == "__main__":
    main()