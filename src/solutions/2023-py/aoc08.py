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
# // PART 2 //
#  
# Reference: (https://www.w3schools.com/python/python_lists_comprehension.asp)
# gist = [expression *for* item *in* iterable *if* condition == True]   
#
# ghost keys = filtered list of keys where last char = 'A'
# 
# First Plan 
#     *update* change 1st key ---> keys = list of ghost keys  
#     *update* change key = new key ---> keys = new keys 
#     *update* change break condition ---> check if all keys end with 'Z'
# Works, BUT simultaneous looping taking toooooo long... 
#
# Second Plan
#     Get no. of steps for each ghost key to get to '**Z'---> solve for LCM
#
# =============================================================================


# =============================================================================
#  //INPUT DATA//
# =============================================================================

test8a=[]
with open('inputs/t08a.txt') as f: 
    for lines in f:
        test8a.append(lines)  
        
test8b=[]
with open('inputs/t08b.txt') as f: 
    for lines in f:
        test8b.append(lines)  
                     
day8=[]
with open('inputs/d08.txt') as f: 
    for lines in f:
        day8.append(lines) 


# =============================================================================
#  // DEFINE FUNCTIONS // 
# =============================================================================

# from collections import Counter
# imprt re
import math

def parseInst(data):                # return list of instructions as L = 0, R = 1
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

def parseMap(data):                 # return dict of map as {'KEY': [L,R]}
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

def ghostKeys(map):
    key_list = list(map.keys())
    filtered_keys = [item for item in key_list if item[2] == 'A']
    return filtered_keys

def countSteps(inst, map):          # count steps from key = 'AAA' to key = 'ZZZ', return c     
    key = 'AAA'
    c=0
    while True:
        for i in range(len(inst)):  
            index=inst[i]                       # call intruction 
            key = map.get(key)[index]           # call new key  
            c+=1                                # increase counter
            if i == len(inst)-1:                # check value of i, reset to 0 if last pos
                i = 0
        if key == 'ZZZ':                        # check value of key, break if 'ZZZ'
            break
    return c

def ghostSteps(inst, map, key):     # count steps from key = '**A' to key = '**Z', return c     
    key_start = key
    c=0
    while True:
        for i in range(len(inst)):  
            index=inst[i]                       # call intruction 
            key = map.get(key)[index]           # call new key  
            c+=1                                # increase counter
            if i == len(inst)-1:                # check value of i, reset to 0 if last pos
                i = 0
        if key[2] == 'Z':                       # check value of key, break if '**Z'
            break
    return c

def OLDghostSteps(inst,map,keys):      # NOT USED
    c=0
    while True:
        for i in range(len(inst)):              # loop through instructions
            index = inst[i]                     # call instruction 
            new = []
            for key in keys:                    # call list of new keys
                new.append(map.get(key)[index])        
            keys = new                          # retain new keys    
            c+=1                                # increase counter
            if i == len(inst)-1:                # check value of i, reset to 0 if last pos
                i = 0
        if all(key[2] =='Z' for key in keys):   # check value of key, break if all end with 'Z'
            break
    return c


# =============================================================================
#  // TEST OUTPUT //
# =============================================================================

inst = parseInst(test8a); #print(inst)

map = parseMap(test8a); #print(map)

steps = countSteps(inst, map); #print(steps)

inst_b = parseInst(test8b); #print(inst_b)

map_b = parseMap(test8b); #print(map_b)

keys = ghostKeys(map_b); #print(keys)

gSteps = []
for key in keys:
    gSteps.append(ghostSteps(inst_b, map_b, key))

steps = math.lcm(*gSteps); #print(steps) 
   
# =============================================================================
#   // PUZZLE OUTPUT //
# =============================================================================

inst = parseInst(day8); #print(inst)

map = parseMap(day8); #print(map)

steps = countSteps(inst, map); #print(steps)

keys = ghostKeys(map); print(keys)

gSteps = []
for key in keys:
    gSteps.append(ghostSteps(inst, map, key))
print(gSteps)

steps = math.lcm(*gSteps); print(steps) 


