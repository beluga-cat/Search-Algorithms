def BFS(Graph, node):
    queue = []
    visited = []
    visited.append(node)
    queue.append(node)
    while queue:
        x = queue.pop(0)
        print (x, end = " ") 
        for adjacents in Graph[x]:
            if adjacents not in visited:
                visited.append(adjacents)
                queue.append(adjacents)



graph = {
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
print("Breadth-First Searching Below: ")
BFS(graph, n)