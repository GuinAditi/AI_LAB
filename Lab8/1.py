import heapq
import copy

# Manhattan Distance
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Reconstruct Path
def reconstruct_path(parent, start, goal):
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = parent.get(node)
        if node is None:
            return []
    path.append(start)
    path.reverse()
    return path

# Search Function
def search(grid, start, goal, algorithm):
    rows = len(grid)
    cols = len(grid[0])
    
    pq = []
    visited = set()
    parent = {}
    g_cost = {start: 0}
    
    heapq.heappush(pq, (manhattan(start, goal), start))
    
    while pq:
        cost, current = heapq.heappop(pq)
        
        if current in visited:
            continue
        
        visited.add(current)
        
        if current == goal:
            break
        
        x, y = current
        neighbors = [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]
        
        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                
                if (nx, ny) not in visited:
                    
                    if algorithm == "gbfs":
                        priority = manhattan((nx, ny), goal)
                    
                    elif algorithm == "astar":
                        new_g = g_cost[current] + 1
                        g_cost[(nx, ny)] = new_g
                        priority = new_g + manhattan((nx, ny), goal)
                    
                    heapq.heappush(pq, (priority, (nx, ny)))
                    parent[(nx, ny)] = current
    
    return reconstruct_path(parent, start, goal), visited


# Terminal Visualization
def print_grid(grid, path, visited, start, goal, title):
    rows = len(grid)
    cols = len(grid[0])
    
    display = [["0" for _ in range(cols)] for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                display[r][c] = "#"
    
    for r, c in visited:
        display[r][c] = "."
    
    for r, c in path:
        display[r][c] = "*"
    
    sr, sc = start
    gr, gc = goal
    display[sr][sc] = "S"
    display[gr][gc] = "G"
    
    print(f"\n--- {title} ---\n")
    for row in display:
        print("  ".join(row))


# ---------------- MAIN PROGRAM ----------------

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

grid = []
print("Enter grid row by row (0 = free, 1 = obstacle)")
for i in range(rows):
    row = list(map(int, input().split()))
    grid.append(row)

sx, sy = map(int, input("Enter start position (row col): ").split())
gx, gy = map(int, input("Enter goal position (row col): ").split())

start = (sx, sy)
goal = (gx, gy)

# Run both algorithms
path_gbfs, visited_gbfs = search(copy.deepcopy(grid), start, goal, "gbfs")
path_astar, visited_astar = search(copy.deepcopy(grid), start, goal, "astar")

# Print Results
print_grid(grid, path_gbfs, visited_gbfs, start, goal, "GBFS Result")
print("Path Length:", len(path_gbfs))
print("Nodes Visited:", len(visited_gbfs))

print_grid(grid, path_astar, visited_astar, start, goal, "A* Result")
print("Path Length:", len(path_astar))
print("Nodes Visited:", len(visited_astar))

# Comparison
print("\n--- Performance Comparison ---")

if len(path_astar) < len(path_gbfs):
    print("A* found shorter path ✅")
elif len(path_astar) > len(path_gbfs):
    print("GBFS found shorter path")
else:
    print("Both found equal path length")

if len(visited_astar) < len(visited_gbfs):
    print("A* explored fewer nodes ✅")
elif len(visited_astar) > len(visited_gbfs):
    print("GBFS explored fewer nodes")
else:
    print("Both explored same number of nodes")
