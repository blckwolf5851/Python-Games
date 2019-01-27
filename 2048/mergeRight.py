"""
Merge function for 2048 game.
"""

#This function does slideing and merging
def mergeRight(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code

    count=1
    for row in range(len(line)):
        for ind in range(len(line[row])):
            for colum in range(1,len(line[row])):
                if line[row][-colum] == 0 :
                    line[row][-colum] = line[row][-colum-1]
                    line[row][-colum-1] = 0


        while count < len(line[row]):
            if line[row][-count] == line[row][-count-1]:
                line[row][-count] += line[row][-count-1]
                line[row].pop(-count-1)
                line[row].insert(0,0)

            count +=1
        count = 1
    #return line
