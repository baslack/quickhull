"""
Adapting 2D QuickHull into 3D quick hull.

links for 3D quick hull
http://algolist.manual.ru/maths/geom/convhull/qhull3d.php
http://www.cogsci.rpi.edu/~destem/gamearch/quickhull.pdf

"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def main():
    xs = [-4.0, -2.5, -3.0, 0.0, 2.5, 5.0, 6.0]
    ys = [2.5, -7.5, 5.0, 0.0, -5.0, -5.0, 0.0]
    zs = [6.0, 3.0, 8.0, 4.0, 7.0, 3.0, 6.0]


if __name__ == "__main__":
    main()