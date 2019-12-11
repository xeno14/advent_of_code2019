from day11a import Brain, Robot


def main():
    with open("./input/day11.txt") as f:
        data = [int(x) for x in f.read().strip().split(",")]
    print(len(data))

    robot = Robot()
    brain = Brain(data)

    color = 1
    while True:
        (c, rot), halt = brain.interpret(color)
        if halt:
            break
        print(c, rot)
        color = robot.next_step(c, rot)
    robot.visualize()


if __name__ == '__main__':
    main()