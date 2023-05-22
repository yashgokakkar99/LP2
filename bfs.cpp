#include<bits/stdc++.h>
using namespace std;

void bfs(int **g,int start,int n)
{
    queue<int> q;
    int i=start;
    int visited[15]={0};
    cout<<i;
    visited[i]=1;
    q.push(i);
    while(!q.empty())
    {
        i=q.front();
        q.pop();
        for(int j=0;j<n;j++)
        {
            if(g[i][j]==1 && visited[j]==0)
            {
                cout<<j;
                visited[j]=1;
                q.push(j);
            }
        }
    }
}

int main()
{
    int n;
    cout<<"Enter number of vertices : ";
    cin>>n;
    int **g=new int*[n];
    for(int i=0;i<n;i++)
    {
        g[i]=new int[n];
    }
    cout<<"Enter the adjacency matrix for graph (1 for edge and 0 for no edge) : ";
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<n;j++)
        {
            cin>>g[i][j];
        }
    }
    int start;
    cout<<"Enter start : ";
    cin>>start;
    bfs(g,start,n);
    return 0;
}