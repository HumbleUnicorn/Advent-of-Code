# =============================================================================
# Ruth Wertz
# AOC 2023 - Day 9
# https://github.com/HumbleUnicorn/Advent-of-Code/blob/main/src/solutions/2023-py/aoc09.py
# =============================================================================

# =============================================================================
#  // SOLUTION OUTLINE //
# =============================================================================
#
# // PART 1 //
#
# function for history of one sequence (seq ---> return sum of last in each redux)
#     last = last val of seq
#     while true     
#         for i in length of seq -1
#             store difference of seq[i+1] - seq[i] in "next" list
#         last += last val of next
#         if all in next = 0
#             return last & break
#         else: 
#             seq = next
#
# // PART 2 //
# 
# amend prev function to store list of fist digits 
# sum in reverse order (odd = +, even = -)
#        
# =============================================================================

# =============================================================================
#  //INPUT DATA//
# =============================================================================

test9=[]
with open('inputs/t09.txt') as f: 
    for lines in f:
        test9.append(lines)  
        
day9=[]
with open('inputs/d09.txt') as f: 
    for lines in f:
        day9.append(lines) 


# =============================================================================
#  // DEFINE FUNCTIONS // 
# =============================================================================

# from collections import Counter
# imprt re
# import math

def parseLines(data):                # return sequence in list
    d=[]
    for lines in data:
        lines = lines.strip('\n')   
        lines = lines.split(' ')
        lines = list(map(int, lines))
        d.append(lines) 
    return d

def getRightHist(seq):
    last = seq[-1]
    while True:
        next = []
        for i in range(len(seq)-1):
            next.append(seq[i+1]-seq[i])
        last += next[-1]
        if all(x == 0 for x in next):
            return last
        else:
            seq = next
            
def getLeftHist(seq):
    first = [seq[0]]
    while True:
        next = []
        for i in range(len(seq)-1):
            next.append(seq[i+1]-seq[i])
        first.append(next[0])
        if all(x == 0 for x in next):
            print(first)
            break
        else:
            seq = next
    fSum=0
    for i in reversed(range(len(first))):
        if i % 2 == 0: 
            fSum += first[i]
        else: 
            fSum -= first[i]
    return fSum

# =============================================================================
#  // TEST OUTPUT //
# =============================================================================

seqs = parseLines(test9)

hR=0
for seq in seqs:
    hR += getRightHist(seq)
print(hR)   

hL = 0
for seq in seqs:
    hL += getLeftHist(seq)
print(hL)

# =============================================================================
#   // PUZZLE OUTPUT //
# =============================================================================

seqs = parseLines(day9)

hR=0
for seq in seqs:
    hR += getRightHist(seq)
print(hR) 

hL=0
for seq in seqs:
    hL += getLeftHist(seq)
print(hL)