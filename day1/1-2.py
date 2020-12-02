import fileinput
import itertools

expenseReportEntries = []

with fileinput.input(files=('input.txt')) as f:
    for line in f:
        expenseReportEntries.append(int(line.rstrip()))

for combo in itertools.combinations(expenseReportEntries, 3):
    firstItem = combo[0]
    secondItem = combo[1]
    thirdItem = combo[2]

    if firstItem + secondItem + thirdItem == 2020:
        print(firstItem * secondItem * thirdItem)
        break
