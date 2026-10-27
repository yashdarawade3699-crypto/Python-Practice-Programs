class Graph:
    def __init__(self,vertices):
        self.v=vertices
        self.adj=[[0]*vertices for _ in range (vertices)]

    def add_edge(self,u,v):
        self.adj[u][v]=1
        self.adj[v][u]=1

    def display(self):
        print("Adjacency matrix")
        for row in self.adj:
            print(row)

    def dfs(self,start,visited):
        visited[start]=True
        print(start,end='')

        for i in range(self.v):
            if self.adj[start][i]==1 and not visited[i]:
                self.dfs(i,visited)

n = int(input("Enter number of vertices: "))
g = Graph(n)
e = int(input("Enter number of edges: "))

for i in range(e):
    u, v = map(int, input("Enter edge (u v): ").split())
    g.add_edge(u, v)

g.display()

start = int(input("Enter starting vertex: "))
visited = [False] * n

print("DFS Traversal:")
g.dfs(start, visited)

