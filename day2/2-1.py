import fileinput
import itertools

validCount = 0
expenseReportEntries = []

with fileinput.input(files=('input.txt')) as f:
    for line in f:
        splitLineArray = line.split()

        minMaxSubString = splitLineArray[0]
        hyphenPosition = minMaxSubString.find('-')
        minTimesToUseLetter = int(minMaxSubString[:hyphenPosition])
        maxTimesToUseLetter = int(minMaxSubString[hyphenPosition+1:])

        validationLetter = splitLineArray[1][0]
        password = splitLineArray[2]

        letterUsageCount = 0

        for letter in password:
            if letter == validationLetter:
                letterUsageCount += 1

        if minTimesToUseLetter <= letterUsageCount <= maxTimesToUseLetter:
            validCount += 1

    print(validCount)
