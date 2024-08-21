#include<bits/stdc++.h>
using namespace std;

void dfs(int node,vector<bool>&vis,vector<int>adj[],vector<int>&dp)
{
    vis[node] = true;
    for (auto child: adj[node])
    {
        if(!vis[child]){
            dfs(child,vis,adj,dp);
            dp[node] +=(dp[child]);
            dp[node]++; 
        }
    }
}



int main()

{

int n;
cin>>n;

    
//     vector<pair<int, int>> edges(n - 1);
//     for (int i = 0; i < n - 1; i++) {
//         cin >> edges[i].first >> edges[i].second;
//     }

//     cout << "Edges:" << endl;
//     for (const auto& edge : edges) {
//         cout << "(" << edge.first << ", " << edge.second << ")" << endl;
//     }



//   vector<int> adj[n];

 
//     for ( auto& edge : edges) {
//         adj[edge.first].push_back(edge.second);
//         adj[edge.second].push_back(edge.first); 
//     }

 vector<int> adj[n+1];
 for (int i = 0; i < =n; i++){
int num;
cin>num;
adj[num].push_back(i);
adj[i].push_back(num);

 }
    for (int i = 0; i < n; i++) {
        cout << "Node " << i << ": ";
        for (const int& neighbor : adj[i]) {
            cout << neighbor << " ";
        }
        cout << endl;
    }

vector<bool> vis(n+1,false);
vector<int> dp(n+1,0);

dfs(1,vis,adj,dp);

for(int i=0;i<=n;i++)
{
    cout<<dp[i] << " ";
}


return 0;

}