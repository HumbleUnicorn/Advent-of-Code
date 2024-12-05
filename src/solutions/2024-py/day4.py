# =============================================================================
# Ruth Wertz
# AOC 2024 - Day 4
# https://github.com/HumbleUnicorn/Advent-of-Code/tree/main/src/solutions/2024-py
# =============================================================================

# =============================================================================
#  // SOLUTION OUTLINE //
# =============================================================================
#
# // PART 1 //
# (1) read h, v, \, / lines
# (2) count instances of word and reversed(word)
# (3) return freq 
#
# // PART 2 //
# (1) find A, if not on border, test if legs of X contain "S" and "M"
# (2) if true, freq +=1
# (3) return freq
#        
# =============================================================================

# =============================================================================
#  // DEFINE FUNCTIONS // 
# =============================================================================

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
        return(data)

def parseGridStr (grid, word): #return <list> 
    lines = []; 
    n = len(grid); #print(n) #number of rows
    m = len(grid[0]); #print(m) #number of columns
    x = len(word)  
    ## Scan rows
    for row in grid:
        lines.append(row)
    ## Scan columns
    for j in range(m): #vertical columns
        col = str()
        for i in range(n):
            col += grid[i][j]
        lines.append(col)
    ## Search backslash diagonal
    for k in range(n): 
        i = k; j = 0; bsd = str()
        while i < n and j < m:
            bsd += grid[i][j]
            i += 1; j += 1
        if len(bsd) >= x:
            lines.append(bsd)
    for k in range(1,m):
        i = 0; j = k; bsd = str()
        while i < n and j < m:
            bsd += grid[i][j]
            i += 1; j += 1
        if len(bsd) >= x:
            lines.append(bsd)    
    ## Search front slash diagonal
    for k in range(n): 
        i = k; j = 0; fsd = str()
        while i >= 0 and j < m:
            fsd += grid[i][j]
            i -= 1; j += 1
        if len(fsd) >= x:
            lines.append(fsd)  
    for k in range(1,m):
        i = n-1; j = k; fsd = str()
        while i >= 0 and j < m:
            fsd += grid[i][j]
            i -= 1; j += 1
        if len(fsd) >= x:
            lines.append(fsd) 
    return(lines)

def findWordFreq (lines, word): #return <int> 
    freq = []
    for string in lines:
        freq.append(string.count(word)); freq.append(string.count(word[::-1]))
    return(sum(freq))

def findXFreq (grid, X): #return <int> 
    freq = 0
    n = len(grid) #number of rows
    m = len(grid[0]) #number of columns
    for i in range(n):
        for j in range(m):
            if grid[i][j] == X and i not in [0,n-1] and j not in [0,m-1]:
                legs = (grid[i+1][j+1]+grid[i-1][j-1],grid[i+1][j-1]+grid[i-1][j+1])
                if all(char in legs[0] for char in "MS") and all(char in legs[1] for char in "MS"):
                    freq += 1
    return(freq)

# =============================================================================
#  // TEST OUTPUT //
# =============================================================================

grid = readSrc('day4_test',False)
lines = parseGridStr(grid,'XMAS')

f = findWordFreq(lines,'XMAS')
print(f"Test Output1: {f}")

x = findXFreq(grid,'A')
print(f"Test Output2: {x}")
   
# =============================================================================
#   // PUZZLE OUTPUT //
# =============================================================================

grid = readSrc('day4',False)
lines = parseGridStr(grid,'XMAS')

f = findWordFreq(lines,'XMAS')
print(f"Output1: {f}")

x = findXFreq(grid,'A')
print(f"Output2: {x}")