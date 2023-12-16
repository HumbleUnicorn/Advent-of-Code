# =============================================================================
# Ruth Wertz
# AOC 2023 - Day 5
# https://github.com/HumbleUnicorn/Advent-of-Code/blob/main/src/solutions/2023-py/aoc05.py
# =============================================================================

# =============================================================================
# Part 1 Outline
# 
# function mapDict ---> Dict {map name: [list of lists]}
#     for lines:
#         if line is key, {key:[]}  
#         if line has digits: append list of ints to key value
#     return dict
# 
# function find seed location ---> list of location ints
#     for n in seeds
#         for map in maps:
#             if start <= n < end:
#                 modifier (start source - start dest)
#             n = n - modifier
#         keep last value of n  
# find min n   
#
# Part 2 Outline
# 
# function to expand seed no sets to ranges ---> for no in
# 
#
# =============================================================================

# =============================================================================
#  //INPUT DATA//
# =============================================================================

names = ['seed-to-soil map:','soil-to-fertilizer map:','fertilizer-to-water map:','water-to-light map:','light-to-temperature map:','temperature-to-humidity map:','humidity-to-location map:']

test5=[]
with open('inputs/t05.txt') as f: 
    for lines in f:
        lines = lines.strip()
        test5.append(lines)    

day5=[]
with open('inputs/d05.txt') as f: 
    for lines in f:
        lines = lines.strip()
        day5.append(lines) 

# =============================================================================
#  // DEFINE FUNCTIONS // 
# =============================================================================

import re

def mapKeys(mapNames): #for funsies (e.g., readability)
    abv=[]
    for name in mapNames:
        i = name.rfind("-")
        if i>0:
            abv.append(name[i+1:i+5])
    return(abv)

def mapIndex(data,mapNames):
    index=[]        
    for name in mapNames:
        index.append(data.index(name))
    index.append(len(data))
    return(index)

def mapsDict(data,index,keys):
    mDict={}
    for key in keys:
        mDict.update({key:[]})
    i=0
    while i < len(index)-1:
        key = keys[i]
        for j in range(index[i]+1,index[i+1]):
            line = data[j]
            key = keys[i]                          
            if any(c.isdigit() for c in line):      
                n=[]
                nums = re.finditer(r'\d+', line)
                for num in nums:
                    n.append(int(num.group()))
                mDict[key].append(n)
        i+=1                                 
    return(mDict)

def findSeeds(data):
    seeds = data[1]
    seeds_str = seeds.split(' ')
    seeds_int = list(map(int, seeds_str))
    return(seeds_int)

def findPath(seeds,keys,maps): # Use for troubleshooting
    path=[]
    for n in seeds:
        p=[n]
        for k in keys:
            m=0
            for r in maps.get(k):
                if r[1]<=n<(r[1]+r[2]):
                    m = r[1]-r[0]
            n = n-m
            p.append([k,n])
        path.append(p)
    return(path)

def findLocation(seeds,keys,maps): # Returns locations only
    end=[]
    for n in seeds:
        for k in keys:
            m=0
            for r in maps.get(k):
                if r[1]<=n<(r[1]+r[2]):
                    m = r[1]-r[0]
            n = n-m
        end.append(n)
    return(end)

def findPairs(seeds):
    pairs=[]
    for i in range(len(seeds)):
        n = seeds[i]
        if i % 2 == 0: # If number is even
            line = [n]
        else:          # If number is odd
            line += [n]
            pairs.append(line)
    return(pairs)

def findPathByPair(pairs,keys,maps): # Use for troubleshooting
    path=[]
    for pair in pairs:
        seeds = range(pair[0],pair[0]+pair[1])
        for n in seeds:
            p=[n]
            for k in keys:
                m=0
                for r in maps.get(k):
                    if r[1]<=n<(r[1]+r[2]):
                        m = r[1]-r[0]
                n = n-m
                p.append([k,n])
            path.append(p)
    return(path)

def findLocMin(pairs,keys,maps,minLoc): # Use for troubleshooting
    for pair in pairs:
        seeds = range(pair[0],pair[0]+pair[1])
        for n in seeds:
            for k in keys:
                m=0
                for r in maps.get(k):
                    if r[1]<=n<(r[1]+r[2]):
                        m = r[1]-r[0]
                n = n-m
            if n < minLoc:
                minLoc = n
    return(minLoc)

# =============================================================================
#  // TEST OUTPUT //
# =============================================================================

keys = mapKeys(names); #print(keys)       #define abrv map keys 

index = mapIndex(test5,names)             #define 

maps = mapsDict(test5,index,keys)         #parse data into dict 

seeds = findSeeds(test5); #print(seeds)   #define list of seed numbers

# paths = findPath(seeds,keys,maps)       #list: [seed, [key,no], [key,num], ] 
# for line in paths:
#     print(line)

locs = findLocation(seeds,keys,maps)
locMin = min(locs); print(locMin)

pairs = findPairs(seeds); #print(pairs)   #define list of seed pairs

paths = findPathByPair(pairs,keys,maps)   #list: [seed, [key,no], [key,num], ]

minLoc = findLocMin(pairs,keys,maps,locMin)   
print(minLoc)
           
# =============================================================================
#   // PUZZLE OUTPUT //
# =============================================================================

index = mapIndex(day5,names)            

maps = mapsDict(day5,index,keys); #print(maps)       

seeds = findSeeds(day5); #print(seeds)    

# paths = findPath(seeds,keys,maps)         
# for line in paths:
#     print(line)
    
locs = findLocation(seeds,keys,maps)
locMin = min(locs); print(locMin)

pairs = findPairs(seeds); #print(pairs)   #define list of seed pairs

# paths = findPathByPair(pairs,keys,maps)   #list: [seed, [key,no], [key,num], ]

minLoc = findLocMin(pairs,keys,maps,locMin)   
print(minLoc)