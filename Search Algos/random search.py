import random
def random_search(Graph, search_value):
    x='0'
    c =[]
    while True:
        c.append(x)
        if(search_value == x):
            print("Found: ", search_value)
            break
        else:
            G = Graph[x]
            temp = random.choice(G)
            x = temp
    print("After Traversing following: ",c)

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
n = input("Enter search value in character: ")
random_search(Graph,n)
