# =============================================================================
# Ruth Wertz
# AOC 2023 - Day 6
# https://github.com/HumbleUnicorn/Advent-of-Code/blob/main/src/solutions/2023-py/aoc06.py
# =============================================================================

# =============================================================================
#  // SOLUTION OUTLINE //
# =============================================================================
#
# // PART 1 //
# Example: [1,6] **LB** [2,5] [3,4] [4,3] [5,2] **UB** [6,1]
#
# Lower bound: x*(7-x) = 9 ---> x^2 - 7x + 9 = 0 ---> Solve for lowest value of x
#      a = 1, b = -time, c = distance            ---> LB = next int > x
#    
# Number of winning options: LB to (time - LB)    ---> n = len of r (LB,t-LB+1)
# 
# // PART 2 //
# Adjust input as [[t,d]]
#
# =============================================================================

# =============================================================================
#  //INPUT DATA//
# =============================================================================

test6=[]
with open('inputs/t06.txt') as f: 
    for lines in f:
        test6.append(lines)    

day6=[]
with open('inputs/d06.txt') as f: 
    for lines in f:
        day6.append(lines) 

# =============================================================================
#  // DEFINE FUNCTIONS // 
# =============================================================================

import re

def raceInfo(data):
    t=[]
    nums = re.finditer(r'\d+', data[0])
    for num in nums:
        t.append(int(num.group()))
    d=[]
    nums = re.finditer(r'\d+', data[1])
    for num in nums:
        d.append(int(num.group())) 
    r=[]
    for i in range(len(t)):
        r.append([t[i],d[i]])
    return(r)

def newRaceInfo(inputs):
    t=str()
    d=str()
    for lines in inputs:
        t += str(lines[0])
        d += str(lines[1])  
    return([[int(t),int(d)]])

import cmath

def findRoot(lines):
    a = 1
    b = -lines[0]
    c = lines[1]  
    D = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b - D) / (2*a); 
    root2 = (-b + D) / (2*a); 
    if isinstance(root1, complex):
        root1 = root1.real
    if isinstance(root2, complex):
        root2 = root2.real
    return(min(root1,root2))
     
def findWins(inputs):
    n=[]
    for lines in inputs: 
        t = lines[0]
        d = lines[1]
        x = findRoot(lines)
        LB = int(x)+1
        n.append(len(range(LB,t-LB+1)))
        p=1
        for lines in n:
            p *= lines
    return(p)

# =============================================================================
#  // TEST OUTPUT //
# =============================================================================

inputs = raceInfo(test6); #print(inputs)

# wins = findWins(inputs); print(wins)

newInput = newRaceInfo(inputs); #print(newInput)

wins = findWins(newInput); print(wins)
    
# =============================================================================
#   // PUZZLE OUTPUT //
# =============================================================================

inputs = raceInfo(day6); #print(inputs)

# wins = findWins(inputs); print(wins)

newInput = newRaceInfo(inputs); #print(newInput)

wins = findWins(newInput); print(wins)