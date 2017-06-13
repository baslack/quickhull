Basic Interface:

Numeric Fields:
Min X, Min Y, Min Z
Max X, Max Y, Max Z
Number of Points:
Radio Button:
Options:
QuickHull2D
Chan Minimalist
String or Browser Field:
Filename
Start Button:
Exit Button:

Start should take the
range values from the Min Max
generate a point cloud, in other words
a list of tuples of 3 elements,
of random points.

That point cloud should be submitted
to the appropriate algo, along with
the filename. The algo should hull
the point cloud and generate the obj
using the Mesh class in the geo
package.

Exit should close the app.


2D quickhull will need to have the following defined

- min x, max x for point range and axis while displaying on graph
- min y, max y for point range and axis while displaying on graph
- how many points to plot
