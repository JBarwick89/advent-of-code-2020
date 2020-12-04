import fileinput

with fileinput.input(files=('input.txt')) as f:
    xPos = 0
    treeCount = 0

    for line in f:
        if line[xPos] == '#':
            treeCount += 1

        if xPos >= 28:
            xPos = xPos - 28
        else:
            xPos += 3

    print(treeCount)
