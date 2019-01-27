"""
Merge function for 2048 game.
"""
#This function does slideing and merging
def mergeUp(line):
    """
    Function that merges a single row or column in 2048.
    """
    count=0
    non=[]
    for colum in range(len(line[1])):
        for ind in range(len(line)):
            for ind2 in range(len(line)):
                for row in range(len(line)-1):

                    if line[row][colum] == 0 :
                        line[row][colum] = line[row+1][colum]
                        line[row+1][colum]=0
            if ind<1:
                for row in range(0,len(line)):
                        if line[row][colum] != 0:
                            non.append(line[row][colum])
            while count < len(line)-1:
                if line[count][colum] == line[count+1][colum]:
                    line[count][colum] += line[count+1][colum]
                    line[count+1][colum]=0

                count +=1
        count = 0
        if len(non)==2 and non[0]==non[1]:
            line[0][colum] = non[0]+non[1]
            line[1][colum] = 0
        non = []

    #return line
