from collections import defaultdict

def parse_input(lines):
    graph = defaultdict(list)
    for line in lines:
        if not line.strip():
            continue
        left, right = line.split(":")
        src = left.strip()
        dests = right.strip().split()
        graph[src].extend(dests)
    return graph


# Count paths using memoized DFS (no enumeration)
def count_paths(graph, start, end, memo=None):
    if memo is None:
        memo = {}

    if start == end:
        return 1
    if start in memo:
        return memo[start]

    total = 0
    for nxt in graph[start]:
        total += count_paths(graph, nxt, end, memo)

    memo[start] = total
    return total


def main():
    with open("reactor.txt", "r") as f:
        lines = f.readlines()

    graph = parse_input(lines)

    # ---------- PART 1 ----------
    part1 = count_paths(graph, "you", "out")
    print("Part 1: Paths from 'you' to 'out' =", part1)

    # ---------- PART 2 ----------
    # Needed path segments:
    a = count_paths(graph, "svr", "dac")
    b = count_paths(graph, "dac", "fft")
    c = count_paths(graph, "fft", "out")

    d = count_paths(graph, "svr", "fft")
    e = count_paths(graph, "fft", "dac")
    f = count_paths(graph, "dac", "out")

    # Two allowed orders:
    total_valid = a * b * c + d * e * f

    print("Part 2: Paths from 'svr' to 'out' containing BOTH 'dac' and 'fft' =", total_valid)


if __name__ == "__main__":
    main()
