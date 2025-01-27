# Python3 program to demonstrate
# multi-source BFS
import math

N = 100000 + 1
inf = 1000000

# This array stores the distances of the vertices
# from the nearest source
inf = math.inf
dist = [inf] * N

# This Set contains the vertices not yet visited in
# increasing order of distance from the nearest source
# calculated till now
Q = set()


# Util function for Multi-Source BFS
def multiSourceBFSUtil(graph, s):
    for i in range(len(graph[s])):
        v = graph[s][i]
        if (dist[s] + 1 < dist[v]):

            # If a shorter path to a vertex is
            # found than the currently stored
            # distance replace it in the Q
            if (dist[v], v) in Q:
                Q.remove((dist[v], v))
            dist[v] = dist[s] + 1
            Q.add((dist[v], v))

    # Stop when the Q is empty . All
    # vertices have been visited. And we only
    # visit a vertex when we are sure that a
    # shorter path to that vertex is not
    # possible
    if (len(Q) == 0):
        return

    # Go to the first vertex in Q
    # and remove it from the Q
    it = min(Q)
    next = it[1]
    Q.remove(it)

    multiSourceBFSUtil(graph, next)


# This function calculates the distance of
# each vertex from nearest source
def multiSourceBFS(graph, n, sources, S):
    # a hash array where source[i] = 1
    # means vertex i is a source
    source = [0] * (n + 1)

    for i in range(0, S):
        source[sources[i]] = 1

    for i in range(1, n):
        if (source[i]):
            dist[i] = 0
            Q.add((0, i))

        else:
            dist[i] = math.inf
            Q.add((math.inf, i))

    # Get the vertex with lowest distance,
    itr = min(Q)
    start = itr[1]

    Q.remove(itr)

    multiSourceBFSUtil(graph, start)

    # Print the distances
    for i in range(1, n + 1):
        print(i, dist[i])


def addEdge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


# Driver Code
if __name__ == '__main__':
    # Number of vertices
    n = 6

    graph = [[] for _ in range(n + 1)]

    # Edges
    addEdge(graph, 1, 2)
    addEdge(graph, 1, 6)
    addEdge(graph, 2, 6)
    addEdge(graph, 2, 3)
    addEdge(graph, 3, 6)
    addEdge(graph, 5, 4)
    addEdge(graph, 6, 5)
    addEdge(graph, 3, 4)
    addEdge(graph, 5, 3)

    # Sources
    sources = (1, 5)

    S = len(sources)

    multiSourceBFS(graph, n, sources, S)
