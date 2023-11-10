import numpy as np
import matplotlib.pyplot as plt
import random

def is_happy(x, y, grid):
    cell_color = grid[x, y]
    if cell_color is None:
        return True
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < grid_size and 0 <= ny < grid_size and grid[nx, ny] == cell_color:
                count += 1
    return count >= 2

def find_unhappy_cell(grid):
    candidates = []
    for x in range(grid_size):
        for y in range(grid_size):
            if not is_happy(x, y, grid) and grid[x, y] is not None:
                candidates.append((x, y))
    return random.choice(candidates) if candidates else None

def find_empty_cell(grid):
    candidates = []
    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x, y] is None:
                candidates.append((x, y))
    return random.choice(candidates) if candidates else None

def move_unhappy_cell(grid):
    unhappy_cell = find_unhappy_cell(grid)
    if unhappy_cell is not None:
        empty_cell = find_empty_cell(grid)
        if empty_cell is not None:
            grid[empty_cell], grid[unhappy_cell] = grid[unhappy_cell], grid[empty_cell]

def plot_grid(grid, iteration):
    img = np.zeros((grid_size, grid_size, 3), dtype=np.uint8)
    for x in range(grid_size):
        for y in range(grid_size):
            if grid[x, y] == 'blue':
                img[x, y] = [0, 0, 255]  # Blue color
            elif grid[x, y] == 'red':
                img[x, y] = [255, 0, 0]  # Red color
    plt.imshow(img)
    plt.title(f'Iteration {iteration}')
    plt.axis('off')
    plt.savefig(f'grid_{iteration}.png')
    plt.close()

if __name__ == '__main__':
    grid_size = 150
    blue_ratio = 0.45
    red_ratio = 0.45
    empty_ratio = 0.10

    grid = np.random.choice(['blue', 'red', None], size=(grid_size, grid_size), p=[blue_ratio, red_ratio, empty_ratio])

    for iteration in range(5000):
        move_unhappy_cell(grid)
        if iteration % 500 == 0:  # Plot every 500 iterations
            plot_grid(grid, iteration)
