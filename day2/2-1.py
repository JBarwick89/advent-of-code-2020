import fileinput

validCount = 0

with fileinput.input(files=('input.txt')) as f:
    for line in f:
        minMaxSubString, validationString, password = line.split()

        minTimesToUseLetter, maxTimesToUseLetter = (
            int(x) for x in minMaxSubString.split('-')
        )

        validationLetter = validationString[0]
        letterUsageCount = 0

        for letter in password:
            if letter == validationLetter:
                letterUsageCount += 1

        if minTimesToUseLetter <= letterUsageCount <= maxTimesToUseLetter:
            validCount += 1

    print(validCount)
