from day9 import interpret


SCAFFOLD = 1
ROBOT = 2


def parse_image(image):
    lines = image.strip().split("\n")
    scaffolds = []
    robo = (-100000, -100000)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == "#":
                scaffolds.append((x, y, SCAFFOLD))
            if c == "^":
                robo = (x, y)
    return scaffolds, robo


def add(p, q):
    return (p[0]+q[0], p[1]+q[1])


def find_path(image, pos):
    image = image.strip().split("\n")
    direc = (1, 0)
    width = len(image[0])
    height = len(image)
    res = ["R"]
    cnt = 0
    while True:
        next_pos = (pos[0]+direc[0], pos[1]+direc[1])
        nx, ny = next_pos
        if 0 <= nx < width and 0 <= ny < height and image[ny][nx] == "#":
            cnt += 1
            pos = next_pos
            continue
        # void
        left = (-direc[1], direc[0])
        next_pos = add(pos, left)
        nx, ny = next_pos
        if 0 <= nx < width and 0 <= ny < height and image[ny][nx] == "#":
            res.append(cnt)
            res.append("R")
            cnt = 1
            pos = next_pos
            direc = left
            continue
        right = (direc[1], -direc[0])
        next_pos = add(pos, right)
        nx, ny = next_pos
        if 0 <= nx < width and 0 <= ny < height and image[ny][nx] == "#":
            res.append(cnt)
            res.append("L")
            cnt = 1
            pos = next_pos
            direc = right
            continue
        res.append(cnt)
        break
    return res


def find_abc(path):
    n = len(path)
    possibles = []
    # assuming A, B ...
    for i in range(2, n, 2):
        a = path[:i]
        sa = "".join(map(str, a))
        for j in range(i+2, n, 2):
            b = path[i:j]
            sb = "".join(map(str, b))

            tmp = "".join(map(str, path))

            # to maximize replace
            if len(sa) > len(sb):
                tmp = tmp.replace(sa, "_").replace(sb, "_")
            else:
                tmp = tmp.replace(sb, "_").replace(sa, "_")

            # the rest can be replaced by a single string?
            pieces = [x for x in tmp.split("_") if x != ""]
            if len(pieces) == 0:
                continue
            sc = pieces[0]
            if all(map(lambda x: x==sc, pieces)):
                possibles.append([sa, sb, sc])

    # print out candidates
    s = "".join(map(str, path))
    print(s)
    for possible in possibles:
        print()
        for i in range(3):
            print(possible[i])


def find_main_routine(path, a, b, c):
    sa = "".join(map(str, a))
    sb = "".join(map(str, b))
    sc = "".join(map(str, c))
    idx = []
    tmp = "".join(map(str, path))
    for r, s in zip("ABC", [sa, sb, sc]):
        pos = 0
        while True:
            i = tmp[pos:].find(s)
            if i < 0:
                break
            idx.append((pos + i, r))
            pos += i + len(s)
        tmp = tmp.replace(s, "_" * len(s))
    idx = sorted(idx)
    return [x[1] for x in idx]


def encode(l):
    s = ",".join(map(str, l))
    return [ord(c) for c in s] + [10]


def main():
    with open("input/17.txt") as f:
        data = [int(x) for x in f.read().strip().split(",")]
    _, outputs = interpret(data)
    image = "".join([str(chr(code)) for code in outputs])
    _, robo = parse_image(image)
    path = find_path(image, robo)
    print(path)

    # hard code main routine for now... could filter inside the function
    # a, b, c = find_abc(path)
    a = ['R', 6, 'L', 10, 'R', 8]
    b = ['R', 8, 'R', 12, 'L', 8, 'L', 8]
    c = ['L', 10, 'R', 6, 'R', 6, 'L', 8]

    main_routine = find_main_routine(path, a, b, c)
    print(main_routine)

    data[0] = 2
    inputs = encode(main_routine) + encode(a) + encode(b) + encode(c) + encode(["n"])
    _, outputs = interpret(data, inputs=inputs)
    print(outputs)
    print(outputs[-1])


if __name__ == '__main__':
    main()