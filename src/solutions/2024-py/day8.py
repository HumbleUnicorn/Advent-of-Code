# =============================================================================
# Ruth Wertz
# AOC 2024 - Day 7
# https://github.com/HumbleUnicorn/Advent-of-Code/tree/main/src/solutions/2024-py
# =============================================================================

# =============================================================================
#  // SOLUTION OUTLINE //
# =============================================================================
#
# // PART 1 //
# (1) parse to list of results and list of values
# (2) enumerate trials (possible combinations of operators)
# (3) if trial == result, resultSum += result
#
# // PART 2 //
# (1) Update operators to include concat (a <opp> b --> int(ab))
#        
# =============================================================================

# =============================================================================
#  // DEFINE FUNCTIONS // 
# =============================================================================

import re
from collections import Counter

def readSrc (fname, split_alt=0): #return <list>
    with open(f'ignore/{fname}.txt', 'r') as file:
        data = []
        for line in file:
            line = line.strip()
            if split_alt == False:
                pass
            elif split_alt != 0:
                line = line.split(split_alt)
            else:
                line = line.split(' ')
            data.append(line)
        return data
    
def readSrcAsStr (fname,replace=0): #return <str>
    with open(f'ignore/{fname}.txt', 'r') as file:
        f = file.read()
        if replace:
            data = f.replace(replace[0],replace[1])
            return(data)
        else:
            data = f.strip()
        return(data)    

def getGrid (input): #return <tuple> as grid, n, m (day8)
    grid = readSrc(input)
    n = len(grid)
    m = len(grid[0])
    return(grid,n,m)

def getPairs (data, text, pattern): #return <list> of <tuple> (day8)
    ## define antenna frequencies
    def getChars (pattern, text): #return <dict> (day8)
        matches = re.findall(pattern, text)
        chars = Counter(matches)
        return(chars)
    def getCombos (objectList): #return <list> of <tuple> 
        return [(a, b) for i, a in enumerate(objectList) for b in objectList[i+1:]]
    cLib = getChars(pattern, text)
    ## plot antenna 
    grid, n, m = data
    pLib={}
    for key in cLib.keys():
        loc = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == key:
                    loc.append((i,j))
        pLib.update({key:getCombos(loc)})
    return(pLib)

def getNodePairs (lib, data): #return <list> of <tuple> (day8)
    grid, n, m = data
    nodes=[]
    for key in lib.keys():
        for pair in lib[key]:
            b, c = (bi,bj), (ci, cj) = pair
            a = (ai, aj) = (2*bi-ci, 2*bj-cj)
            if ai in range(n) and aj in range(m):
                nodes.append(a)
            d = (di, dj) = (2*ci-bi, 2*cj-bj)
            if di in range(n) and dj in range(m):
                nodes.append(d)
    nodes  = list(set(nodes))
    return(nodes)

def getAllNodes (lib, data): #return <list> of <tuple> (day8)
    grid, n, m = data
    def inBounds(point):
        i, j = point
        if i in range(n) and j in range(m):
            return(True)
        else:
            return(False)
    nodes = []
    for key in lib.keys():
        for pair in lib[key]:
            #print('key:',key,'pair:',pair)
            x, y = pair
            nodes += [x, y]
            b, c = (bi, bj), (ci, cj) = x, y
            a = i, j = 2*bi-ci, 2*bj-cj 
            onMap = inBounds(a)
            while onMap:
                #print(onMap, a)
                nodes += [a]
                newPair = (a, b)
                b, c = (bi, bj), (ci, cj) = newPair
                a = i, j = 2*bi-ci, 2*bj-cj 
                onMap = inBounds(a)  
            b, c = (bi, bj), (ci, cj) = x, y     
            d = i, j = 2*ci-bi, 2*cj-bj 
            onMap = inBounds(d)
            while onMap:
                #print(onMap, d)
                nodes += [d]
                newPair = (c, d)
                b, c = (bi, bj), (ci, cj) = newPair
                d = i, j = 2*ci-bi, 2*cj-bj 
                onMap = inBounds(d)  
    nodes=list(set(nodes))
    return(nodes)

# =============================================================================
#  // TEST OUTPUT //
# =============================================================================

gridlines = readSrcAsStr('day8_test',['\n',''])
gridmap = getGrid('day8_test')
pairLib = getPairs(gridmap,gridlines,r'([A-Za-z0-9])')
nodes = getNodePairs(pairLib,gridmap)
print(f"Test Output1: {len(nodes)}")

allnodes = getAllNodes(pairLib,gridmap)
print(f"Test Output2: {len(allnodes)}")
   
# =============================================================================
#   // PUZZLE OUTPUT //
# =============================================================================

gridlines = readSrcAsStr('day8',['\n',''])
gridmap = getGrid('day8')
pairLib = getPairs(gridmap,gridlines,r'([A-Za-z0-9])')
nodes = getNodePairs(pairLib,gridmap)
print(f"Output1: {len(nodes)}")

allnodes = getAllNodes(pairLib,gridmap)
print(f"Output2: {len(allnodes)}")