# Implement A star Algorithm using Python.

import heapq

graph = {
    'A':[('B',1),('C',3)],
    'B':[('D',1)],
    'C':[('D',1)],
    'D':[]
}

h = {'A':3,'B':2,'C':1,'D':0}

pq = [(0,'A')]
visited = set()

while pq:
    cost,node = heapq.heappop(pq)
    if node=='D':
        print("Goal reached")
        break
    if node not in visited:
        visited.add(node)
        for n,w in graph[node]:
            heapq.heappush(pq,(cost+w+h[n],n))