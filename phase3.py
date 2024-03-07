def count_islands_and_create_records(grid):
    if not grid or not grid[0]:
        return 0  # Empty grid

    m, n = len(grid), len(grid[0])
    islands_count = 0

    def dfs(row, col, island_id):
        if 0 <= row < m and 0 <= col < n and grid[row][col] == '1':
            grid[row][col] = island_id  # Mark the cell as visited
            # Explore adjacent cells
            dfs(row + 1, col, island_id)
            dfs(row - 1, col, island_id)
            dfs(row, col + 1, island_id)
            dfs(row, col - 1, island_id)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                islands_count += 1
                island_id = f'Island_{islands_count}'  # Generate unique island ID
                dfs(i, j, island_id)

    # Create records in the database for each island
    for i in range(m):
        for j in range(n):
            if grid[i][j] != '0':
                island_id = grid[i][j]
                # Replace the following line with your actual database insertion code
                print(f"Inserted record for island {island_id} into the database")

    return islands_count

# User input for the binary grid
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
image_grid = []
print("Enter the binary grid (each row separated by spaces):")
for _ in range(m):
    row = input().split()
    image_grid.append(row)

num_islands = count_islands_and_create_records(image_grid)
print(f'Number of islands: {num_islands}')