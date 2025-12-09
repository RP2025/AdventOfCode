from itertools import combinations
from shapely.geometry import Polygon, box
from shapely.prepared import prep


def parse_points(path: str):
    with open(path) as f:
        return [tuple(map(int, line.strip().split(','))) for line in f if line.strip()]


def rectangle_area(a: tuple[int, int], b: tuple[int, int]) -> int:
    width = abs(a[0] - b[0]) + 1
    height = abs(a[1] - b[1]) + 1
    return width * height


def part1(points):
    max_area = 0
    for a, b in combinations(points, 2):
        max_area = max(max_area, rectangle_area(a, b))
    return max_area


def part2(points):
    polygon = Polygon(points)  # red loop polygon
    prepared = prep(polygon)

    max_area = 0
    for a, b in combinations(points, 2):
        rect = box(
            min(a[0], b[0]),
            min(a[1], b[1]),
            max(a[0], b[0]),
            max(a[1], b[1])
        )

        if prepared.contains(rect):
            max_area = max(max_area, rectangle_area(a, b))

    return max_area


def Movie_theater(path):
    points = parse_points(path)
    print("Part 1:", part1(points))
    print("Part 2:", part2(points))


Movie_theater("DAY09/Movie.txt")
