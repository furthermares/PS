from collections import deque

# input numbers of nodes and edges
v, e = map(int,input().split())
# initalize all nodes' indegrees to 0
indegree = [0] * (v+1)
# initalize each linked list(graph) for connected edges to each nodes
graph = [[] for i in range(v+1)]

# input all edges for Directed Acyclic Graph (DAG)
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    # increment indegree by 1
    indegree[b] += 1

# Topology sort function
def topological_sort():
    result = []
    q = deque()

    # first, append node with 0 indegrees to queue
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # repeat until queue is empty
    while q:
        # pop element
        now = q.popleft()
        result.append(now)
        # decrement conneted edges' indegrees by 1
        for i in graph[now]:
            indegree[i] -= 1
            # append nodes whose indegree newly became 0
            if indegree[i] == 0:
                q.append(i)


    # print result after the sort
    for i in result:
        print(i, end=' ')

topological_sort()

"""input
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""
"""output
1 2 5 3 6 4 7
"""
"""complexity
time: O(V + E)
"""
