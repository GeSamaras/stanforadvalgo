import random

def contraction(graph):
    while len(graph) > 2:
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])

        graph[u].extend(graph[v])
        for w in graph[v]:
            graph[w].remove(v)
            graph[w].append(u)

        graph[u] = [w for w in graph[u] if w != u]

        del graph[v]

    remaining_vertex = next(iter(graph))
    return len(graph[remaining_vertex])

graph = {}
with open("kargerMinCut.txt") as file:
    for line in file:
        vertices = list(map(int, line.strip().split("\t")))
        graph[vertices[0]] = vertices[1:]

iterations = 1000
min_cut = float('inf')

# Run the algorithm multiple times
for _ in range(iterations):
    # Create a copy of the original graph
    temp_graph = {k: v[:] for k, v in graph.items()}

    cut = contraction(temp_graph)
    if cut < min_cut:
        min_cut = cut

print("Minimum cut:", min_cut)
