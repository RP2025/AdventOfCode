# LOAD + GLOBALS
def load_grid(path):
    return [list(line.strip()) for line in open(path)]

DIRS = [(-1,-1),(-1,0),(-1,1),
        (0,-1),        (0,1),
        (1,-1), (1,0), (1,1)]

def count_adjacent(grid, r, c):
    h, w = len(grid), len(grid[0])
    return sum(
        0 <= r+dr < h and 0 <= c+dc < w and grid[r+dr][c+dc] == '@'
        for dr, dc in DIRS
    )

def part1_rule(adj):
    return adj < 4

def count_accessible_part1(path):
    grid = load_grid(path)
    return sum(
        part1_rule(count_adjacent(grid, r, c))
        for r in range(len(grid))
        for c in range(len(grid[0]))
        if grid[r][c] == '@'
    )


print(count_accessible_part1('DAY04\Printing_Department_Sample.txt'))
