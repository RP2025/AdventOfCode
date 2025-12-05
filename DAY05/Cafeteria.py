import bisect

def parse(path):
    with open(path) as f:
        lines = [l.strip() for l in f]

    i = lines.index("")
    ranges = [list(map(int, r.split("-"))) for r in lines[:i]]
    ids    = [int(x) for x in lines[i+1:] if x]

    return ranges, ids


def merge_ranges(ranges):
    ranges.sort()
    merged = []
    for a, b in ranges:
        if not merged or a > merged[-1][1] + 1:
            merged.append([a, b])
        else:
            merged[-1][1] = max(merged[-1][1], b)
    return merged


def count_fresh_ids(ranges, ids):
    merged = merge_ranges(ranges)

    fresh = 0
    for x in ids:
        i = bisect.bisect_right(merged, [x, 10**18]) - 1
        if i >= 0 and merged[i][0] <= x <= merged[i][1]:
            fresh += 1
    return fresh


def count_total_fresh(ranges):
    merged = merge_ranges(ranges)
    return sum(b - a + 1 for a, b in merged)


def solve(path):
    ranges, ids = parse(path)
    part1 = count_fresh_ids(ranges, ids)
    part2 = count_total_fresh(ranges)
    return part1, part2


print(solve("DAY05\cafeteria.txt"))