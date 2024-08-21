#https://www.geeksforgeeks.org/cses-solutions-tree-distances-ii/

from collections import defaultdict

# Initialize variables
n = 5
graph = defaultdict(list)
dp = [0] * (n+1)
ans = [0] * (n+1)

# First DFS to calculate the answer for node 1 and the size of each node's subtree


def dfs1(node=1, parent=0, depth=0):
    # Add depth to the answer for node 1
    ans[1] += depth

    # Initialize the size of the subtree rooted at node to 1
    dp[node] = 1

    # For each child of node
    for i in graph[node]:
        # If the child is not the parent
        if i != parent:
            # Recurse on the child
            dfs1(i, node, depth + 1)

            # Add the size of the child's subtree to dp[node]
            dp[node] += dp[i]

# Second DFS to calculate the answer for all nodes


def dfs2(node=1, parent=0):
    # For each child of node
    for i in graph[node]:
        # If the child is not the parent
        if i != parent:
            # Calculate the answer for the child
            ans[i] = ans[node] + n - 2 * dp[i]

            # Recurse on the child
            dfs2(i, node)


# Driver code
if __name__ == "__main__":
    # Define edges
    edges = [(1, 2), (1, 3), (3, 4), (3, 5)]

    # Build the graph
    for edge in edges:
        a, b = edge
        graph[a].append(b)
        graph[b].append(a)

    # Run the first DFS
    dfs1()

    # Run the second DFS
    dfs2()

    # Print the answer for each node
    for i in range(1, n+1):
        print(ans[i], end=' ')





#   1
# 2   3
#    4  5
