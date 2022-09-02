def closedlist_search(Graph, search_value):
    x='0'
    closed_list =[]
    while True:
        if(search_value == x):
            print("Found: ", search_value)
            break
        else:
            G = Graph[x]
        if(len(G)==0):
            print("Not found")
            break
        else:
            closed_list.append(x)
        for temp in G:
            if temp not in closed_list:
                x = temp
            else:
                pass
    print("After Traversing following: ",closed_list)

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

n = input("Enter search value: ")
closedlist_search(Graph,n)