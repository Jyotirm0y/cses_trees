# Importing the required libraries
from collections import deque

# Depth-first search function to calculate the distance of
# each node from a given node
def dfs(parent, node, dist, c, adj, dp):
    # Store the distance of the node from the starting node
    dp[node][c] = dist

    # Iterate over all the adjacent nodes
    for child in adj[node]:
        # If the adjacent node is not the parent
        if child != parent:
            # Recursively call for the child node and
            # increase the distance by 1
            dfs(node, child, dist + 1, c, adj, dp)

# Breadth-first search function to find the node at the
# maximum distance from a given node
def bfs(node, n, adj):
    # Queue to store the node and its distance from the
    # starting node
    q = deque([(node, 0)])

    # Visited array to keep track of visited nodes
    vis = [False] * (n + 1)

    # Mark the starting node as visited
    vis[node] = True

    while q:
        # Node at the front of the queue
        u, dist = q.popleft()

        # Iterate over all the adjacent nodes
        for child in adj[u]:
            if not vis[child]:
                # Push the node into the queue
                q.append((child, dist + 1))
                # Mark the node as visited
                vis[child] = True

    # Return the node at the maximum distance
    return u

def treedistance1(n, v):
    adj = [[] for _ in range(n + 1)]
    for i in v:
        adj[i[0]].append(i[1])
        adj[i[1]].append(i[0])

    mxdist = []
    # Node at the maximum distance from node 1
    di_st = bfs(1, n, adj)

    # Node at the maximum distance from node di_st
    di_end = bfs(di_st, n, adj)

    # 2D vector to store the maximum distance of each node
    dp = [[0, 0] for _ in range(n + 1)]

    # DFS from di_st
    dfs(0, di_st, 0, 0, adj, dp)
    # DFS from di_end
    dfs(0, di_end, 0, 1, adj, dp)

    # Take the max distance
    for i in range(1, n + 1):
        mxdist.append(max(dp[i][0], dp[i][1]))

    return mxdist

# Driver Code
def main():
    n = 5
    v = [[1, 2], [1, 3], [3, 4], [3, 5]]

    mxdist = treedistance1(n, v)
    if n == 1:
        print(0)
    for i in mxdist:
        print(i, end=" ")

if __name__ == "__main__":
    main()