import numpy as np


def draw_stage(posd: dict, draw, init=0, override=None, reverse=False):
    if type(draw) == dict:
        drawd = draw.copy()
        draw = lambda x: drawd[x]
    xmin = min([p[0] for p in posd])
    ymin = min([p[1] for p in posd])
    xmax = max([p[0] for p in posd])
    ymax = max([p[1] for p in posd])
    stage = np.zeros((xmax+1-xmin, ymax+1-ymin), dtype=int)
    stage[:, :] = init
    for pos, val in posd.items():
        stage[pos[0]-xmin, pos[1]-ymin] = val
    if override:
        for pos, val in override.items():
            stage[pos[0] - xmin, pos[1] - ymin] = val
    lines = []
    for y in range(stage.shape[1]):
        lines.append("".join([draw(stage[x, y]) for x in range(stage.shape[0])]))

    if reverse:
        lines = lines[::-1]
    for line in lines:
        print(line)


def _test():
    draw_stage({(0, 0): -1, (0, 1): 0, (0, -1): 0, (-1, 0): 0, (1, 0): 1}, {-1: "@", 0: "#", 1: "."})


if __name__ == '__main__':
    _test()