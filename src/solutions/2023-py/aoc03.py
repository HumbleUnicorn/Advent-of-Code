# =============================================================================
# Ruth Wertz
# AOC 2023 - Day 3
# https://github.com/HumbleUnicorn/Advent-of-Code/blob/main/src/solutions/2023-py/aoc03.py
# =============================================================================


# =============================================================================
# Part 1 Outline
# 
# fuction to define number range and value - regex
#    return [x1, x2, y1, y2, int]
# 
# function to define symbol range - regex
#    return [x1, x2, y1, y2, sym]
# 
# function to check if num is in  symbol range - Counter
#    return [sum]
#
# Part 2 Outline
# 
# update function to check if num is in range
#    return [line], then sum
# 
# function to check if sym in range of exactly two num - Counter
#    return [num1, num2, product], then sum products
#
# =============================================================================


# =============================================================================
#  //INPUT DATA//
# =============================================================================

test3=[]
with open('inputs/t03.txt') as f: 
    for lines in f:
        lines = lines.replace("\n","")
        test3.append(lines) 
        

day3=[]
with open('inputs/d03.txt') as f: 
    for lines in f:
        lines = lines.replace("\n","")
        day3.append(lines)         


# =============================================================================
#  // DEFINE FUNCTIONS // 
# =============================================================================

import re

from collections import Counter

def findDigits(dataSet):
    dL=[]
    i = -1
    for lines in dataSet:
        i+=1
        matches = re.finditer(r'\d+', lines)
        for match in matches:
            num = int(match.group())
            x1 = match.start()
            x2 = match.end()  
            y = i
            dL.append([list(range(x1,x2)),[y],num])
    return(dL)

def findSymbols(dataSet):
    sL=[]
    i = -1
    for lines in dataSet:
        i+=1
        matches = re.finditer(r'\W', lines)
        for match in matches:
            sym = match.group(); 
            if sym != '.':
                x = match.start()
                y = i
                sL.append([list(range(x-1,x+2)),list(range(y-1,y+2)),sym])
    return(sL)

def findParts(digits,symbols):
    pL = []
    for line in digits:
        c = 0
        for sets in symbols:
            cx = Counter(line[0]) & Counter(sets[0])
            cy = Counter(line[1]) & Counter(sets[1])
            if cx and cy: 
                c +=1
        if c > 0:
            pL.append(line)
    return(pL)

def sumParts(parts):
    p = 0
    for line in parts:
        p += line[2]
    return(p)

def findGears(parts, symbols):
    gL = []
    for sym in symbols:
        c = 0
        n = []
        if sym[2] == '*':
            for line in parts:
                cx = Counter(line[0]) & Counter(sym[0])
                cy = Counter(line[1]) & Counter(sym[1])
                if cx and cy: 
                    c += 1
                    if c<= 2:
                        n.append(line[2])
            if c == 2:
                gL.append([n[0],n[1],n[0]*n[1]])
    return(gL)

def sumGears(gears):
    g = 0
    for line in gears:
        g += line[2]
    return(g)

# =============================================================================
#  // TEST OUTPUT //
# =============================================================================

sLib = findSymbols(test3)
# for sets in sLib:
#     print(sets)    

dLib = findDigits(test3)
# for line in dLib:
#     print(line)

pLib = findParts(dLib,sLib) 
# for line in pLib:
#     print(line)
    
pTest = sumParts(pLib) # Output = 4361

print(f'The sum of all part nos. is {pTest}...and I am (theoretically) the Master of the Universe')
 
gLib = findGears(pLib,sLib)
# for line in gLib:
#     print(line)

gTest = sumGears(gLib) # Output = 467835

print(f'The sum of all gear ratios is {gTest}...and I am (still, theoretically) the Master of the Universe')


# =============================================================================
#  // PUZZLE OUTPUT //
# =============================================================================

sLib = findSymbols(day3)
    
dLib = findDigits(day3)

pLib = findParts(dLib,sLib) 
    
pSum = sumParts(pLib) 

print(f'The sum of all part nos. is {pSum}...and I am (for real) the Master of the Universe')

gLib = findGears(pLib,sLib)

gSum = sumGears(gLib) 

print(f'The sum of all gear ratios is {gSum}...and I am (still, for real) the Master of the Universe')