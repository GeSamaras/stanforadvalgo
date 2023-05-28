import random


def contract(graph):
    # Randomly select an edge and merge the corresponding vertices
    while len(graph) > 2:
        # Randomly choose an edge
        u = random.choice(list(graph.keys()))
        v = random.choice(graph[u])

        # Merge vertices u and v
        graph[u].extend(graph[v])

        # Update adjacency lists of other vertices
        for vertex in graph[v]:
            graph[vertex].remove(v)
            graph[vertex].append(u)

        # Remove self-loops
        graph[u] = [vertex for vertex in graph[u] if vertex != u]

        del graph[v]


def min_cut(graph):
    min_cut_size = float("inf")
    num_iterations = int(len(graph) ** 2 * 2)  # Empirically determined value

    for _ in range(num_iterations):
        temp_graph = {vertex: neighbors[:] for vertex, neighbors in graph.items()}

        contract(temp_graph)

        cut_size = len(temp_graph[list(temp_graph.keys())[0]])

        if cut_size < min_cut_size:
            min_cut_size = cut_size

    return min_cut_size


graph = {}

with open("kargerMinCut.txt") as file:
    for line in file:
        row = list(map(int, line.split()))
        graph[row[0]] = row[1:]

min_cut_size = min_cut(graph)

print("Minimum cut size:", min_cut_size)
