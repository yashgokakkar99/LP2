// BFS
void BFS(int G[][7], int start, int n)
{
    queue<int> q;
    int visited[7] = {0};

    int i = start;
    cout<<i;
    visited[i] = 1;
    q.push(i);

    while(!q.empty())
    {
        i = q.front();
        q.pop();
        for(int j = 1; j<n;j++)
        {
            if(G[i][j]==1 && visited[j]==0){
                cout<<j;
                q.push(j);
                visited[j] = 1;
            }
        }
    }
}

// DFS
void DFS(int G[][7],int start,int n)
{
    static int visited[7] = {0};
    if(visited[start] == 0){
        cout<<start;
        visited[start] = 1;
        for(int j=1;j<n;j++)
        {
            if(G[start][j]==1 && visited[j]==0)
            {
                DFS(G,j,n);
            }
        }
    }
}
