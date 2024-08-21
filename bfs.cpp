#include<bits/stdc++.h>
using namespace std;

void bfs(vector <bool>&vis,vector <int>adj[]){
queue<int> q;
q.push(0);
vis[0]=1;
while (!q.empty())
{
    int node= q.front();
    q.pop();
    cout<<node<<endl;

    for(auto child:adj[node]){
        if(!vis[child]){
            q.push(child);
            vis[child]=1;
        }
    }
}

}

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
    vector<int> adj[n];

    // Building the adjacency list
    for ( auto& edge : edges) {
        adj[edge.first].push_back(edge.second);
        adj[edge.second].push_back(edge.first); // For an undirected tree 
    }  // *****this also works


    // for (int i = 0; i < n; i++) {
    //     cout << "Node " << i << ": ";
    //     for (const int& neighbor : tree[i]) {
    //         cout << neighbor << " ";
    //     }
    //     cout << endl;
    // }

    vector<bool> vis(n,false);
    bfs(vis,adj);

    return 0;
}



// 5
// 0 1
// 0 2
// 1 3
// 1 4
