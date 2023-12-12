# =============================================================================
# Ruth Wertz
# AOC 2023 - Day 2
# https://github.com/HumbleUnicorn/Advent-of-Code/blob/main/src/solutions/2023-py/aoc02.py
# =============================================================================


# =============================================================================
# Part 1 Outline
#
# define limits: rMax,gMax,bMax,sumMax
# for game in gameData:
#    parse to [game id, [str], [str], etc.]
# for game in gameData:
#    parse to [game id, [r,g,b,sum], [r,g,b,sum], etc.]
# for game in gameData:
#    read Trial return True if possible, False if not
#   
# 
# Part 2 Outline
#
# for line in data
#     find first digit **or str('digit')** in line
#         store as str
#     find last digit **or str('digit')** in line
#         store as string
#     define num as str(first+last)
#         append to list as int(str)
# sum list
#     print sum
# =============================================================================


# =============================================================================
#  //INPUT DATA//
# =============================================================================

day2=[]
with open('inputs/d02.txt') as f: 
    for lines in f:
        day2.append(lines) 
        
test2=['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n',
        'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n',
        'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n',
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n',
        'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']


lim1 = [12,13,14,sum([13,14,15])]


# =============================================================================
#  // DEFINE FUNCTIONS // 
# =============================================================================

def gameLog(data):
    gl = []
    for game in data:
        game = game.replace('Game ','')
        game = game.replace(':', ';')
        game = game.replace('\n','') 
        game = game.split(';')
        game[0] = int(game[0])
        gl.append(game)     
    for game in gl:
        for i in range(len(game)): 
            trial = game[i]
            if type(trial) == str:
                game.pop(i)
                trial = trial.split(',')
                game.insert(i, trial)
        for i in range(1,len(game)):
            trial = game[i]
            n = len(trial)
            for j in range(n):
                cubes = trial[j]
                trial.pop(j)
                cubes = cubes.strip()
                trial.insert(j, cubes)
    return(gl)

def gameCounts(gameData):
    gc = []
    for game in gameData:
        gID = game[0]
        trials = [gID]
        for i in range(1,len(game)):
            trial = game[i]
            r = 0
            g = 0
            b = 0
            for j in range(len(trial)):
                c = trial[j]
                c = c.strip()
                if 'red' in c:
                    c = c.replace(' red','')
                    r = int(c)
                if 'green' in c:
                    c = c.replace(' green','')
                    g = int(c)
                if 'blue' in c:
                    c = c.replace(' blue','')
                    b = int(c)
                s = r + g + b
            trials.append([r,g,b,s])
        gc.append(trials)
    return(gc)

def gamesPossible(gameLimits,gameData): 
    gp = []
    gIDs = []
    rMax = gameLimits[0]
    gMax = gameLimits[1]
    bMax = gameLimits[2]
    sMax = gameLimits[3]
    for game in gameData:
        gID = game[0]
        log = [gID]
        for i in range(1, len(game)):
            trial = game[i]
            r = trial[0]
            g = trial[1]
            b = trial[2]
            s = trial[3]
            if r<=rMax and g<=gMax and b<=bMax and s<=sMax:
                log.append(True)
            else:
                log.append(False)
        gp.append(log)
    for game in gp:
        if game.count(False) > 0:
            next
        else:
            gIDs.append(game[0])
    return(gIDs)

def minPossible(gameData):
    power = []
    for game in gameData:
        r = 0
        g = 0
        b = 0
        for i in range(1,len(game)):
            trial = game[i]
            rT = trial[0]
            gT = trial[1]
            bT = trial[2]
            if rT > r:
                r = rT
            if gT > g:
                g = gT
            if bT > b:
                b = bT
        power.append(r*g*b)
    return(power)
        
 
# =============================================================================
#  // TEST OUTPUT //
# =============================================================================

gLog = gameLog(test2)
# for game in gLog:
#     print(game)  

gCounts = gameCounts(gLog)
# for game in gCounts:
#     print(game)

gIDs = gamesPossible(lim1,gCounts)
# for game in gIDs:
#     print(game)
    
print(f'Test Part 1 - Sum of Possible Games = {sum(gIDs)}')

gPower = minPossible(gCounts)
# for game in gPower:
#     print(game)
print(f'Test Part 2 - Sum of Possible Games = {sum(gPower)}')

# =============================================================================
#  // PUZZLE OUTPUT //
# =============================================================================

gLog = gameLog(day2)
# for game in gLog:
#     print(game)  

gCounts = gameCounts(gLog)
# for game in gCounts:
#     print(game)

gIDs = gamesPossible(lim1,gCounts)
# for game in gIDs:
#     print(game)
    
print(f'Part 1 - Sum of Possible Games = {sum(gIDs)}')

gPower = minPossible(gCounts)
# for game in gPower:
#     print(game)
print(f'Test Part 2 - Sum of Possible Games = {sum(gPower)}')