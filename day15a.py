from day9 import *
from util import *

from collections import deque


class Robot:

    def __init__(self, data=None):
        if data is None:
            data = []
        self.data = build_unbound_data(data)
        self.pos = 0
        self.rb = 0

    def interpret(self, i):
        while self.pos != -1:
            self.pos, self.rb, self.data, o = next_step(self.pos, self.rb, self.data, iter([i]))
            # visualize(self.pos, self.rb, self.data)
            if self.pos == -1:
                return None
            if o is not None:
                return o

    def clone(self) -> "Robot":
        r = Robot()
        r.data = self.data.copy()
        r.pos = self.pos
        r.rb = self.rb
        return r


def next_pos(pos, i):
    x, y = pos
    if i==1:  # north
        return x, y+1
    if i==2:  # south
        return x, y-1
    if i==3:  # west
        return x-1, y
    if i==4:  # east
        return x+1, y


INIT = -1
WALL = 0
VOID = 1
OXYGEN = 2


def solve(data):
    q = deque([])
    q.append(
        ((0, 0), Robot(data), 0)
    )
    visited = {
        (0, 0): INIT
    }
    min_dist = {
        (0, 0): 0
    }
    res = -1
    while res < 0:
        pos, robot, d = q.popleft()
        for i in range(1, 5):
            pos2 = next_pos(pos, i)
            if pos2 in visited:
                continue
            robot2: Robot = robot.clone()
            d2 = d + 1

            o = robot2.interpret(i)
            visited[pos2] = o
            if o == WALL:
                continue
            min_dist[pos2] = d2
            if o == OXYGEN:
                res = d2
            else:
                q.append((pos2, robot2, d2))
        draw_stage(visited, {INIT: "_", WALL: "#", VOID: " ", OXYGEN: "X", -2: "?", -3: "@"}, init=-2, override={pos: -3}, reverse=True)
    return res


def main():
    with open("./input/day15.txt") as f:
        data = [int(x) for x in f.read().split(",")]
    print(solve(data))


if __name__ == '__main__':
    main()