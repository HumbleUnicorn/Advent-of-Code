# =============================================================================
# Ruth Wertz
# AOC 2023 - Day 10
# https://github.com/HumbleUnicorn/Advent-of-Code/blob/main/src/solutions/2023-py/aoc10.py
# =============================================================================

# =============================================================================
#  // SOLUTION OUTLINE //
# =============================================================================
#
# // PART 1 //
# 
# S = (r,c) ---> store (r,c) in list with index of 0
#     Test for connections to N, E, S, W ---> start with N, move CW
#         If connection, next = (r,c) 
#             If next != start, append to list, else steps = (len(list))/2
#           
# // PART 2 //
#
# io scan
#     set I/O counter = 0
#     read each char in lines of data
#     if char has [r,c] in the loop
#         if char "type" has a stem (e.g.,'N':["┌","|","┐"]) ---> increment I/O counter
#         all ----> print pipe char 
#     otherwise
#         if counter is even ---> outside, print "O"
#         if counter is odd ---> inside, print "I", increment "innie" counter

# =============================================================================

# =============================================================================
#  //INPUT DATA//
# =============================================================================

test10=[]
with open('inputs/t10.txt') as f: 
    for lines in f:
        test10.append(lines)  

# for lines in test10:
#     print(lines)

day10=[]
with open('inputs/d10.txt') as f: 
    for lines in f:
        day10.append(lines) 

types = {'N': ["┌","|","┐"], 'E': ["┘","─","┐"], 'S': ["└","|","┘"], 'W': ["└","─","┌"], '┘': ['N','W'], '└': ['N','E'], '┌': ['E','S'], '┐': ['S','W'], '|': ['N','S'], '─': ['E','W']}

moves = {'N': [-1,0], 'E': [0,1], 'S': [1,0], 'W': [0,-1]}

# =============================================================================
#  // DEFINE FUNCTIONS // 
# =============================================================================

def prettyMap(data):
    new=[]
    for lines in data:
        lines = lines.replace("\n","")
        lines = lines.replace("F","┌")
        lines = lines.replace("J","┘")
        lines = lines.replace("L","└")
        lines = lines.replace("7","┐")
        lines = lines.replace("-","─")
        lines = lines.replace("/","|")
        new.append(lines)
    return new

def wheresWaldo(data):
    for lines in data:
        if "S" in lines:
            r = data.index(lines)
            c = lines.index("S")
    return [r,c]

def matchType(data,srt,cMap=types):             # match pipe type based on connectors
    r = srt[0]
    c = srt[1]
    n = len(data)-1
    m = len(data[0])-1 
    val = []
    if r >= 0 and data[r-1][c] in cMap.get('N'):
        val.append('N')
    if c <= m and data[r][c+1] in cMap.get('E'):
        val.append('E')
    if r+1 <= n and data[r+1][c] in cMap.get('S'):
        val.append('S')
    if c-1 >= 0 and data[r][c-1] in cMap.get('W'):
       val.append('W')
    for k,v in cMap.items():
       if v == val:
           return k
       
def fitPipe(data,srt):                          # return the type of just the starting pipe
    r = srt[0]
    c = srt[1]
    start = [r,c]                               
    type = matchType(data,srt) 
    return type# type = 'F'

def findLoop(data,srt,cMap=types,mMap=moves):
    r = srt[0]
    c = srt[1]
    start = [r,c]                               # start = [2,0]
    type = matchType(data,start)                # type = '┌'
    loop = [start]                              # loop = [[2,0]]
    while True:     
        at = cMap.get(type)                     # at = ['E','S']          
        move = mMap.get(at[0])                  # move = [0,1] ('E')
        r += move[0]                            # r = 2
        c += move[1]                            # c = 1
        if [r,c] in loop and [r,c] != start:    # check if [2,1] in already in loop ---> FALSE           
            r-= move[0]                             # if TRUE ---> undo last move
            c-= move[1]                             # if TRUE ---> undo last move
            move = mMap.get(at[1])                  # if TRUE ---> move [1,0] ('S')
            r += move[0]                            # if TRUE ---> r = 3
            c += move[1]                            # if TRUE ---> c = 0
        if [r,c] != start:                      # check if [2,1] is NOT start ---> TRUE
            loop.append([r,c])                      # if TRUE ---> append [2,1] to loop
            type = data[r][c]                       # if TRUE ---> next type = '┘'
        else:
            break                                   # if FALSE ---> break condition
    return loop 

def findInnies(data,srt,loop,cMap=types,mMap=moves):
    nL=[]
    for r in range(len(data)):
        line = data[r]
        new=str()
        io=0
        for c in range(len(line)):
            char  = line[c]
            if [r,c] in loop:
                if char == 'S': 
                    char = fitPipe(data,srt)
                if char in cMap.get('N'):
                    io +=1
                    new += char
                else: 
                    new += char
            else:
                if io % 2 == 0:
                    new += "O"
                else: 
                    new += "I"
        nL.append(new)
    return nL

 
# ===========================================================================
#  // TEST OUTPUT //
# =============================================================================

pMap = prettyMap(test10)
# for lines in pMap:
#     print(lines)
    
sRC = wheresWaldo(pMap); #print(sRC)

loop = findLoop(pMap,sRC); #print(loop)

n = len(loop)/2; print(int(n))

inner = 0
traps = findInnies(pMap,sRC,loop)
for lines in traps:
    inner += lines.count("I")
    print(lines)
    
print(inner)
                    
# =============================================================================
#   // PUZZLE OUTPUT //
# =============================================================================

pMap = prettyMap(day10)
# for lines in pMap:
#     print(lines)    
    
sRC = wheresWaldo(pMap); #print(sRC)

loop = findLoop(pMap,sRC); #print(loop)

n = len(loop)/2; print(int(n))

inner = 0
traps = findInnies(pMap,sRC,loop)
for lines in traps:
    inner += lines.count("I")
    print(lines)
    
print(inner)