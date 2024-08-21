#include<bits/stdc++.h>
using namespace std;

void dfs(int node ,vector <bool>&vis,vector <int>adj[])
{

vis[node]=1;
cout<<node<<" ";
for(auto child:adj[node])
{
    if(!vis[child]){
        printf("dfs");
     dfs(child,vis,adj);}
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

    
  vector<int> adj[n];

    // Building the adjacency list
    for ( auto& edge : edges) {
        adj[edge.first].push_back(edge.second);
        adj[edge.second].push_back(edge.first); 
    }

vector<bool> vis(n,false);

dfs(0,vis,adj);





    return 0;
}


