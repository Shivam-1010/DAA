
from itertools import permutations

distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(distance)
cities = list(range(n))

min_cost = float('inf')
best_route = []


for route in permutations(cities[1:]):
    path = (0,) + route + (0,)
    cost = 0

    # Calculate the total distance of the route
    for i in range(len(path) - 1):
        cost += distance[path[i]][path[i + 1]]

    # Keep the route with the minimum distance
    if cost < min_cost:
        min_cost = cost
        best_route = path

print("Best route:", " -> ".join(map(str, best_route)))
print("Minimum distance:", min_cost)
