import matplotlib.pyplot as plt
import random
nil = []
hull = []

def main():
    #s = [(1.1,5.0), (2.0,5.5), (3.0,5.0), (5.0,3.0), (3.0,3.0), (7.5,4.0), (7.0,5.0),(5.0,6.0),
    #     (6.0,5.5), (7.0,5.3), (6.0,3.5), (6.0,4.0), (5.0,4.0), (4.0,4.0), (3.0,4.0),(5.0,5.0),
    #     (5.0,-5.0),(2.5,-2.5),(6.7, -2.5),(1.3,0.0),(7.5,0.0),(5.0,-3.0),(5.0, 0.0)]
    s1=[]
    s2=[]
    s=[]
    a = []
    b = []
    i=0
    while i < 15:
        a.append(random.uniform(0.0, 50.0))
        b.append(random.uniform(0.0, 50.0))
        s.append((a[i], b[i]))
        i+=1

    i=0
    max = 0
    min = 0
    while i < len(s):
        if(s[i][0] < s[min][0]):
            min = i
        if (s[i][0] > s[max][0]):
            max = i
        i+=1
    p1 = []
    p2 = []
    p1.append(s[min])
    p2.append(s[max])
    if s[max][0] < s[min][0]:
        del s[min]
        del s[max]
    else:
        del s[max]
        del s[min]



    hull.append(p2[0])
    hull.append(p1[0])
    i=0
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


def split_point(s, p1, p2, pos):
    p3 = []
    index = getmax(s, pos)
    p3.append(s[index])
    del s[index]
    hull.append(p3[0])
    s1 = []
    s2 = []
    i=0
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
            if s[i][1] >= y and s[i][1] <= y2:# and s[i][0] < p3[0][0]:
                s1.append(s[i])
            elif s[i][1] <= y and s[i][1] >= y2:# and s[i][0] > p3[0][0]:
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
            x1 = (s[i][1] - b1) / m1
            x2 = (s[i][1] - b2) / m2
            if s[i][0] < x1:
                s1.append(s[i])
            elif s[i][0] > x2:
                s2.append(s[i])
            elif s[i][0] > x1 and s[i][0] < x2:
                nil.append(s[i])
            i+=1

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
    if len(s1) != 0:
        split_point(s1,p1,p3,pos)
    if len(s2) != 0:
        split_point(s2,p3,p2,pos)

def getmax(s, pos):
    i=0
    max = 0
    while i < len(s):
        if pos*s[i][1] > pos*s[max][1]:
            max = i
        i+=1
    return max

if __name__ == "__main__":
    main()