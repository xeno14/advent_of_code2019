from day9 import next_step, visualize, build_unbound_data
import numpy as np


BLACK = 0
WHITE = 1


class Brain:

    def __init__(self, data):
        self.data = build_unbound_data(data)
        self.pos = 0
        self.rb = 0

    def interpret(self, i):
        outputs = []
        while self.pos != -1:
            self.pos, self.rb, self.data, o = next_step(self.pos, self.rb, self.data, iter([i]))
            if self.pos == -1:
                return [None, None], True
            if o is not None:
                outputs.append(o)
            if len(outputs) == 2:
                break
        return outputs, self.pos == -1


class Robot:

    def __init__(self):
        self.pos = (0, 0)
        self.d = (0, 1)
        self.space = dict()

    def next_step(self, color, rot):
        # change color
        self.space[self.pos] = color

        # rotation
        if rot == 0:
            self.d = (-self.d[1], self.d[0])
        else:
            self.d = (self.d[1], -self.d[0])

        # move forward
        self.pos = (self.pos[0]+self.d[0], self.pos[1]+self.d[1])
        print(self.pos, self.d)

        return self.space.get(self.pos, BLACK)

    def count(self):
        return len(self.space)

    def visualize(self):
        minx = min(map(lambda x: x[0], self.space.keys()))
        miny = min(map(lambda x: x[1], self.space.keys()))
        maxx = max(map(lambda x: x[0], self.space.keys()))
        maxy = max(map(lambda x: x[1], self.space.keys()))
        space = np.zeros((maxx-minx+1, maxy-miny+1)).astype(int)
        for p, c in self.space.items():
            x = p[0] - minx
            y = p[1] - miny
            space[x, y] = c
        space = space[:, ::-1]  # invert y
        for y in range(space.shape[1]):
            s = "".join(map(lambda c: " " if c==0 else "*", space[:, y]))
            print(s)


def test():
    robot = Robot()
    c = robot.next_step(1, 0)
    print(c)
    c = robot.next_step(0, 0)
    print(c)
    c = robot.next_step(1, 0)
    print(c)
    c = robot.next_step(1, 0)
    print(c)
    c = robot.next_step(0, 1)
    print(c)
    c = robot.next_step(1, 0)
    print(c)
    c = robot.next_step(1, 0)
    print(c)
    robot.visualize()
    print(robot.count())


def main():
    test()

    with open("./input/day11.txt") as f:
        data = [int(x) for x in f.read().strip().split(",")]
    print(len(data))

    robot = Robot()
    brain = Brain(data)

    color = 0
    while True:
        (c, rot), halt = brain.interpret(color)
        if halt:
            break
        print(c, rot)
        color = robot.next_step(c, rot)
    print(robot.count())


if __name__ == '__main__':
    main()