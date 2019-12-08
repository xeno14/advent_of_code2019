from day5 import *
from day07a import amp_simulate

from itertools import permutations, cycle, chain


class Amp:

    def __init__(self, data, phase):
        self.data = list(data)
        self.pos = 0
        self.input = iter([phase])

    def interpret(self, i):
        self.input = chain(self.input, [i])
        outputs = []
        while self.pos != -1:
            self.pos, self.data, o = next_step(self.pos, self.data, self.input)
            if o is not None:
                outputs.append(o)
                break
        return outputs, self.pos == -1


def amp_feedback_simulate(data: list, phase: list):
    amps = [Amp(data, p) for p in phase]
    o = 0
    for i in cycle(range(len(amps))):
        # print("-"*10, i, "-"*10)
        outputs, halt = amps[i].interpret(o)
        if halt:
            return o
        o = outputs[-1]


def solve(data):
    phases = permutations([5,6,7,8,9])
    thrusts = [amp_feedback_simulate(data, phase) for phase in phases]
    thrusts = sorted(thrusts, reverse=True)
    print(thrusts)
    return thrusts[0]


def main():
    with open("./input/day7.txt") as f:
        data = [int(x) for x in f.read().split(",")]

    assert solve([3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26,
                                  27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]) == 139629729
    assert solve([3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
                                  -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
                                  53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10]) == 18216

    print(solve(data))


if __name__ == '__main__':
    main()
