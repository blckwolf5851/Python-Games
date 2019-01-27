from random import *
lev2 = []
negPos = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
ram = sample(nums,  1)   # Pick a random item from the list
ram1= ram[0]
mini = 1
maxi = 20
count =0
#ind = nums.index(ram1)

while True:
    inp = input('Guess a number: ')
    raw = int(inp)
    ind = nums.index(raw)
    guess = nums[ind]
    if guess <mini or guess > maxi:
        print('Plz print the number from', mini, 'to', maxi)
        continue
    if guess != ram1:
        lev2.append(guess)
    if guess < ram1:
        mini = guess + 1
        print('Guess higher than', mini)
        count=count+1
    elif guess > ram1:
        maxi = guess - 1
        count=count+1
        print('Guess lower than', maxi)
    elif guess == ram1:
        print('U failed dodging the numbers:', ram1)
        break
print('Numbers that u guessed:', lev2)


print('Welcome to level 2:) guessed number is now in random order')
shuffle(lev2)
