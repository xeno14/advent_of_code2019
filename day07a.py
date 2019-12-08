from day5 import interpret

from itertools import permutations


def amp_simulate(data: list, phase: list, a_in=0):
    o = a_in
    for p in phase:
        _, outputs = interpret(list(data), inputs=[p, o])
        o = outputs[0]
    return o


def solve(data, n=5):
    phases = permutations(range(n))
    return max(map(lambda phase: amp_simulate(data, phase), phases))


def main():
    with open("./input/day7.txt") as f:
        data = [int(x) for x in f.read().split(",")]

    assert solve([3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]) == 43210
    assert solve([3,23,3,24,1002,24,10,24,1002,23,-1,23, 101,5,23,23,1,24,23,23,4,23,99,0,0]) == 54321
    assert solve([3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]) == 65210
    print(solve(data, 5))


if __name__ == '__main__':
    main()
