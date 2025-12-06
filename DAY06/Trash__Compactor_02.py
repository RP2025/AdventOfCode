import math
def parse_cephalopod_numbers(path):
    lines = [line.rstrip("\n") for line in open(path)]
    H = len(lines)
    W = max(len(line) for line in lines)
    grid_lines = [line.ljust(W) for line in lines]

    trash_compactor = 0

    grids = []
    ops = lines[-1].split()
    ops = ops[::-1]
    col = W - 1
    while col >= 0:
       if all(grid_lines[row][col] == ' ' for row in range(H-1)):
            col -= 1
            continue

        problem_cols = []
        while col >= 0 and not all(grid_lines[row][col] == ' ' for row in range(H-1)):
            problem_cols.append(col)
            col -= 1

        problem_cols = problem_cols[::-1] 
        numbers = []
        for c in problem_cols:
            digits = ''.join(grid_lines[r][c] for r in range(H-1)).strip()
            numbers.append(int(digits))

        grids.append(numbers[::-1])  
        
    for op, nums in zip(ops, grids):
        if op == '*':
            trash_compactor += (math.prod(nums))
        elif op == '+':
            trash_compactor += (sum(nums))
  
    return trash_compactor           


parse_cephalopod_numbers("DAY06\Trash_compactor.txt")
