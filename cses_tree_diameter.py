# Create an adjacency list for the tree

adj = [[] for _ in range(2 * 10**5 + 5)]
adj = [[] for _ in range(2 * 10)]
# Create an array to store the distance of each node from the root
dist = [0] * (2 * 10**5 + 5)

# Depth-First Search function
def dfs(node, parent):
    # Iterate over all children of the current node
    for child in adj[node]:
        # If the child is not the parent
        if child != parent:
            # Update the distance of the child
            dist[child] = dist[node] + 1
            # Recursively call DFS for the child
            dfs(child, node)

# Number of nodes (static input)
n = 5

# Edges of the tree (static input)
edges = [(1, 2), (1, 3), (3, 4), (3, 5)]

# Add edges to the adjacency list
for a, b in edges:
    adj[a].append(b)
    adj[b].append(a)

# Initialize the distance of the first node and call DFS
dist[1] = 0
dfs(1, 0)

# Find the node with the maximum distance from the first node
maxDist = max(dist[1:])
node = dist.index(maxDist)

# Reset the distances and call DFS from the farthest node
for i in range(1, n + 1):
    dist[i] = 0
dfs(node, 0)

# Find the maximum distance from the farthest node
maxDist = max(dist[1:])

# Print the diameter of the tree
print(maxDist)


print("Adjacency List:")
for i, neighbors in enumerate(adj):
    print(f"Vertex {i + 1}: {', '.join(str(n + 1) for n in neighbors)}")
# This code is contributed by Ayush Mishra