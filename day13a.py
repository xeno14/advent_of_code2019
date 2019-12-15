from day9 import *


def stage(outputs):
    return [(outputs[i], outputs[i+1], outputs[i+2]) for i in range(0, len(outputs), 3)]


def main():
    with open("input/day13.txt") as f:
        data = [int(x) for x in f.read().strip().split(",")]
    _, outputs = interpret(data)

    tiles = stage(outputs)
    print(tiles)

    print(len([t for t in tiles if t[2] == 2]))


if __name__ == '__main__':
    main()