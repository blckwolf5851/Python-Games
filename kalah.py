#initial houses and store
num = [4,4,4,4,4,4]
store=[0]
init = num+store
step = 0
print(init)

while True:
    ind = int(input("Pick Index: "))
    inp = init[ind]
    step += 1
    #chosen index = 0
    init[ind] = 0
    for i in range(inp):
        print(i)
        #skip illegal moves
        if ind+inp != len(init):
            print('Not a legal move')
            continue
        #each index after chosen index +=1
        if ind+i+1 <= (len(init)-1):
            init[ind+1+i] += 1
        #once exceed index length, go reverse
        if (ind+i+1) > (len(init)-1):
            init[-(i+1)]+=1
            # if reversed index exceed index length
            if (-(inp-i)-1) < (-len(init)):
                init[(-len(init))-(-(inp-i)-1)+1] += 1
    print(init)
    #when houses are all 0, win
    if init[0] = 0 and init[1] = 0 and init [2] = 0 and init[3] = 0 and init[4] = 0 and init[5] = 0:
        print('You Win. Step =', step, 'Final result =', init[6] )
        break
