import matplotlib.pyplot as plt
import time as t
nil = []
hull = []

def main():
    s = [(1.1,5.0), (2.0,5.5), (3.0,5.0), (5.0,3.0), (3.0,3.0), (7.5,4.0), (7.0,5.0),(5.0,6.0),
         (6.0,5.5), (7.0,5.3), (6.0,3.5), (6.0,4.0), (5.0,4.0), (4.0,4.0), (3.0,4.0), (5.0,5.0)]
    p1 = [(1.0,3.0)]
    p2 = [(8.0,3.0)]
    hull.append(p2[0])
    hull.append(p1[0])
    split_point(s, p1, p2)






def split_point(s, p1, p2):
    p3 = []
    index = getmax(s)
    p3.append(s[index])
    print "p1 ", p1, " p3 ", p3, " p2 ", p2
    del s[index]
    hull.append(p3[0])
    s1 = []
    s2 = []
    i=0
    m1 = ((p1[0][1] - p3[0][1]) / (p1[0][0] - p3[0][0]))
    m2 = ((p3[0][1] - p2[0][1]) / (p3[0][0] - p2[0][0]))
    b1 = (-(m1 * p3[0][0]) + p3[0][1])
    b2 = (-(m2 * p2[0][0])) + p2[0][1]

    #print "slope 1: ", m1, " b1: ", b1, " slope 2: ", m2, " b2: ", b2
    while i < len(s):
        y = (m1 * s[i][0]) + b1
        y2 = (m2 * s[i][0]) + b2
        if s[i][1] >= y and s[i][1] <= y2:# and s[i][0] < p3[0][0]:
            s1.append(s[i])
        elif s[i][1] <= y and s[i][1] >= y2:# and s[i][0] > p3[0][0]:
            s2.append(s[i])
        elif s[i][1] > y and s[i][1] > y2:
            s1.append(s[i])
        else:
            nil.append(s[i])
        i += 1
    x3, y3 = zip(*nil)
    x4, y4 = zip(*hull)
    plt.scatter(x3, y3, marker='o', color='black')
    plt.scatter(x4, y4, marker='o', color='orange')
    if len(s1) != 0:
        x1, y1 = zip(*s1)
        plt.scatter(x1, y1, marker='x', color='blue')
    if len(s2) != 0:
        x2, y2 = zip(*s2)
        plt.scatter(x2, y2, marker='x', color='green')
    plt.show()
    if len(s1) != 0:
        split_point(s1,p1,p2)
    if len(s2) != 0:
        split_point(s2,p2,p3)

def getmax(s):
    i=0
    max = 0
    while i < len(s):
        if s[i][1] > s[max][1]:
            max = i
        i+=1
    return max

if __name__ == "__main__":
    main()