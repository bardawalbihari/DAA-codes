def print_grid(grid):
    for row in grid:
        for cell in row:
            print(cell, end=' ')
        print()
    print()

def fill_dominoes(grid, x, y, size, tile_number):
    if size == 2:
        # Base case: 2x2 grid, directly place dominoes
        grid[x][y] = tile_number
        grid[x][y + 1] = tile_number
        grid[x + 1][y] = tile_number
        grid[x + 1][y + 1] = tile_number
        return

    half = size // 2
    
    # Recursive calls for each quadrant
    fill_dominoes(grid, x, y, half, tile_number)
    fill_dominoes(grid, x, y + half, half, tile_number + 1)
    fill_dominoes(grid, x + half, y, half, tile_number + 2)
    fill_dominoes(grid, x + half, y + half, half, tile_number + 3)

    # Place an L-shaped tile in the center
    center_x = x + half - 1
    center_y = y + half - 1
    grid[center_x][center_y] = tile_number
    grid[center_x][center_y + 1] = tile_number
    grid[center_x + 1][center_y] = tile_number
    grid[center_x + 1][center_y + 1] = tile_number

def solve_domino_tiling(n):
    if n <= 0:
        raise ValueError("Grid size must be greater than 0.")
    grid = [[0] * n for _ in range(n)]
    fill_dominoes(grid, 0, 0, n, 1)
    return grid

# Input from the user
try:
    n = int(input("Enter the size of the grid (must be a power of 2): "))
    if (n & (n - 1)) == 0 and n > 0:  # Check if n is a power of 2
        grid = solve_domino_tiling(n)
        print("Tiled grid:")
        print_grid(grid)
    else:
        print("Invalid size. Grid size must be a positive power of 2.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
