# Represents infinity
INF = 10000000000000
# Maximum number of nodes
# MX = 200005
MX = 20
# Adjacency list
Adj = [[] for _ in range(MX)]
# Dynamic programming array
dp = [[0] * MX for _ in range(2)]




# def DFS(u, p):
#     # Initialize dp values
#     # Maximum number of pairs without including the current node
#     dp[0][u] = 0
#     # Maximum number of pairs including the current node
#     dp[1][u] = -INF

#     # Traverse through each adjacent node
#     for v in Adj[u]:
#         if v == p:
#             # Skip if it's the parent node
#             continue

#         # Recursively call DFS for child node
#         DFS(v, u)

#         # Update dp values
#         dp[0][u] += max(dp[1][v], dp[0][v])
#         opt = min(dp[0][v] - dp[1][v], 0)
#         # Update maximum pairs including the current node
#         dp[1][u] = max(dp[1][u], opt)

#     # Update dp[1] value
#     # Add pairs without the current node
#     dp[1][u] += dp[0][u]
#     # Add the current node to the matching
#     dp[1][u] += 1


# Number of nodes
n = 10

# Edges of the tree
edges = [[5, 8], [4, 6], [9, 1], [10, 4], [
    1, 3], [2, 3], [7, 9], [6, 2], [5, 10]]

# Build adjacency list
for edge in edges:
    # Convert to 0-based indexing
    a = edge[0] - 1
    # Convert to 0-based indexing
    b = edge[1] - 1
    Adj[a].append(b)
    # Undirected tree, add edge in both directions
    Adj[b].append(a)

# Start DFS from root node (0)
# DFS(0, -1)

# for vertex, neighbors in enumerate(Adj):
#     print(f"{vertex} -> {' '.join(map(str, neighbors))}")

print("Adjacency List:")
for i, neighbors in enumerate(Adj):
    print(f"Vertex {i + 1}: {', '.join(str(n + 1) for n in neighbors)}")

print(Adj)
# Output the maximum number of pairs
ans = max(dp[0][0], dp[1][0])
print("Maximum number of edges in a matching:", ans)
