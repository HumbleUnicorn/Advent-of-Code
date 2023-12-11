# Ruth Wertz
# AOC 2023 - Day 2
# https://github.com/HumbleUnicorn/Advent-of-Code/blob/main/src/solutions/2023-py/aoc02.py


# //INPUT DATA//
day2=[]
with open('inputs/d02.txt') as f: 
    for lines in f:
        day2.append(lines) 
        
test2a=['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n','Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue\n',
        'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red\n',
        'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red\n',
        'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

#for lines in test2a:
#    print(lines)
#for lines in day2:
#    print(lines)

cntMax = [12,13,14,sum([13,14,15])]

# // DEFINE FUNCTIONS // 

def games(data):
    games=[]
    for line in data:
        game = line.replace('Game ','')
        game = game.replace(' ','')
        game = game.replace(':', ';')
        game = game.replace('\n','')
        game = game.split(';'); 
        games.append(game)
    return(games)

def gameLog(games):
    gLog=[]
    for game in games:
        gID = int(game[0])
        tNo = len(game)-1
        gLog.append([gID, tNo])
    return(gLog)

def gameTrials(games):
    trials=[]
    for game in games:
        n = len(game)
        gID = int(game[0])
        for i in range(1,n):
            tID=i
            trial = game[i]
            trials.append([gID,tID,trial])
    return(trials)   

def trialPulls(trials):
    pulls=[]
    for trial in trials:
        gID = trial[0]
        tID = trial[1]
        p = trial[2]
        p = p.split(',')
        pull = [gID,tID,p]
        pulls.append(pull) 
    return(pulls)
                
def pullCounts(pulls):
    counts=[]
    for pull in pulls: 
        gID = pull[0]
        tID = pull[1]
        pCnts = pull[2]
        for cnt in pCnts:
            r = 0
            g = 0
            b = 0
            if 'red' in cnt:
                r = cnt.replace('red','')
                r = int(r)
            elif 'green' in cnt:
                g = cnt.replace('green','')
                g = int(g)
            elif 'blue' in cnt:
                b = cnt.replace('blue','')
                b = int(b)
            s = r + g + b
            count = [gID, tID, r, g, b, s]
            counts.append(count)
    return(counts)

def trialCounts(n,m,counts):
    tCounts=[]
    for i in range(n):
        for j in range(m):
            gID = i+1
            tID = j+1
            r = 0
            g = 0
            b = 0
            s = 0
            for n in counts:
                if n[0] == gID and n[1] == tID:
                    r += n[2]
                    g += n[3]
                    b += n[4]
                    s += n[5]
            tSums = [gID,tID,r,g,b,s]
            tCounts.append(tSums)
    return(tCounts)

def trialsPossible(n,cntMax,tCounts):
    tPoss = []
    rMax = cntMax[0]
    gMax = cntMax[1]
    bMax = cntMax[2]
    sMax = cntMax[3]
    for i in range(n):
        poss = [i+1]
        for line in tCounts:
            gID = line[0]
            r = line[2]
            g = line[3]
            b = line[4]
            s = line[5]
            if gID == i+1 and s > 0:
                if r<=rMax and g<=gMax and b<=bMax and s<=sMax:
                    poss.append(True)
                else:
                    poss.append(False)
        tPoss.append(poss)
    return(tPoss)

def gamesPossible(tPoss):
    gPoss = []
    for line in tPoss:
        if line.count(False) > 0:
            next
        else:
            gPoss.append(line[0])   
    return(gPoss)

'''        
# // TEST OUTPUT //

games = games(test2a)
#for game in games:
    #print(game)  

gLog = gameLog(games)
#for line in gLog:
    #print(line)

n = 0 #max game number
m = 0 #max trials per game    
for log in gLog:
    if log[0] > n:
        n = log[0]
    if log[1] > m:
        m = log[1]
    
trials = gameTrials(games)
#for trial in trials:
    #print(trial)

pulls = trialPulls(trials)
#for pull in pulls:
    #print(pull) 

counts = pullCounts(pulls)
#for count in counts:
    #print(count)

tCounts = trialCounts(n,m,counts)
#for line in tCounts:
    #print(line)
    
tPoss = trialsPossible(n,cntMax,tCounts)
#for line in tPoss:
    #print(line)  

gPoss = gamesPossible(tPoss)
#print(gPoss)
print(f'Test Part 1 - Sum of Possible Games = {sum(gPoss)}')
'''

# // PUZZLE OUTPUT //   
            
games = games(day2)
#for game in games:
    #print(game)  

gLog = gameLog(games)
#for line in gLog:
    #print(line)

n = 0 #max game number
m = 0 #max trials per game    
for log in gLog:
    if log[0] > n:
        n = log[0]
    if log[1] > m:
        m = log[1]
    
trials = gameTrials(games)
#for trial in trials:
    #print(trial)

pulls = trialPulls(trials)
#for pull in pulls:
    #print(pull) 

counts = pullCounts(pulls)
#for count in counts:
    #print(count)

tCounts = trialCounts(n,m,counts)
#for line in tCounts:
    #print(line)
    
tPoss = trialsPossible(n,cntMax,tCounts)
#for line in tPoss:
    #print(line)  

gPoss = gamesPossible(tPoss)
#print(gPoss)
print(f'Part 1 - Sum of Possible Games = {sum(gPoss)}')    
                    
            
    

    





   
    
        
        
        
    
    
        
        

            
            
    

    