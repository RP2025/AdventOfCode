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

def part2_rule(adj):
    return adj < 4

def count_accessible_part2(path):
    grid = load_grid(path)
    h, w = len(grid), len(grid[0])
    total_removed = 0

    while True:
        removable = []

        for r in range(h):
            for c in range(w):
                if grid[r][c] == '@' and part2_rule(count_adjacent(grid, r, c)):
                    removable.append((r, c))

        if not removable:
            break

        for r, c in removable:
            grid[r][c] = '.'

        total_removed += len(removable)

    return total_removed


print(count_accessible_part2('DAY04\Printing_Department_Sample.txt'))
