import math
def parse_grid(file_path):
    ops = []
    grid = []
    trash_compactor = 0
    with open(file_path) as f:
        lines = [line.strip() for line in f if line.strip()]

    ops = lines[-1].split()

    for line in lines[:-1]:
        grid.append(list(map(int, line.split())))
    
    grid = [list(col) for col in zip(*grid)]

    for op, nums in zip(ops, grid):
        if op == '*':
            trash_compactor += (math.prod(nums))
        elif op == '+':
            trash_compactor += (sum(nums))
    
    return trash_compactor


parse_grid("DAY06\trash_compactor.txt")
