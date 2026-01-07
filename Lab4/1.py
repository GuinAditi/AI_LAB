from collections import deque

# ---------------- Maze Definition ----------------
maze = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1]
]

start = (0, 0)
end = (3, 4)

rows, cols = len(maze), len(maze[0])
directions = [(0,1), (1,0), (0,-1), (-1,0)]

# ---------------- BFS (Shortest Path) ----------------
def bfs(maze, start, end):
    queue = deque([start])
    visited = set([start])
    parent = {}
    nodes_explored = 0

    while queue:
        x, y = queue.popleft()
        nodes_explored += 1

        if (x, y) == end:
            # Reconstruct path
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            path.reverse()
            return path, nodes_explored

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1:
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)
                    queue.append((nx, ny))

    return None, nodes_explored

# ---------------- DFS (Any Valid Path) ----------------
def dfs(maze, start, end):
    visited = set()
    path = []
    nodes_explored = 0

    def helper(x, y):
        nonlocal nodes_explored

        if (x, y) in visited:
            return False

        visited.add((x, y))
        path.append((x, y))
        nodes_explored += 1

        if (x, y) == end:
            return True

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1:
                if helper(nx, ny):
                    return True

        path.pop()
        return False

    found = helper(start[0], start[1])
    return (path if found else None), nodes_explored

# ---------------- Run Both Algorithms ----------------
bfs_path, bfs_nodes = bfs(maze, start, end)
dfs_path, dfs_nodes = dfs(maze, start, end)

# ---------------- Output ----------------
print("Maze Solver using BFS and DFS\n")

print("BFS (Shortest Path):")
print("Path:", bfs_path)
print("Nodes Explored:", bfs_nodes)

print("\nDFS (Any Valid Path):")
print("Path:", dfs_path)
print("Nodes Explored:", dfs_nodes)

print("\nComparison:")
if bfs_nodes < dfs_nodes:
    print("BFS explored fewer nodes.")
elif dfs_nodes < bfs_nodes:
    print("DFS explored fewer nodes.")
else:
    print("Both explored the same number of nodes.")
