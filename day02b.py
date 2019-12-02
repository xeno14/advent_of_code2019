from day02a import interpret


def run(noun, verb, memory):
    data = list(memory)  # copy
    data[1] = noun
    data[2] = verb
    data = interpret(data)
    return data[0]


def main():
    with open("./input/day2.txt") as f:
        memory = [int(x) for x in f.read().split(",")]
    assert run(12, 2, memory) == 7594646

    print("loaded %d integers" % len(memory))
    for noun in range(100):
        for verb in range(100):
            x = run(noun, verb, memory)
            if x == 19690720:
                print(noun, verb, 100 * noun + verb)
                return
    print("not found :(")


if __name__ == '__main__':
    main()



