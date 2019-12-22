import string
import itertools
from collections import deque


class Maze:

    @staticmethod
    def transpose(lines):
        n = len(lines)
        m = max(map(lambda l: len(l), lines))
        # print(n, m)
        res = [["" for i in range(n)] for _ in range(m)]
        for i in range(n):
            for j in range(m):
                if j < len(lines[i]):
                    val = lines[i][j]
                else:
                    val = " "
                # print(j, i)
                res[j][i] = val
        for i in range(len(res)):
            res[i] = "".join(res[i])
        return res

    def __init__(self, s: str):
        self.lines = s.split("\n")
        l = max(map(lambda x: len(x), self.lines))
        for i in range(len(self.lines)):
            if len(self.lines[i]) < l:
                self.lines[i] += " " * (l - len(self.lines[i]))
        self.tlines = self.transpose(self.lines)

    def find_portal(self, portal: str):
        res = []
        for i in range(len(self.lines)):
            line = self.lines[i]
            j = line.find(portal)
            if j >= 0:
                if j+2 < len(line) and line[j+2] == ".":
                    res.append((i, j+2))
                elif j-1 >= 0 and line[j-1] == ".":
                    res.append((i, j-1))
        # or transposed
        for i in range(len(self.tlines)):
            line = self.tlines[i]
            j = line.find(portal)
            if j >= 0:
                if j+2 < len(line) and line[j+2] == ".":
                    res.append((j+2, i))
                elif j-1 >= 0 and line[j-1] == ".":
                    res.append((j-1, i))
        return res

    def find_portals(self):
        res = {}
        for portal in itertools.product(string.ascii_uppercase, string.ascii_uppercase):
            portal = "".join(portal)
            pos = self.find_portal(portal)
            if len(pos) == 1:
                res[portal] = pos[0]
            if len(pos) == 2:
                pos1, pos2 = pos
                res[pos1] = pos2
                res[pos2] = pos1
        return res

    def solve(self):
        # BFS
        portals = self.find_portals()
        start = portals["AA"]
        goal = portals["ZZ"]
        q = deque([start + (1,)])
        visited = set()
        while q:
            x, y, d = q.popleft()
            if (x, y) == goal:
                return d-1
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx = x + dx
                ny = y + dy
                np = (nx, ny)
                # warp
                if np in portals:
                    print("warp", np, portals[np], d+1)
                    visited.add(np)
                    np = portals[np]
                    nx, ny = np
                    if np not in visited:
                        q.append((nx, ny, d+2))
                elif self.lines[nx][ny] == "." and np not in visited:
                    q.append((nx, ny, d + 1))


def main():
    maze = Maze("""         A           
         A           
  #######.#########  
  #######.........#  
  #######.#######.#  
  #######.#######.#  
  #######.#######.#  
  #####  B    ###.#  
BC...##  C    ###.#  
  ##.##       ###.#  
  ##...DE  F  ###.#  
  #####    G  ###.#  
  #########.#####.#  
DE..#######...###.#  
  #.#########.###.#  
FG..#########.....#  
  ###########.#####  
             Z       
             Z
""")
    # print("\n".join(maze.lines))
    # print("\n".join(maze.tlines))
    # print(maze.find_portal("BC"))
    print(maze.find_portals())
    print(maze.solve())

    print(Maze("""                   A               
                   A               
  #################.#############  
  #.#...#...................#.#.#  
  #.#.#.###.###.###.#########.#.#  
  #.#.#.......#...#.....#.#.#...#  
  #.#########.###.#####.#.#.###.#  
  #.............#.#.....#.......#  
  ###.###########.###.#####.#.#.#  
  #.....#        A   C    #.#.#.#  
  #######        S   P    #####.#  
  #.#...#                 #......VT
  #.#.#.#                 #.#####  
  #...#.#               YN....#.#  
  #.###.#                 #####.#  
DI....#.#                 #.....#  
  #####.#                 #.###.#  
ZZ......#               QG....#..AS
  ###.###                 #######  
JO..#.#.#                 #.....#  
  #.#.#.#                 ###.#.#  
  #...#..DI             BU....#..LF
  #####.#                 #.#####  
YN......#               VT..#....QG
  #.###.#                 #.###.#  
  #.#...#                 #.....#  
  ###.###    J L     J    #.#.###  
  #.....#    O F     P    #.#...#  
  #.###.#####.#.#####.#####.###.#  
  #...#.#.#...#.....#.....#.#...#  
  #.#####.###.###.#.#.#########.#  
  #...#.#.....#...#.#.#.#.....#.#  
  #.###.#####.###.###.#.#.#######  
  #.#.........#...#.............#  
  #########.###.###.#############  
           B   J   C               
           U   P   P     
""").solve())

    with open("input/20.txt") as f:
        maze = Maze(f.read())
    print(maze.solve())


if __name__ == '__main__':
    main()
