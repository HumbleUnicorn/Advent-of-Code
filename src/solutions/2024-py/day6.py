# =============================================================================
# Ruth Wertz
# AOC 2024 - Day 6
# https://github.com/HumbleUnicorn/Advent-of-Code/tree/main/src/solutions/2024-py
# =============================================================================

# =============================================================================
#  // SOLUTION OUTLINE //
# =============================================================================
#
# // PART 1 //
# (1) Find start
# (2) Move to next obstruction: 
# (a) mark visited points as 'X' 
# (b) append (i,j) to path list
# (3) Sum = count('X') for row in grid
#
# // PART 2 //
# (1) For each point in path that isn't original start
# (a) move to next obstruction; record 'leg' as str in list 
# (b) if count(leg) > 1 ===> loop True; obst += 1
# (c) if out of range ===> loop False
# (2) return obst
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

def walkPath(data,out): #return 'map', 'walk', or 'path'
    ## Define Grid
    grid = data.copy(); n = len(grid); m = len(grid[0])
    dir = ["^", ">", "v", "<",]; move = {"^":(-1,0), ">":(0,1),"v":(1,0),"<":(0,-1)}
    ## Point, Char, and Location
    def pt(i,j):
        return f"({i},{j})"
    def char(i,j):
        return(grid[i][j])
    def write(sym,i,j):
        grid[i] = grid[i][:j]+sym+grid[i][j+1:]
    def loc(pool):
        for i in range(n):
            for j in range(m):
                if char(i,j) in pool:
                    return(i,j)
    ## Initiate Path
    path = []; walk = []
    s = loc(dir); i = s[0]; j = s[1]; d = char(i,j)
    ## Initiate Leg Loop
    leg = str()
    while True:
        leg += pt(i,j); path.append((i,j))
        last = i,j
        write("X",i,j)
        i = i + move[d][0]; j = j + move[d][1]
        try:
            if char(i,j) in [".","X"]:
                write("X",i,j)
            else:
                i = last[0]; j = last[1]
                x = dir.index(d)
                try:
                    d = dir[x+1]
                except:
                    d = dir[0]
                walk.append(leg); #print(path)
                leg = str()
        except:
            walk.append(leg)
            if out == 'map':
                return(grid)
            elif out == 'walk':
                return(walk)
            else:
                return (list(set(path)))

def getPathSum(data): #return <int>
    sum = 0
    for i in range(len(data)):
        sum += data[i].count("X")
    return(sum)

def getObstSum(data,path): #return <int>
    ## Define Grid
    grid = data.copy(); n = len(grid); m = len(grid[0])
    dir = ["^", ">", "v", "<",]
    ## Point, Char, and Location
    def pt(i,j):
        return f"({i},{j})"
    def char(i,j):
        return(grid[i][j])
    def write(sym,i,j):
        grid[i] = grid[i][:j]+sym+grid[i][j+1:]
    def loc(pool):
        for i in range(n):
            for j in range(m):
                if char(i,j) in pool:
                    return(i,j)
    def testPath(i,j,d):
        move = {"^":(-1,0), ">":(0,1),"v":(1,0),"<":(0,-1)}
        walk = []; leg = str()
        while True:
            leg += pt(i,j)
            last = i,j
            i = i + move[d][0]; j = j + move[d][1]
            if i in range(n) and j in range(m):
                if char(i,j) not in ["#","O"]:
                    continue
                else:
                    i = last[0]; j = last[1]
                    x = dir.index(d)
                    try:
                        d = dir[x+1]
                    except:
                        d = dir[0]
                    walk.append(leg); #print(leg)
                    if walk.count(leg) > 1:
                        #print(True, point)
                        return(True)
                    else:  
                        leg = str()
            else:
                return(False)
    ## Initiate Walk
    s = start = loc(dir); i = s[0]; j = s[1]; d = char(i,j)
    obst=0
    for point in path:
        #print(point)
        c = char(point[0],point[1])
        if point != start:
            write("O",point[0],point[1])
            if testPath(i,j,d):
                obst += 1
            write(c,point[0],point[1])
    return(obst)

# =============================================================================
#  // TEST OUTPUT //
# =============================================================================

grid = readSrc('day6_test')
map = walkPath(grid,'map')
#for line in map:
#    print(line)
pathSum = getPathSum(map); 
print(f"Test_Output1: {pathSum}")

path = walkPath(grid,'path')
obstSum = getObstSum(grid,path); 
print(f"Test_Output2: {obstSum}")
   
# =============================================================================
#   // PUZZLE OUTPUT //
# =============================================================================

grid = readSrc('day6')
map = walkPath(grid,'map')
#for line in map:
#    print(line)
pathSum = getPathSum(map); 
print(f"Output1: {pathSum}")

path = walkPath(grid,'path')
obstSum = getObstSum(grid,path); 
print(f"Output2: {obstSum}")