# Ruth Wertz
# AOC 2022 - Day 4
# https://adventofcode.com/2022/day/4


# //READ DATA//
with open('t04.txt') as f: 
    test=[]
    for lines in f: 
        test.append(lines.replace('\n',''))       
           
with open('d04.txt') as f: 
    day4=[]
    for lines in f:
        day4.append(lines.replace('\n',''))

#print(test)
#print(type(test),len(test))
#print(test[0],type(test[0]),len(test[0]))
#print(test[0][0],type(test[0][0]),len(test[0][0]))

# //FIND CONTAINED SETS AND OVERLAP//
def findOverlap(run_data):
    cnt=0
    ovr=0
    for line in run_data:
        pair=line.split(',')
        pair1=list(range(int((pair[0].split('-'))[0]),int((pair[0].split('-'))[1])+1))
        pair2=list(range(int((pair[1].split('-'))[0]),int((pair[1].split('-'))[1])+1))
        pairSet = set(list(pair1+pair2))
        a=len(pair1)    
        b=len(pair2)
        c=len(pairSet)
        if c == max(a,b):
            cnt+=1
        if c < a+b:
            ovr+=1
        results=[cnt,ovr]
    return(results)
    
# //RUN WITH TEST AND PUZZLE DATA//
testSol=findOverlap(test)
day4Sol=findOverlap(day4)

print('Test1 ===>',testSol[0])
print('SOULTION PART 1 ===>',day4Sol[0])

print('Test2 ===>',testSol[1])
print('SOULTION PART 1 ===>',day4Sol[1])