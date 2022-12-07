# Ruth Wertz
# AOC 2022 - Day 2
# https://adventofcode.com/2022/day/2


# //READ TEST DATA//
'''
data=[]
with open('t02.txt') as f: 
    for lines in f:
        data.append(lines) 
print(data)
'''

   
# //READ PUZZLE DATA//
data=[]
with open('d02.txt') as f: 
    for lines in f:
        data.append(lines) 


# //SCORING FUNCTIONS//
def playRPS_part1(opp,me,i):
    score={'R':1, 'P':2, 'S':3, 'W':6, 'L':0, 'D':3}
    if me[i] == 'X':
        shapeScore = score['R']
        if opp[i] == 'A':
            matchScore = score['D']
        elif opp[i] == 'B':
            matchScore = score['L']        
        else:
            matchScore = score['W']    
    elif me[i] == 'Y':
        shapeScore = score['P']
        if opp[i] == 'A':
            matchScore = score['W']
        elif opp[i] == 'B':
            matchScore = score['D']        
        else:
            matchScore = score['L']
    else:
        shapeScore = score['S']
        if opp[i] == 'A':
            matchScore = score['L']
        elif opp[i] == 'B':
            matchScore = score['W']        
        else:
            matchScore = score['D']
    rpsScore=shapeScore+matchScore
    return(rpsScore)

def playRPS_part2(opp,me,i):
    score={'R':1, 'P':2, 'S':3, 'W':6, 'L':0, 'D':3}
    if me[i] == 'X':
        matchScore = score['L']
        if opp[i] == 'A':
            shapeScore = score['S']
        elif opp[i] == 'B':
            shapeScore = score['R']        
        else:
            shapeScore = score['P']    
    elif me[i] == 'Y':
        matchScore = score['D']
        if opp[i] == 'A':
            shapeScore = score['R']
        elif opp[i] == 'B':
            shapeScore = score['P']        
        else:
            shapeScore = score['S']
    else:
        matchScore = score['W']
        if opp[i] == 'A':
            shapeScore = score['P']
        elif opp[i] == 'B':
            shapeScore = score['S']        
        else:
            shapeScore = score['R']
    rpsScore=shapeScore+matchScore
    return(rpsScore)

# //PARSE DATA INTO "ME" and "OPP" LISTS//
n=len(data)
i=0
opp=[]
me=[]
for i in range(n):
    opp.append(data[i][0])
    me.append(data[i][2])     
#print(opp,me)    

# //RUN & STORE SCORING FUNCTION//
i=0
rps=[]
for i in range(n):
    rps.append(playRPS_part1(opp,me,i))
#print(rps)      
print('SOLUTION PART 1:',sum(rps))

i=0
rps=[]
for i in range(n):
    rps.append(playRPS_part2(opp,me,i))
#print(rps)      
print('SOLUTION PART 2:',sum(rps))
