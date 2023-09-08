# https://www.geeksforgeeks.org/ford-fulkerson-algorithm-for-maximum-flow-problem/

# uses adjacency matrix representation

# Returns true if there is a path from source 's' to sink 't' in residual graph.
# Also fills parent[] to store the path
def BFS(S, T, parent):

    # Mark all the vertices as not visited
    visited = [False] * len(G)

    # Create a queue for BFS
    q = []

    # Mark the source node as visited and enqueue it
    q.append(S)
    visited[S] = True

    # Standard BFS Loop
    while q:

        # Dequeue a vertex from q and print it
        u = q.pop(0)

        # Get all adjacent vertices of the dequeued vertex u.
        # If an adjacent has not been visited, then mark it visited and enqueue it.
        for idx, val in enumerate(G[u]):
            if not visited[idx] and val > 0:
                # If we find a connection to the sink node,
                # then there is no point in BFS anymore.
                # We just have to set its parent and canreturn True.
                q.append(idx)
                visited[idx] = True
                parent[idx] = u
                if idx == T:
                    return True

    # We didn't reach sink in BFS starting from source, so return False.
    return False
			
	
# Returns the maximum flow from s to t in the given graph
def FordFulkerson(S, T):
    
    # This array is filled by BFS and to store path
    parent = [-1]*len(G)

    max_flow = 0 # There is no flow initially

    # Augment the flow while there is path from S to T
    while BFS(S, T, parent):

        # Find minimum residual capacity of the edges along the path filled by BFS.
        # Or we can say find the maximum flow through the path found.
        path_flow = float("Inf")
        
        s = T
        while(s != S):
            path_flow = min(path_flow, G[parent[s]][s])
            s = parent[s]

        # Add path flow to overall flow
        max_flow += path_flow

        # update residual capacities of the edges and reverse edges along the path
        v = T
        while(v != S):
            u = parent[v]
            G[u][v] -= path_flow
            G[v][u] += path_flow
            v = parent[v]

    return max_flow

G = [[0, 16, 13, 0, 0, 0],
	[0, 0, 10, 12, 0, 0],
	[0, 4, 0, 0, 14, 0],
	[0, 0, 9, 0, 0, 20],
	[0, 0, 0, 7, 0, 4],
	[0, 0, 0, 0, 0, 0]]
source = 0; sink = 5

print("The maximum possible flow is %d " % FordFulkerson(source, sink))
