"""
MergeDown function for 2048 game.
"""
def mergeDown(line):
    count=1
    non=[]
    #avoid mutation of input list
    #for ind in range(len(line)):
    #    line.append(line[ind])

    for colum in range(len(line[1])): # in sliding up/down colum is the least frequent check target
        for ind in range(len(line)): # iterate a few times to check for the 0 being made by slide and merge
            '''SLIDE LOOP'''
            for ind2 in range(len(line)):
                for row in range(1,len(line)): # in sliding up/down row is the high frequent check target
                    if line[-row][colum] == 0 : # for each negative index check for the next negative index by -1
                        line[-row][colum] = line[-row-1][colum] # replace the current index value with next index value if the current index value is 0
                        line[-row-1][colum]=0 # make the next index 0 so it can iterate again, and keep sliding
                '''MERGE LOOP'''
            if ind<1:
                for row in range(1,len(line)+1):
                        if line[-row][colum] != 0:
                            non.append(line[-row][colum])
            while count < len(line): # loop to merge number that have the same value

                if line[-count][colum] == line[-count-1][colum]:
                    line[-count][colum] += line[-count-1][colum]
                    line[-count-1][colum]=0 # make the merged target be 0, slide loop will slide again

                count +=1 # update global variable
        count = 1 # reset global value after each merge act in a colum
        if len(non)==2 and non[0]==non[1]:

            line[-1][colum] = non[0]+non[1]
            line[-2][colum] = 0
        non = []

    #return line
