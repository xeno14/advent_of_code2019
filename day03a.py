
def generate_path(pos, d, n):
    dx, dy = {
        "R": (1, 0),
        "L": (-1, 0),
        "U": (0, 1),
        "D": (0, -1),
    }[d]
    for i in range(1, n+1):
        yield pos[0]+dx*i, pos[1]+dy*i


def parse(order):
    return order[0], int(order[1:])


assert parse("R12") == ("R", 12)
assert list(generate_path((0, 0), "R", 2)) == [(1, 0), (2, 0)]
assert list(generate_path((0, 0), "L", 2)) == [(-1, 0), (-2, 0)]
assert list(generate_path((0, 0), "U", 2)) == [(0, 1), (0, 2)]
assert list(generate_path((0, 0), "D", 2)) == [(0, -1), (0, -2)]


def solve(o1, o2):
    os = [o1, o2]
    visited = [set(), set()]
    for i in range(2):
        o = os[i]
        pos = (0, 0)
        orders = map(parse, o)
        for d, n in orders:
            for pos in generate_path(pos, d, n):
                visited[i].add(pos)
    intersections = visited[0].intersection(visited[1])
    # print(intersections)

    return min(map(lambda p: abs(p[0])+abs(p[1]), intersections))


def main():
    assert solve("R75,D30,R83,U83,L12,D49,R71,U7,L72".split(","), "U62,R66,U55,R34,D71,R55,D58,R83".split(",")) == 159
    assert solve("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(","), "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(",")) == 135

    with open("input/day3.txt") as f:
        s = f.read().strip()
    o1, o2 = s.split("\n")
    ans = solve(o1.split(","), o2.split(","))
    print(ans)


if __name__ == '__main__':
    main()
