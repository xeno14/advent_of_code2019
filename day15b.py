from day15a import *
from util import *

from collections import deque


WALL = 0
VOID = 1
OXYGEN = 2


def search_space(data):
    q = deque([])
    q.append(
        ((0, 0), Robot(data))
    )
    visited = {
        (0, 0): VOID
    }
    oxpos = None
    while len(q):
        pos, robot = q.popleft()
        for i in range(1, 5):
            pos2 = next_pos(pos, i)
            if pos2 in visited:
                continue
            robot2: Robot = robot.clone()
            o = robot2.interpret(i)
            visited[pos2] = o
            if o == WALL:
                continue
            if o == OXYGEN:
                oxpos = pos2
            q.append((pos2, robot2))
    return oxpos, visited


def fill_oxygen(oxpos, space):
    q = deque([(oxpos, 0)])
    min_dist = {oxpos: 0}

    cnt = 0
    while q:
        pos, d = q.popleft()

        for i in range(1, 5):
            pos2 = next_pos(pos, i)
            if pos2 not in space:
                continue
            d2 = d + 1
            o = space[pos2]
            if o == VOID:
                space[pos2] = OXYGEN
                min_dist[pos2] = d2
                cnt = max(cnt, d2)
                q.append((pos2, d2))
        # print(min_dist)
        # draw_stage(space, {INIT: "_", WALL: "#", VOID: " ", OXYGEN: "o", -3: "@"}, reverse=True)
    return cnt

 ##
#..##
#.#..#
#.O.#
 ###
SPACE0 = {
    (1, 0): WALL, (2, 0): WALL, (3, 0): WALL,
    (0, 1): WALL, (1, 1): VOID, (2, 1): OXYGEN, (3, 1): VOID, (4,1): WALL,
    (0, 2): WALL, (1, 2): VOID, (2, 2): WALL, (3, 2): VOID, (4, 2): VOID, (5, 2): WALL,
    (0, 3): WALL, (1, 3): VOID, (2, 3): VOID, (3, 3): WALL, (4, 3): WALL, (5, 3): WALL,
    (0, 4): WALL, (1, 4): WALL,
}

def main():
    assert fill_oxygen((2, 1), SPACE0) == 4
    with open("./input/day15.txt") as f:
        data = [int(x) for x in f.read().split(",")]
    oxpos, space = search_space(data)
    ans = fill_oxygen(oxpos, space)
    print(ans)


if __name__ == '__main__':
    main()