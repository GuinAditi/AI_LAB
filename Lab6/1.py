import heapq

def uniform_cost_search(graph, start, goal):
    # Priority Queue stores (cost, node, path)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))

    visited = set()

    while priority_queue:
        cost, current_node, path = heapq.heappop(priority_queue)

        # Skip if already visited
        if current_node in visited:
            continue
        visited.add(current_node)

        # Goal test
        if current_node == goal:
            return path, cost

        # Expand neighbors
        for neighbor, weight in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (cost + weight, neighbor, path + [neighbor])
                )

    return None, float('inf')


# Example weighted graph (Adjacency List)
graph = {
    'A': [('B', 2), ('C', 1)],
    'B': [('D', 5), ('E', 3)],
    'C': [('D', 2)],
    'D': [('E', 1)],
    'E': []
}

start = 'A'
goal = 'E'

path, total_cost = uniform_cost_search(graph, start, goal)

print("Optimal Path:", path)
print("Total Cost:", total_cost)
