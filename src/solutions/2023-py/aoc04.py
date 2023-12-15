# =============================================================================
# Ruth Wertz
# AOC 2023 - Day 4
# https://github.com/HumbleUnicorn/Advent-of-Code/blob/main/src/solutions/2023-py/aoc04.py
# =============================================================================


# =============================================================================
# Part 1 Outline
# 
# function to read Cards
#     parse to [str1],[str2] per line (card no. not retained)
#     regex: parse to [list1],[list2] per line
# 
# function to find winning numbers
#    Counter: wins = list1 & list2
#    score = 1*2**n; n = len of wins
#    sum scores
#  
# Part 2 Outline
#
# winDict with {card no: no of winning numbers on card}
# copyDict with {card no: no of copies (starts at 1)}
# function to track copies
#     for each key in winDict
#         access number of wins from winDict --> (range) 
#         access number of copies from copyDict ---> (multiplier, m)
#         for card in range, increase copies by "m"
#     sum copyDict values
# =============================================================================


# =============================================================================
#  //INPUT DATA//
# =============================================================================

test4=[]
with open('inputs/t04.txt') as f: 
    for lines in f:
        test4.append(lines) 
      

day4=[]
with open('inputs/d04.txt') as f: 
    for lines in f:
        day4.append(lines)         


# =============================================================================
#  // DEFINE FUNCTIONS // 
# =============================================================================

import re

from collections import Counter

def readCards(dataSet):
    rC=[]
    for lines in dataSet:
        lines = lines.replace("\n","")
        lines = lines.replace(":", ",")
        lines = lines.replace("|", ",")
        lines = lines.split(",")
        lines.pop(0)
        win=[]
        own=[]
        win_matches = re.finditer(r'\d+', lines[0])
        own_matches = re.finditer(r'\d+', lines[1])
        for match in win_matches:
            win.append(match.group())
        for match in own_matches:
            own.append(match.group())
        rC.append([win,own])
    return(rC)
        
def findWins(cards):
    fW = []
    for i in range(len(cards)):
        line = cards[i]
        wins = Counter(line[0]) & Counter(line[1])
        if wins:
            m = i+1 #card number  
            n = len(wins)  
            score = 2**(n-1) 
            fW.append([m,n,score])
        else:
            m = i+1 #card number
            n = 0
            score = 0
            fW.append([m,n,score])
    return(fW)

def sumWins(wins):
    score = []
    for line in wins: 
        score.append(line[2])
    return(sum(score))

def winLib(wins):
    wL = {}
    for lines in wins:
        w = {lines[0]:lines[1]}
        wL.update(w)
    return(wL)

def cardLib(wLib):
    k = wLib.keys() 
    cL = dict.fromkeys(k,1)
    return(cL)

def copyCard(wLib,cLib):
    keys = wLib.keys()      #list of card nos.
    for k in keys:          #k = card no to process
        w = wLib.get(k)     #w = no of winning nos on card
        m = cLib.get(k)     #m = no of copies (default = 1)
        r = list(range(k+1,k+1+w))
        for c in r:         #c = card no to be copy
            cLib[c] += m    #increase value of card c by m
    return(cLib)
            
   
# =============================================================================
#  // TEST OUTPUT //
# =============================================================================

rCard = readCards(test4)
for lines in rCard:
    print(lines)    

fWin = findWins(rCard)
for lines in fWin:
    print(lines)

wLib = winLib(fWin)
print(wLib)

cLib = cardLib(wLib)
print(cLib)

cCard = copyCard(wLib,cLib)
print(cCard)

scoreSum = sumWins(fWin)

cardSum = sum(cCard.values())

print(f'Test1 = {scoreSum} and Test2 = {cardSum}')

# =============================================================================
#   // PUZZLE OUTPUT //
# =============================================================================

rCard = readCards(day4)  

fWin = findWins(rCard)

wLib = winLib(fWin)

cLib = cardLib(wLib)

cCard = copyCard(wLib,cLib)

scoreSum = sumWins(fWin)

cardSum = sum(cCard.values())
    
print(f'Part 1: The Elfs cards are worth {scoreSum} points')

print(f'Part 2: The Elf will have a total of {cardSum} cards')