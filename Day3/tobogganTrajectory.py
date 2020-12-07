from timeit import default_timer as timer
from functools import reduce

if __name__ == '__main__':
    geology = dict()
    width = 0
    with open('tobogganTrajectoryInput') as f:
        for i, line in enumerate(f):
            width = len(line.strip())
            geology[i] = line.strip()

    print("Part 1")
    start = timer()
    trees = 0
    for key in geology:
        value = geology[key]
        if value[(key * 3) % width] == '#':
            trees += 1
    print("Number of trees:", trees)
    end = timer()
    print("Time taken: ", end - start, "\n\n")

    print("Part 2")
    start = timer()
    # trees encountered on each slope
    trees = [0, 0, 0, 0, 0]
    h_motion = [1, 3, 5, 7, 1]
    v_motion = [1, 1, 1, 1, 2]
    hPos = [0, 0, 0, 0, 0]
    for key in geology:
        value = geology[key]
        for i, (h, v) in enumerate(zip(h_motion, v_motion)):
            if key % v == 0:
                if value[hPos[i]] == '#':
                    trees[i] += 1
                hPos[i] += h_motion[i]
                hPos[i] %= width
    print("Number of trees:", trees, " multiplied: ", reduce(lambda x, y: x * y, trees))
    end = timer()
    print("Time taken: ", end - start, "\n\n")
