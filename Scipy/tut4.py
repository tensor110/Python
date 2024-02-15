# Graphs -> scipy.sparse.csgraph

# Connected Component: 
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse import csr_matrix
sha = np.array([[0,1,2],[1,0,0],[2,0,0]])
shanew = csr_matrix(sha)
print(connected_components(shanew))

# Dijkstra's method: Finding shortest path between two elements
# It take 3 args: return_predecessors, indices, limit
# The shortest path from element 1 to 2:
from scipy.sparse.csgraph import dijkstra
sha = np.array([[0,1,2],[1,0,0],[2,0,0]])
shanew = csr_matrix(sha)
print(dijkstra(shanew, return_predecessors= True, indices=0))

# Floyd Warshall() method: To find shortest path between all the pairs of elements
from scipy.sparse.csgraph import floyd_warshall
sha = np.array([[0,1,2],[1,0,0],[2,0,0]])
shanew = csr_matrix(sha)
print(floyd_warshall(shanew, return_predecessors= True))

# Bellman Ford() method: To find shortest path between all the pairs of elements and this method also handles negative weights as well
from scipy.sparse.csgraph import bellman_ford
sha = np.array([[0,-1,2],[1,0,0],[2,0,0]])
shanew = csr_matrix(sha)
print(bellman_ford(shanew, return_predecessors= True))

# Depth First Order: Returns a depth first traversal from node. It has 2 args: graph, starting element
from scipy.sparse.csgraph import depth_first_order
sha = np.array([[0,1,0,1],[1,1,1,1],[2,1,1,0], [0,1,0,1]])
shanew = csr_matrix(sha)
print(depth_first_order(shanew, 1))

# Breadth First Order: Returns a breadth first traversal from node. It has 2 args: graph, starting element
from scipy.sparse.csgraph import breadth_first_order
sha = np.array([[0,1,0,1],[1,1,1,1],[2,1,1,0], [0,1,0,1]])
shanew = csr_matrix(sha)
print(breadth_first_order(shanew, 1))

