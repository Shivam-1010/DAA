# Prim's Algorithm

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

vertices = len(graph)

selected = [False] * vertices

selected[0] = True

print("Edges in Minimum Spanning Tree:")

for _ in range(vertices - 1):

    minimum = float('inf')
    start = 0
    end = 0

    for i in range(vertices):
        if selected[i]:

            
            for j in range(vertices):

                if not selected[j] and graph[i][j] != 0:

                   
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        start = i
                        end = j

    
    print(start, "->", end, "=", minimum)

    
    selected[end] = True