# Implement water jug problem puzzle using state space search.

from collections import deque

def water_jug(x, y, target):
    visited = set()
    q = deque([(0,0)])

    while q:
        a,b = q.popleft()
        if (a,b) in visited: continue

        print(a,b)
        visited.add((a,b))

        if a==target or b==target:
            print("Target reached")
            return

        q.extend([
            (x,b),(a,y),(0,b),(a,0),
            (min(a+b,x), b-(min(a+b,x)-a)),
            (a-(min(a+b,y)-b), min(a+b,y))
        ])

water_jug(4,3,2)