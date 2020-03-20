margin=35
cellwidth=85
cellheight=34.5

a=[margin + (12*cellheight),margin+0,margin+(7*cellheight),margin+(2*cellwidth)]
b=[0,3,4,4]
c=[0,5,8,4]
d=[1,6,2,10]
e=[3,6,5,10]
f=[7,6,8,10]
#initialize with alll empty celss ltdr
cellid=[[0,0,0,0]]
ltrd=[0,0,0,0]
for i in range(1,109):
    l,r,t,d=1,1,1,1
    if(i%9==1):
        l=0
    if(i%9==0):
        r=0
    if(i<=9):
        d=0
    if(i>99):
        t=0
    ltrd=[l,t,r,d]
    cellid.append(ltrd)
p=0
for item in cellid:
    print(p)
    print(item)
    p=p+1
adjacency=[]
for j in range(0,109):
    adjrow=[]
    for i in range(0,109):
        adjrow.append(0)
    if(cellid[j][0]==1):
        adjrow[j-1]=1
    if(cellid[j][1]==1):
        print(j)
        adjrow[j+9]=1
    if(cellid[j][2]==1):
        adjrow[j+1]=1
    if(cellid[j][3]==1):
        adjrow[j-9]=1
    adjacency.append(adjrow)
p=0
for item in adjacency:
    print(p)
    print(item)
    p=p+1

graph={}
for i in range(1,109):
    lis=[];
    for j in range(0,109):
        if(adjacency[i][j]==1):
            lis.append(j)

    graph.update({i:lis})






def bfs(graph_to_search, start, end):
        queue = [[start]]
        visited = set()
        while queue:
        # Gets the first path in the queue
            path = queue.pop(0)

    # Gets the last node in the path
            vertex = path[-1]

    # Checks if we got to the end
            if vertex == end:
                return path
        # We check if the current node is already in the visited nodes set in order not to recheck it
            elif vertex not in visited:
            # enumerate all adjacent nodes, construct a new path and push it into the queue
                for current_neighbour in graph_to_search.get(vertex, []):
                    new_path = list(path)
                    new_path.append(current_neighbour)
                    queue.append(new_path)

                #No need to visit other neighbour. Return at once
                    if current_neighbour == end:
                        return new_path;

            # Mark the vertex as visited
                visited.add(vertex)


print( bfs(graph, 29, 70))

