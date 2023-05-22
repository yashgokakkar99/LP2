#include<bits/stdc++.h>
using namespace std;

void dfs(int **g,int start, int n){
    static int visited[15]={0};
    if(visited[start]==0)
    {
        cout<<start;
        visited[start]=1;
        for(int j=0;j<n;j++)
        {
            if(g[start][j]==1 && visited[j]==0){
                dfs(g,j,n);
            }
        }
    }
}

int main()
{
    int n;
    cout<<"Enter number of vertices : ";
    cin>>n;
    int **g = new int*[n];
    for(int i=0;i<n;i++)
    {
        g[i]=new int[n];
    }
    cout<<"Enter the adjacency matrix for graph (1 for edge and 0 for no edge) : "<<endl;
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            cin>>g[i][j];
        }
    }
    int start;
    cout<<"Enter start vertex : ";
    cin>>start;
    dfs(g,start,n);
    return 0;
}