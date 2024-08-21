#include <bits/stdc++.h>
using namespace std;

const int MAXN = 200000;
const int LOG = 18; // because 2^18 > 200000

vector<int> adj[MAXN + 1]; // adjacency list of the tree
int LCA[MAXN + 1]
       [LOG]; // LCA[i][j] stores the 2^j-th ancestor of i
int depth[MAXN + 1]; // depth of each node

// DFS to find the depth of all the nodes and initialize the
// LCA table
void dfs(int v, int p)
{
    LCA[v][0] = p;
    // Fill the LCA table
    for (int i = 1; i < LOG; ++i) {
        if (LCA[v][i - 1] != -1) {
            LCA[v][i] = LCA[LCA[v][i - 1]][i - 1];
        }
        else {
            LCA[v][i] = -1;
        }
    }
    // Explore the neoghboring nodes
    for (int u : adj[v]) {
        if (u != p) {
            depth[u] = depth[v] + 1;
            dfs(u, v);
        }
    }
}

// function to find the LCA of node a and b
int lca(int a, int b)
{
    if (depth[a] < depth[b]) {
        swap(a, b);
    }

    int diff = depth[a] - depth[b];
    for (int i = 0; i < LOG; ++i) {
        if ((diff >> i) & 1) {
            a = LCA[a][i];
        }
    }

    if (a == b) {
        return a;
    }

    for (int i = LOG - 1; i >= 0; --i) {
        if (LCA[a][i] != LCA[b][i]) {
            a = LCA[a][i];
            b = LCA[b][i];
        }
    }

    return LCA[a][0];
}

int main()
{
    int n = 5, q = 3;
    int arr[] = { 1, 1, 3, 3 };
    vector<int> parent(n + 1);
    vector<vector<int> > queries
        = { { 4, 5 }, { 2, 5 }, { 1, 4 } };

    for (int i = 1; i < n; i++) {
        parent[i + 1] = arr[i - 1];
    }
    parent[1] = -1; // General director has no boss

    for (int i = 2; i <= n; ++i) {
        adj[parent[i]].push_back(i);
        adj[i].push_back(parent[i]);
    }

    depth[1] = 0;
    dfs(1, -1);

    for (int i = 0; i < q; ++i) {
        int a = queries[i][0], b = queries[i][1];
        cout << lca(a, b) << endl;
    }

    return 0;
}
