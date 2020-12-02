import fileinput

validCount = 0

with fileinput.input(files=('input.txt')) as f:
    for line in f:
        postionSubString, validationString, password = line.split()
        validationLetter = validationString[0]

        firstLetterToCheck, secondLetterToCheck = (
            password[int(x) - 1] for x in postionSubString.split('-')
        )

        if (firstLetterToCheck == validationLetter) != (secondLetterToCheck == validationLetter):
            validCount += 1

    print(validCount)
