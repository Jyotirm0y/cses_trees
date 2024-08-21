#include<bits/stdc++.h>
using namespace std;

// void dfs(int node ,vector <int>&vis,vector <int>adj[])
// {

// vis[node]=1;
// cout<<node<<" ";
// for(auto child:adj[node])
// {
//     if(!vis[child])
//      dfs(child,vis,adj);
// }

// }

int main()

{   
    // init();
    int n;
    cin >> n;
    
    vector<pair<int, int>> edges(n - 1);
    for (int i = 0; i < n - 1; i++) {
        cin >> edges[i].first >> edges[i].second;
    }
 // Print the edges
    cout << "Edges:" << endl;
    for (const auto& edge : edges) {
        cout << "(" << edge.first << ", " << edge.second << ")" << endl;
    }

    



    // Correctly declaring a vector of vectors for the adjacency list  *****this also works
    vector<vector<int>> tree(n);

    // Building the adjacency list
    for ( auto& edge : edges) {
        tree[edge.first].push_back(edge.second);
        tree[edge.second].push_back(edge.first); // For an undirected tree 
    }  // *****this also works

    // int tree[n][n];
    // memset(tree,0,sizeof(tree));
    // for(auto& edge : tree) 
    // {tree[edge[0]][edge[1]]=1;}

// vector <int>adj[n];
//     for (auto& edge : edges) {
//     adj[edge[0]].push_back(edge[1]);
//     adj[edge[1]].push_back(edge[0]);
//     }  // *****this also works

    // tree[edge[0]].push_back(edge[1]);
    // tree[edge[1]].push_back(edge[0]);

// vector<bool> vis(n,false);

// dfs(0,vis,adj);




       // Print the adjacency list
    for (int i = 0; i < n; i++) {
        cout << "Node " << i << ": ";
        for (const int& neighbor : tree[i]) {
            cout << neighbor << " ";
        }
        cout << endl;
    }

    return 0;
}


// 5
// 0 1
// 0 2
// 1 3
// 1 4
