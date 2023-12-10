# Ruth Wertz
# AOC 2022 - Day 1
# https://adventofcode.com/2022/day/1

'''
# //READ TEST DATA//'

data=[]
with open('t01.txt') as f: 
    for lines in f:
        data.append(lines) 
'''
       
# //READ PUZZLE DATA//
data=[]
with open('d01.txt') as f: 
    for lines in f:
        data.append(lines)            


# Convert lines from 'str' to 'int'
n=len(data)
i=0
for i in range(n):
    if data[i] == '\n':
        data[i] = int(0)
    else: 
        data[i] = int(data[i])
    i+=1
if data[n-1]!=0:                            #Append '0' to satify 'else'  
    data.append(0)                          #Condition for last elf


# Parse values to calories carried per elf     

#Initial Values
n=len(data)   
i=0             #loop iterator
j=0             #elf number counter 
cal=0           #calories carried counter


#Define Elf Attributes
from collections import namedtuple
elf = namedtuple('elf', ['elfNo','calCarried'])
elves = []


#Generate and Sort 'elf' Instantiates 
for i in range(n):                          #repeat loop 'n' number of times
    if data[i]>0:                           #IF list item > 0 
        cal+=data[i]                        #THEN add val to 'cal' sum
    else:                                   #ELSE 
        elves.append(elf(str(j+1),cal))     #Append 'elfNo' and 'calCarried'      
        j+=1                                #Add 1 to elf counter
        cal=0                               #Reset calorie counter to 0
    i+=1                                    #Add 1 to loop iterator

elves.sort(key=lambda x: getattr(x,'calCarried'), reverse=True)


# //PART 1: Max Cal Carried By Single Elf
maxCalCarried = elves[0]
maxCal=maxCalCarried.calCarried
elfNo=maxCalCarried.elfNo

print('SOLUTION PART 1:',maxCal,'cal, Elf No',elfNo)                         


# //PART 2: Max Cal Carried By Sum of Three Elves
maxCalCarried = elves[:3]
maxCal=[]
elfNo=[]

m=len(maxCalCarried)
for i in range (m):
    elfTemp = maxCalCarried[i]
    maxCal.append(elfTemp.calCarried)
    elfNo.append(elfTemp.elfNo)

print('SOLUTION PART 2:',sum(maxCal),'cal, Elf No',elfNo)      

