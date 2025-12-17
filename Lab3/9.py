# Input grid size
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input grid
grid = []
print("Enter grid values (0 = free cell, 1 = obstacle):")
for i in range(rows):
    grid.append(list(map(int, input().split())))

# Function to check boundary
def is_valid(r, c):
    return 0 <= r < rows and 0 <= c < cols

# Count obstacles
obstacles = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 1:
            obstacles += 1

print("\nNumber of obstacles:", obstacles)

# Input cell
r = int(input("\nEnter row index: "))
c = int(input("Enter column index: "))

# Check boundary
if is_valid(r, c):
    print("Cell is inside the grid")
else:
    print("Cell is outside the grid")

# Print valid neighbors
print("\nValid neighbors (Up, Down, Left, Right):")
directions = [(-1,0), (1,0), (0,-1), (0,1)]

for dr, dc in directions:
    nr, nc = r + dr, c + dc
    if is_valid(nr, nc):
        print((nr, nc), "=", grid[nr][nc])
