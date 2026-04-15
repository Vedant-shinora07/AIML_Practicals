graph = {
    'A' : ['B','C'],
    'B' : ['D'],
    'C' : ['E'],
    'D' : [],
    'E' : []
}

visited = set()    # store node that are already visited

def dfs(node):
    if node not in visited:   # check if node is already visited
        print(node, end="")   # print node in traversal order
        visited.add(node)     # mark node as visited
        for neighbour in graph[node]:   # loop through all connected nodes
            dfs(neighbour)  # recursive call of function

dfs('A')