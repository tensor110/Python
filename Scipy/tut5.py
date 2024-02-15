# Spatial Data : Data i.e. represented in a geometric space
# Triangulation: to generate this we use delaunay() Triangulation

import numpy as np
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt

sha = np.array([[2,4],[3,4],[3,0],[2,2],[4,1]])
simplices = Delaunay(sha).simplices
plt.triplot(sha[:,0], sha[:,1], simplices)
plt.scatter(sha[:,0], sha[:,1], color = 'r')
plt.show()

# Convex Hull: smallest polygon that covers all of the given point
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
share = np.array([[2,4],[3,4],[3,0],[2,2],[4,1],[1,2],[5,0],[3,1],[1,2],[0,2]])
hull = ConvexHull(share)
hull_points = hull.simplices
plt.scatter(share[:,0], share[:,1])
for i in hull_points:
    plt.plot(share[i,0], share[i,1], 'k-')
plt.show()

# KDTrees: Data structures optimized for the nearest neighbour 
from scipy.spatial import KDTree
shared = [(1,-1), (2,3), (-2,3), (2,-3)]
tree = KDTree(shared)
res = tree.query((1,1))
print(res)

# Distance Matrix: It is used to find the various type of distance between 2 points. 2 types: Euclidean Distance, Cosine Distance
# Euclidean Distance
from scipy.spatial.distance import euclidean
p1 = (1,0)
p2 = (10,2)
sh = euclidean(p1,p2)
print(sh)

# Cosine Distance
from scipy.spatial.distance import cosine
p1 = (1,0)
p2 = (10,2)
sh = cosine(p1,p2)
print(sh)