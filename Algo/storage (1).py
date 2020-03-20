import json
row=[]
grid=[]
#json file details
def fetchdata(item):
    with open('fgdata1.json','r')as f:
        data=json.load(f)
    for items in data:
        if(items['cellno']==item):
            return items

# graph to search shortest path
def bfs(graph_to_search, start, end):
    queue = [[start]]
    visited = set()
    while queue:
        path = queue.pop(0)
        vertex = path[-1]
        if vertex == end:
            return path
        elif vertex not in visited:
            for current_neighbour in graph_to_search.get(vertex, []):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)
                if current_neighbour == end:
                    return new_path;

            visited.add(vertex)
# grid representaion
for i in range(0,9):
    row.append(0)
for i in range (1,7):
    grid.append(row)
print(grid)
cellid=[[0,0,0,0]]
ltrd=[0,0,0,0]
for i in range(1,55):
    l,r,t,d=1,1,1,1
    if(i%9==1):
        l=0
    if(i%9==0):
        r=0
    if(i<=9):
        d=0
    if(i>45):
        t=0
    ltrd=[l,t,r,d]
    cellid.append(ltrd)
p=0
for item in cellid:
    print(p)
    print(item)
    p=p+1
adjacency=[]
grid1=[]
for j in range(0,55):
    adjrow=[]
    for i in range(0,55):
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
#adjacency done
nodelist=[x for x in range(1,55)]
print(nodelist)
#nodelist graph for implementing the bfs
def graphmake(adjacency):
    graph = {}
    for i in range(1, 55):
        lis = []
        for j in range(0, 55):
            if (adjacency[i][j] == 1):
                lis.append(j)

        graph.update({i: lis})
    graphc = graph.copy()
    return graphc
#updating the adjacencty matrix to update the graph
def updateadj(adjacency,cellid,op): #if op =0, pick up, if op=1, place
    if(op==0):
        listupdate=[]
        if (cellid > 9):
            listupdate.append(cellid - 9)
        if (cellid <= 45):
            listupdate.append(cellid + 9)
        if (cellid % 9 == 0):
            listupdate.append(cellid - 1)
        if (cellid % 9 == 1):
            listupdate.append(cellid + 1)
        if (cellid % 9 > 1):
            listupdate.append(cellid + 1)
            listupdate.append(cellid - 1)
        listupdate=intersection(nodelist,listupdate)
        for i in listupdate:
            adjacency[i][cellid]=1
            adjacency[cellid][i]=1
        nodelist.append(cellid)




    else:
        nodelist.remove(cellid)
        for i in range(0,55):
            adjacency[cellid][i]=0
        if(cellid>9):
            adjacency[cellid-9][cellid]=0
        if (cellid<=45):
            adjacency[cellid+9][cellid]=0
        if (cellid%9==0):
            adjacency[cellid - 1][cellid] = 0
        if (cellid%9==1):
            adjacency[cellid+1][cellid] = 0
        if(cellid%9>1):
            adjacency[cellid + 1][cellid] = 0
            adjacency[cellid - 1][cellid] = 0
    return adjacency




pathlist=[3,12,21,30,39,46,47,48,49,50,51,52,53,54]
#priority of a cell
def fgupdate():
    with open('fgdata1.json','r')as f:
        data=json.load(f)
    for dataitems in data:
        if(dataitems['flag']==1):
            updateadj(adjacency,dataitems['cellno'],1)
def cellproir(cellid):
    priority=0
    for i in adjacency[cellid]:
        if(i==1):
            priority=priority+1
    return priority
def gridlst(grid):
    gridlist=[]
    grid1=1
    grid2= 4
    grid3=6
    grid1end=2
    grid2end=5
    grid3end=9
    if(grid=="grid1"):
        gridstart=grid1
        gridend=grid1end
    if (grid == "grid2"):
        gridstart = grid2
        gridend = grid2end
    if (grid == "grid3"):
        gridstart = grid3
        gridend = grid3end
    for i in range(6,9):
        gridlist.append(i)
        gridlist.append(i+9)
        gridlist.append(i+18)
        gridlist.append(i+27)
        gridlist.append(i+36)


    return gridlist


print("cellprior")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(cellproir(9)) #if priroty=0 then it is blocked
print(gridlst("grid3"))


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
def allocate(grid,weight):
    prioritylist=[]
    prioritynode=[]
    priornode=[]
    print(gridlst(grid))
    def Diff(li1, li2):
        return (list(set(li1) - set(li2)))
    weightcheck=Diff(gridlst(grid),nodelist)
    grid=intersection(gridlst(grid),nodelist)
    if(len(grid)==0):
        print("cannot be allocated")
        allocate("grid2",weight)


    for i in intersection(gridlst(grid),nodelist):
        print(i,"----------------------------")
        prioritylist.append(cellproir(i))
        priornode.append(i)
    min1=min(prioritylist)
    for i in range(0,len(prioritylist)):
        if(prioritylist[i]==min1):
            prioritynode.append(priornode[i])
    print("lenelenenenenenen",len(prioritylist))
    print(len(prioritynode))
    print("--------------------------------------------------------------------------------------------------------------")
    print(prioritynode)
    if (len(prioritynode)==1):
        print("allocate1",prioritynode[0])
        return prioritynode[0]
    if (len(weightcheck)==0):
        print("allocate2",prioritynode[0])
        print("weightcheck is zer0")
        return (prioritynode[0])
    else:
        for item in weightcheck:
            dictdata = fetchdata(item)
            print(dictdata)
            if (abs(dictdata['weight'] - weight) < 2):
                print('###################################################################')
                print(dictdata['cellno'])
                print(bfs(graphc, 3, dictdata['cellno']))
                listofcells = bfs(graphc, 3, dictdata['cellno'])
                if (cellproir(listofcells[-1]) > min1):
                    print("at this location")
                    updateadj(dictdata['cellno'], 1)
                    return prioritynode[0]
                print("list of cells")
                updateadj(dictdata['cellno'], 1)
                return listofcells[0]
        return prioritynode[0]
    return (prioritynode[0])

def allocation(grid,weight):
    data=[]
    fgupdate()
    cell=(allocate(grid,weight))
    print(cell)
    print("cell allocated-----------------------------------------------")
    print(bfs(graphmake(adjacency),3,cell))
    with open('fgdata1.json','r')as f:
        data=json.load(f)
    for i in range(0,len(data)):
        print("in for")
        #987 14810716,977 1107437, 971   1072280,969 14810724
        if (data[i]['rfid']=="14810716"):
            data[i]['flag']=1
            data[i]['cellno']=cell

    with open('fgdata1.json','w') as f:
        print(data)
        json.dump(data,f)

    print(type(data))
    return cell

print(bfs(graphmake(adjacency),3,6))



















