from collections import defaultdict

def load_grid(path):
    rows = [line.rstrip("\n") for line in open(path) if line.strip()]
    width = max(map(len, rows))
    return [row.ljust(width, '.') for row in rows]

def locate_source(grid):
    for r, row in enumerate(grid):
        c = row.find("S")
        if c >= 0:
            return r, c
    raise RuntimeError("Source 'S' not found.")

def simulate_classical(grid):
    sr, sc = locate_source(grid)
    beams = {sc}
    split_count = 0

    for row in grid[sr+1:]:
        next_beams = set()
        for col in beams:
            if row[col] == '^':   
                split_count += 1
                next_beams.update([col - 1, col + 1])
            else:               
                next_beams.add(col)
        beams = {c for c in next_beams if 0 <= c < len(row)}
        if not beams:
            break

    return split_count

def simulate_quantum(grid):
    sr, sc = locate_source(grid)
    timelines = defaultdict(int)
    timelines[sc] = 1

    for row in grid[sr+1:]:
        next_t = defaultdict(int)
        for col, count in timelines.items():
            if row[col] == '^':     
                next_t[col - 1] += count
                next_t[col + 1] += count
            else:                  
                next_t[col] += count

        timelines = defaultdict(int,
            {c: n for c, n in next_t.items() if 0 <= c < len(row)}
        )

        if not timelines:
            break

    return sum(timelines.values())


grid = load_grid("DAY07\laboratories.txt")

print("Part 1 — Classical splits   :", simulate_classical(grid))
print("Part 2 — Quantum timelines :", simulate_quantum(grid))
