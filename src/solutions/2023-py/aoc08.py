# =============================================================================
# Ruth Wertz
# AOC 2023 - Day 8
# https://github.com/HumbleUnicorn/Advent-of-Code/blob/main/src/solutions/2023-py/aoc08.py
# =============================================================================

# =============================================================================
#  // SOLUTION OUTLINE //
# =============================================================================
#
# // PART 1 //
#
# Parse Data
#     Instructions: Convert first line into list where 'L' = 0 and 'R' = 1 
#     Map: Stoe as dict {'KEY': [L,R]}
#
# function to count steps (while loop)
#     set 1st key = 'AAA'
#     set counter = 0
#     while True --- loop indefinitely
#         for i in range(n) ---> n = len(instructions)
#             index = instructions[i] ---> 0 or 1
#             key = new key ---> get stored pair from map, get index from inst 
#             counter += 1
#             check
#                 if i at last pos of n, reset i to 0 ---> loop inst indefinitely
#                 if new key == 'ZZZ', break ---> end loop, return counter value
# 
# 
#
# // PART 2 //
# 
#
#        
# =============================================================================


# =============================================================================
#  //INPUT DATA//
# =============================================================================

test8=[]
with open('inputs/t08.txt') as f: 
    for lines in f:
        test8.append(lines)  
        
                
day8=[]
with open('inputs/d08.txt') as f: 
    for lines in f:
        day8.append(lines) 


# =============================================================================
#  // DEFINE FUNCTIONS // 
# =============================================================================

# from collections import Counter
# imprt re

def parseInst(data):
    line = data[0]
    line = line.replace('\n','')
    line = line.replace('L','0')
    line = line.replace('R','1')
    inst=[]
    for c in line:
        inst.append(int(c))
    data.pop(1)
    data.pop(0)
    return inst

def parseMap(data):
    map={}
    for line in data:
        line = line.replace('\n','')
        line = line.replace(' ','')
        line = line.replace('(','')
        line = line.replace(')','')
        line = line.split("=")
        line[1] = line[1].split(',')
        map.update({line[0]:line[1]})
    return map

def countSteps(inst,map):
    key = 'AAA'
    c=0
    while True:
        for i in range(len(inst)):
            index=inst[i]
            key = map.get(key)[index]
            c+=1
            if i == len(inst)-1:
                i = 0
        if key == 'ZZZ':
            break   
    return c


# =============================================================================
#  // TEST OUTPUT //
# =============================================================================

inst = parseInst(test8); #print(inst)

map = parseMap(test8); #print(map)

steps = countSteps(inst,map); print(steps)
    
    
    

   
# =============================================================================
#   // PUZZLE OUTPUT //
# =============================================================================

inst = parseInst(day8); #print(inst)

map = parseMap(day8); #print(map)

steps = countSteps(inst,map); print(steps)