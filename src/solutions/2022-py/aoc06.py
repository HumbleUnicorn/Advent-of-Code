# Ruth Wertz
# AOC 2022 - Day 6
# https://adventofcode.com/2022/day/6


# //READ DATA//
with open('t06.txt') as f: 
    test=f.read()
    #print(test, type(test), len(test))
           
with open('d06.txt', 'r') as f: 
    day6=f.read()                   
    #print(type(day6),len(day6))                

# //FUNCTIONS//
from collections import Counter

def findMarker(run_line,seqLen):
    s=seqLen
    ds=run_line
    i=0 
    n=len(ds); 
    while i+s-1 <= n:
        c= Counter(ds[i:i+s]); 
        d=c.most_common(1)[0][1]; 
        if d == 1:
            ans=(i+s)
            break
        else:
            i+=1
    return(ans)

# //SCRIPTS//
pt1 = findMarker(test,4); print('SOLUTION PART 1:',pt1)

pt2 = findMarker(test,14); print('SOLUTION PART 2:',pt2)

pt1 = findMarker(day6,4); print('SOLUTION PART 1:',pt1)

pt2 = findMarker(day6,14); print('SOLUTION PART 2:',pt2)