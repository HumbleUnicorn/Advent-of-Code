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
# Uhhhh... no idea
#
# =============================================================================

# =============================================================================
#  //INPUT DATA//
# =============================================================================

test10=[]
with open('inputs/t10.txt') as f: 
    for lines in f:
        lines = lines.replace("\n","")
        test10.append(lines)  

for lines in test10:
    print(lines)

day10=[]
with open('inputs/d10.txt') as f: 
    for lines in f:
        day10.append(lines) 

types = {'N': ["F","|","7"], 'E': ["J","-","7"], 'S': ["L","|","J"], 'W': ["L","-","F"], 'J': ['N','W'], 'L': ['N','E'], 'F': ['E','S'], '7': ['S','W'], '|': ['N','S'], '-': ['E','W']}

moves = {'N': [-1,0], 'E': [0,1], 'S': [1,0], 'W': [0,-1]}

# =============================================================================
#  // DEFINE FUNCTIONS // 
# =============================================================================

def wheresWaldo(data):
    for lines in data:
        if "S" in lines:
            r = data.index(lines)
            c = lines.index("S")
    return [r,c]

def matchType(data,srt,cMap=types): 
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

def findLoop(data,srt,cMap=types,mMap=moves):
    r = srt[0]
    c = srt[1]
    start = [r,c]                               # start = [2,0]
    type = matchType(data,start)                # type = 'F'
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
            type = data[r][c]                       # if TRUE ---> next type = 'J'
        else:
            break                                   # if FALSE ---> break condition
    return loop 


# ===========================================================================
#  // TEST OUTPUT //
# =============================================================================

S = wheresWaldo(test10); print(S)

loop = findLoop(test10,S); print(loop)

n = len(loop)/2; print(int(n))

                    
# =============================================================================
#   // PUZZLE OUTPUT //
# =============================================================================

S = wheresWaldo(day10); print(S)

loop = findLoop(day10,S); print(loop)

n = len(loop)/2; print(int(n))