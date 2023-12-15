# =============================================================================
# Ruth Wertz
# AOC 2023 - Day 5
# https://github.com/HumbleUnicorn/Advent-of-Code/blob/main/src/solutions/2023-py/aoc05.py
# =============================================================================

# =============================================================================
# Part 1 Outline
# 
# function mapDict ---> Nested Dict {map name: {src No:dst No}}
#     for lines:
#         if line is key, store index location  
#         if line has digits: send list(ints) to value in stored index location
#     zip key, value {map name: list of (dst,src,len)}  
#     for keys:
#         src range = list of ints from src to src+len 
#         dst range = list of ints from dst to dst+len
#     zip src range, dst range {src No:dst No}
#     dict[key] = nested dict{src No:dst No}
# 
# function find seed location ---> list of location ints
#     for n in seeds
#         for maps:
#             if n in map, store n as m (else is keep as n)
#             keep last value of n  
# find min n   
#
# Part 2 Outline
#
# =============================================================================

# =============================================================================
#  //INPUT DATA//
# =============================================================================

k = ['seeds:','seed-to-soil map:','soil-to-fertilizer map:','fertilizer-to-water map:','water-to-light map:','light-to-temperature map:','temperature-to-humidity map:','humidity-to-location map:']

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

def mapsDict(data,k):
    v = []
    for i in range(len(k)):                     #one list per map
        v.append(list())
    for line in data:           
        if line in k:                           #key: fetch & store index
            j = k.index(line)
        if any(c.isdigit() for c in line):      #value: fetch & store list of ints
            n=[]
            nums = re.finditer(r'\d+', line)
            for num in nums:
                n.append(int(num.group()))
            v[j].append(n)                      
    maps=dict(zip(k,v))                         #dict: {'map name':[[dst, src, len],[...]}
    for key in k:
        if "map" in key:
            src=[]
            dst=[]
            val = maps.get(key)                 
            for n in val:                       
                src += list(range(n[1],n[1]+n[2])) #[list all ints in range(src,src+len)]
                dst += list(range(n[0],n[0]+n[2])) #[list all ints in range(src,src+len)
            d = dict(zip(src,dst))
            maps[key]=d 
        else:
            maps[key]=maps.get(key)[0]
    return(maps)

def seedMapsTest(maps,k):
    seeds = maps.get(k[0])
    path = []
    for n in seeds: 
        line=[n]              
        for i in range(1,len(k)):  
            m = maps.get(k[i]) 
            if n in m:
                n = m.get(n)
            line.append([i,n])
        path.append(line)
    return(path)
 
def seedLocTest(seedMap,sL=[]):
   for lines in seedMap:
       n=len(lines)
       sL.append(lines[n-1][1])
   return(sL)   

def seedLoc(maps,k):
    seeds = maps.get(k[0])
    loc = []
    for n in seeds:             
        for i in range(1,len(k)):  
            m = maps.get(k[i]) 
            if n in m:
                n = m.get(n)
        loc.append(n)
    return(loc)

# =============================================================================
#  // TEST OUTPUT //
# =============================================================================
 
maps = mapsDict(test5,k); #print(maps)

paths = seedMapsTest(maps,k)

locs_test = seedLocTest(paths)
print(min(locs_test))

locs = seedLoc(maps,k)
print(min(locs))
           
# =============================================================================
#   // PUZZLE OUTPUT //
# =============================================================================

maps = mapsDict(day5,k); 

locs = seedLoc(maps,k)
print(min(locs))
