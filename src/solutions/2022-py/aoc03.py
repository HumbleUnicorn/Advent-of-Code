# Ruth Wertz
# AOC 2022 - Day 3
# https://adventofcode.com/2022/day/3


# //PART 1: FUNCTIONS//
with open('t03.txt') as f: 
    test=[]
    for lines in f: 
        test.append(lines.replace('\n','')) 

with open('d03.txt') as f: 
    day3=[]
    for lines in f:
        day3.append(lines.replace('\n',''))

from collections import Counter

def parseMe(sack):
    n=len(sack)
    a=sack[:int(n/2)]
    b=sack[int(n/2):int(n)]
    return [a,b]

def findCommon(set1,set2):
    a=Counter(set1)
    b=Counter(set2)
    common=a & b
    char=list(common.items())
    return char[0][0]

def findPriority(item):
    a='0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    b=a.find(item)
    return int(b)


# //PART 1: RUN SOLUTION//
# sacks = test ===> Result = 157 
sacks = day3
commonItems=[]
priority=0
for sack in sacks:
    s=parseMe(sack)   
    set1=s[0]
    set2=s[1]
    c=findCommon(set1,set2)
    commonItems.append(c)
    #print(commonItems)
for item in commonItems:
    p=findPriority(item)
    priority+=p
print('PART 1 SOLUTION:',priority)


# //PART 2: FUNCTIONS//
def setGroups(sacks,i):
    a=sacks[i]
    b=sacks[i+1]
    c=sacks[i+2]
    return[a,b,c]

def findCommonGroup(sack1,sack2,sack3):
    a=Counter(sack1)
    b=Counter(sack2)
    c=Counter(sack3)
    common=a & b & c
    char=list(common.items())
    return char[0][0]    


# //PART 2: RUN SOLUTION//
# sacks = test ===> Result = 70
sacks = day3
commonItems=[]
priority=0
i=0
while i < len(sacks):
    s=setGroups(sacks,i)
    sack1=s[0]
    sack2=s[1]
    sack3=s[2]
    c=findCommonGroup(sack1,sack2,sack3)
    commonItems.append(c)
    i+=3
for item in commonItems:
    p=findPriority(item)
    priority+=p
print('PART 2 SOLUTION:',priority)   


