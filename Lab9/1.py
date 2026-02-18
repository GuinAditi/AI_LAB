import heapq

# ----------------------------
# Manhattan Heuristic
# ----------------------------
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# ----------------------------
# Get Neighbors (No Diagonal)
# ----------------------------
def get_neighbors(node, grid):
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    neighbors = []
    
    for dx, dy in directions:
        nx, ny = node[0] + dx, node[1] + dy
        
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] == 0:
                neighbors.append((nx, ny))
    
    return neighbors

# ----------------------------
# A* Algorithm
# ----------------------------
def astar(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    g_cost = {start: 0}
    parent = {}
    
    while open_list:
        _, current = heapq.heappop(open_list)
        
        if current == goal:
            break
        
        for neighbor in get_neighbors(current, grid):
            new_g = g_cost[current] + 1
            
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f = new_g + manhattan(neighbor, goal)
                heapq.heappush(open_list, (f, neighbor))
                parent[neighbor] = current
    
    return reconstruct_path(parent, start, goal)

# ----------------------------
# Reconstruct Path
# ----------------------------
def reconstruct_path(parent, start, goal):
    path = []
    current = goal
    
    while current != start:
        path.append(current)
        current = parent.get(current)
        if current is None:
            return []
    
    path.append(start)
    path.reverse()
    return path

# ----------------------------
# Print Grid in Terminal
# ----------------------------
def print_grid(grid, path, start, goal):
    path_set = set(path)
    
    print("\nFinal Grid:\n")
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) == start:
                print(" S ", end="")
            elif (i, j) == goal:
                print(" G ", end="")
            elif (i, j) in path_set:
                print(" * ", end="")
            elif grid[i][j] == 1:
                print(" # ", end="")
            else:
                print(" . ", end="")
        print()

# ----------------------------
# MAIN PROGRAM
# ----------------------------

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter grid row by row (0 = free, 1 = obstacle):")
grid = []

for i in range(rows):
    row = list(map(int, input().split()))
    grid.append(row)

print("\nEnter start position (row col): ")
start = tuple(map(int, input().split()))

print("Enter goal position (row col): ")
goal = tuple(map(int, input().split()))

path = astar(grid, start, goal)

if path:
    print_grid(grid, path, start, goal)
else:
    print("\nNo path found!")
