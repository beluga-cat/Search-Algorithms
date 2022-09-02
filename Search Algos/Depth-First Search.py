def DFS(visited, graph, node):
    if node not in visited:
        print (node , end = " ")
        visited.append(node)
        for adjacents in graph[node]:
            DFS(visited, graph, adjacents)



Graph = {
'0' : ['1', '6'],
'1' : ['0', '2', '6', '7'],
'2' : ['1', '3' ,'4'],
'3' : ['5', '2', '4'],
'4' : ['8', '7', '5', '3', '2'],
'5' : ['8', '3', '4'],
'6' : ['0', '1', '7'],
'7' : ['8', '6', '1', '4'],
'8' : ['4', '7', '5']
}

n = input("Enter Node: ")
print("Depth-First Search Below: ")
visited=[]
DFS(visited, Graph, n)