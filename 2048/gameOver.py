def gameOver(line):
    failCount = 0
    for row in range(len(line)):
        for colum in range(len(line[1])-1):
            if line[row][colum] != line[row][colum+1] and 0 not in line[row]:
                failCount +=1
    for colum in range(len(line[1])):
        for row in range(len(line)-1):
            if line[row][colum] != line[row+1][colum] and 0 not in line[row]:
                failCount+=1
    if failCount == (len(line)*(len(line[1])-1)+(len(line)-1)*len(line[1])): # total number of rows all have no 0 and doesn't equal to each other, game over
        return 1
    else:
        return 0
print(gameOver([[2,8,4,2],[4,16,32,4],[16,32,128,32],[128,512,256,64]]))
