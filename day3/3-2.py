import fileinput


def countTrees(x, y):
    with fileinput.input(files=('input.txt')) as f:
        xPos = 0
        treeCount = 0
        lineLength = 31

        for i, line in enumerate(f):
            if i % y != 0:
                continue

            if line[xPos] == '#':
                treeCount += 1

            if xPos >= lineLength - x:
                xPos = xPos - lineLength + x
            else:
                xPos += x

        return treeCount


print(
    countTrees(1, 1) * countTrees(3, 1) * countTrees(5, 1)
    * countTrees(7, 1) * countTrees(1, 2)
)
