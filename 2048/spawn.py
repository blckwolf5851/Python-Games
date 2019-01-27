import random
def spawn(line):
    num = random.randrange(2,5,2) #pick a random number to display (either 2 or 4)
    zeroIndex = [] #all the indexs that is has value of zero, later chose from those 0 index to put new value
    for row in range(len(line)): # append lists of indexs to zeroIndex
        for colum in range(len(line[row])):
            if line[row][colum] == 0:
                zeroIndex.append([row,colum])
    if len(zeroIndex>0):
        for i in range(1,2): # pick random index from zeroIndex
            randomIndex = random.randrange(0,len(zeroIndex))
            pickIndex = zeroIndex[randomIndex]
            row = pickIndex[0]
            colum = pickIndex[1]
            line[row][colum] = num
    zeroIndex = [] # reset zeroIndex
    #return line
