# Ruth Wertz
# AOC 2022 - Day 5
# https://adventofcode.com/2022/day/5


# //READ DATA//

with open('t05a.txt') as f: 
    testA=[]
    for lines in f: 
        testA.append(lines.replace('\n',''))
 
with open('t05b.txt') as f: 
    testB=[]
    for lines in f: 
        testB.append(lines.replace('\n',''))   
          
with open('d05a.txt') as f:                 #Includes only lines of crate arrangment
    day5A=[]
    for lines in f:
        day5A.append(lines.replace('\n',''))

with open('d05b.txt') as f:                 #Includes only lines of move instructions 
    day5B=[]
    for lines in f:
        day5B.append(lines.replace('\n',''))        

def parseStacks(run_data):   
    d=run_data                              #assign input data
    n=len(d)                                #number of lines in 'd'
    m=len(d[0])                             #number of bits per line in 'd'
    col=1                                   #crate column counter iterator
    S={}                                    #dict of {stackName:crateList}
    s=[]                                    #list of keys
    while col <= m-1: 
        row=n-1                             #row counter iterator
        cL=[]                               #list of crates in stack 's'
        while row>=0:
            if row == n-1:                  #last row contains stackName
                sN=str(d[row][col])
            elif d[row][col] != ' ':        #every other row contains Crates
                cL=cL+list(d[row][col])
            row-=1
        stack={sN:cL}                   
        S.update(stack)                     #S={'sN':[cL], 'sN':[CL], ...}
        s.append(sN)                        #s=['sN','sN'...] keys only
        col+=4 
    return[S,s]

def parseMoveInst(run_data):
    moves=run_data
    moveInst=[] 
    for i in range(len(moves)):       
        m = moves[i].split(" ")
        m = [int(m[1]),m[3],m[5]]
        moveInst.append(m)
    return(moveInst)

def moveCrate(move,stackDict): 
    stackDict=S
    n=move[0]
    f=move[1]
    t=move[2]
    for i in range(n):
        m=len(S[f])-1
        S[t].append(S[f][m])
        S[f].pop(m)
    return

def moveCrate9001(move,stackDict): 
    stackDict=S
    n=move[0]
    f=move[1]
    t=move[2]
    m=len(S[f])-n
    for i in range(n):
        S[t].append(S[f][m+i])
    for i in range(n):
        S[f].pop()
    return

# //PART 1 WITH PUZZLE DATA//
S=parseStacks(day5A)[0]             #Dictionary {stackName:crateList}
s=parseStacks(day5A)[1]             #List of keys
moveInst=parseMoveInst(day5B)       #[int(n), fromName(f), toName(t)]
       
top=str()  
for move in moveInst:               #execute moves 
    moveCrate(move,S)
    #print(S)
for name in s:
    n = len(S[name])-1              #identify top crates in each stack
    top=top+str(S[name][n])                 
print('SOLUTION PART 1:',top)


# //PART 2 WITH PUZZLE DATA//
S=parseStacks(day5A)[0]             #Dictionary {stackName:crateList}
s=parseStacks(day5A)[1]             #List of keys
moveInst=parseMoveInst(day5B)       #[int(n), fromName(f), toName(t)]
      
top=str()  
for move in moveInst:               #execute moves 
    moveCrate9001(move,S)
    #print(S)
for name in s:
    n = len(S[name])-1              #identify top crates in each stack
    top=top+str(S[name][n])                          
print('SOLUTION PART 2:',top)






    


    





