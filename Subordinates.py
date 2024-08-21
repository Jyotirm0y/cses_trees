# Adjacency list to represent the company structure
adj = [[] for _ in range(200005)]

# Array to store the number of subordinates for each employee
subordinates = [0] * 200005

# DFS function to calculate the number of subordinates for each employee


def dfs(node):
    for child in adj[node]:
        dfs(child)
        # Adding the number of subordinates of the child to the current node
        subordinates[node] += subordinates[child] + 1


# Number of employees
n = 5
# Direct boss for each employee 2,3,...,n
bosses = [1, 2, 2, 3]

# Building the adjacency list for the company structure
for i in range(n - 1):
    adj[bosses[i]].append(i + 2)

# Performing DFS to calculate subordinates
dfs(1)

# Printing the number of subordinates for each employee
for i in range(1, n + 1):
    print(subordinates[i], end=" ")
print()