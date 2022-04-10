############## problem 1 ############

'''
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). 
The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a
bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, 
and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to
 destination, or false otherwise.
'''

'''

Example 1:

Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2


Example 2:

Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.

'''

def validPath(n: int, edges, source: int, destination: int) -> bool:
    adj_element = {}

    for i in edges:
        if i[0] in adj_element:
            adj_element[i[0]].append(i[1])
        else:
            adj_element[i[0]] = [ i[1] ]


        if i[1] in adj_element:
            adj_element[i[1]].append(i[0])
        else:
            adj_element[i[1]] = [ i[0] ]

    # print(adj_element)

    queue = [source]
    visited = [source]

    while queue:

        val = queue.pop(0)

        if val == destination:
            return True

        if val in adj_element:
            for j in adj_element[val]:
                if j not in visited:
                    queue.append(j)
                    visited.append(j)

    return False


# n = 3
# edges = [[0,1],[1,2],[2,0]]
# source = 0
# destination = 2


n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5


print(validPath(n, edges, source, destination))

