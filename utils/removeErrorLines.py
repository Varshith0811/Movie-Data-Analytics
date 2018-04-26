import fileinput

listOfLineNums = []

with open('../data/errorLines.txt', 'r') as errorLines:
    for line in errorLines:

        string = line.replace(':', '')
        listOfStrings = string.split(' ')

        for index, item in enumerate(listOfStrings):
            if item == 'line':
                listOfLineNums.append(listOfStrings[index+1])

print(len(listOfLineNums)) #result was 429


oldFile = open('../data/imdb.csv', 'r')
oldLines = oldFile.readlines()
oldFile.close()

indexOfBadLines = 0
numberOfNonFloats = 0
numberOfBlanks = 0

newFile = open('../data/imdb.csv', 'w')

for index, line in enumerate(oldLines):
    #print(listOfLineNums[indexOfBadLines])
    currentLineArray = line.split(',')
    if index == int(listOfLineNums[indexOfBadLines]):
        if int(listOfLineNums[indexOfBadLines]) < 14688:
            indexOfBadLines += 1
    elif '\\' in line:
        line = line.replace('\\', '')
        #newFile.write(line)
        numberOfNonFloats += 1
    elif currentLineArray[0] == '' or currentLineArray[1] == '' or currentLineArray[2] == '':
        numberOfBlanks += 1
    else:
        newFile.write(line)
print('Error reported lines : ' + str(indexOfBadLines))
print('Non-Float detected: ' + str(numberOfNonFloats))
print('Blanks: ' + str(numberOfBlanks))
print('Total: ' + str(indexOfBadLines + numberOfNonFloats + numberOfBlanks))
newFile.close()
