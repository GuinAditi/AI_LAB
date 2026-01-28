import heapq

# Goal state of the puzzle
GOAL_STATE = ((1, 2, 3),
              (4, 5, 6),
              (7, 8, 0))  # 0 represents the blank tile


# Find the position of a tile
def find_position(state, value):
    for i in range(3):
        for j in range(3):
            if state[i][j] == value:
                return i, j


# Heuristic H1: Number of misplaced tiles
def h1_misplaced_tiles(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != GOAL_STATE[i][j]:
                count += 1
    return count


# Heuristic H2: Manhattan distance
def h2_manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i][j]
            if tile != 0:
                goal_i, goal_j = find_position(GOAL_STATE, tile)
                distance += abs(i - goal_i) + abs(j - goal_j)
    return distance


# Generate possible next states
def get_neighbors(state):
    neighbors = []
    x, y = find_position(state, 0)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors


# A* Search Algorithm
def a_star(start_state, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start_state))
    g_cost = {start_state: 0}
    visited = set()

    nodes_explored = 0

    while open_list:
        _, current = heapq.heappop(open_list)
        nodes_explored += 1

        if current == GOAL_STATE:
            return g_cost[current], nodes_explored

        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor in visited:
                continue

            tentative_g = g_cost[current] + 1

            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f_cost = tentative_g + heuristic(neighbor)
                heapq.heappush(open_list, (f_cost, neighbor))

    return None, nodes_explored


# Initial state
initial_state = ((1, 2, 3),
                 (4, 0, 6),
                 (7, 5, 8))


# Run A* with both heuristics
depth_h1, nodes_h1 = a_star(initial_state, h1_misplaced_tiles)
depth_h2, nodes_h2 = a_star(initial_state, h2_manhattan_distance)

# Results
print("A* using Misplaced Tiles Heuristic (H1)")
print("Solution Depth:", depth_h1)
print("Nodes Explored:", nodes_h1)

print("\nA* using Manhattan Distance Heuristic (H2)")
print("Solution Depth:", depth_h2)
print("Nodes Explored:", nodes_h2)
