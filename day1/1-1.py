import fileinput
import itertools

expenseReportEntries = []

with fileinput.input(files=('input.txt')) as f:
    for line in f:
        expenseReportEntries.append(int(line.rstrip()))

for combo in itertools.combinations(expenseReportEntries, 2):
    firstItem = combo[0]
    secondItem = combo[1]

    if firstItem + secondItem == 2020:
        print(firstItem * secondItem)
        break
