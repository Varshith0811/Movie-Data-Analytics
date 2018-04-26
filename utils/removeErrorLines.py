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

newFile = open('../data/newFile.csv', 'w')

for index, line in enumerate(oldLines):
    #print(listOfLineNums[indexOfBadLines])
    if index == int(listOfLineNums[indexOfBadLines]):
        print(indexOfBadLines)
        if int(listOfLineNums[indexOfBadLines]) < 14688:
            indexOfBadLines += 1
    else:
        newFile.write(line)
newFile.close()

# for n in listOfLineNums:
#     for line in fileinput.input('../data/imdb.csv', inplace=True):
#         if fileinput.lineno() == n:
#             continue
#             print(line, end='')


# def removeLine(n, f):
#     d = f.readlines()
#     f.seek(0)
#     for i in range(len(d)):
#         f.write(d[i])
#     f.truncate()
#
# f = open('../data/imdb.csv',"r+")
# for lineToRemove in listOfLineNums:
#     removeLine(lineToRemove, f)
# f.close()
