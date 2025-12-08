import itertools

class UnionFind:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.sizes = [1] * n
        self.subgraphs = n

    def find(self, i: int):
        while i != self.parents[i]:
            self.parents[i] = self.parents[self.parents[i]]
            i = self.parents[i]
        return i

    def union(self, a: int, b: int):
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False

        self.subgraphs -= 1
        if self.sizes[pa] < self.sizes[pb]:
            self.parents[pa] = pb
            self.sizes[pb] += self.sizes[pa]
        else:
            self.parents[pb] = pa
            self.sizes[pa] += self.sizes[pb]
        return True


def load_points(filename: str):
    with open(filename, 'r') as f:
        return [tuple(map(int, line.split(','))) for line in f]


def distance_sq(p1, p2):
    return sum((a - b) ** 2 for a, b in zip(p1, p2))


def sorted_pairs(points):
    return sorted(
        itertools.combinations(range(len(points)), 2),
        key=lambda p: distance_sq(points[p[0]], points[p[1]])
    )


def solve(filename: str):
    points = load_points(filename)
    n = len(points)

    pairs = sorted_pairs(points)
    uf = UnionFind(n)

    part1_answer = None
    part2_answer = None

    for idx, (a, b) in enumerate(pairs):

        uf.union(a, b)

        if idx == 999: 
            sizes = sorted(uf.sizes, reverse=True)
            part1_answer = sizes[0] * sizes[1] * sizes[2]

        if uf.subgraphs == 1 and part2_answer is None:
            x1 = points[a][0]
            x2 = points[b][0]
            part2_answer = x1 * x2
            if part1_answer is not None:
                break

    return part1_answer, part2_answer



filename = "DAY08/playground.txt"

part1, part2 = solve(filename)
print("Part 1:", part1)
print("Part 2:", part2)
