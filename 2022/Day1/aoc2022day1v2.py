# Ruth Wertz
# AOC 2022 - Day 1
# https://adventofcode.com/2022/day/1


# //SOLUTION WITH TEST DATA//

test=[]
with open('day1test22.txt') as f: 
    for lines in f:
        test.append(lines)

# Read data and convert lines to int
n=len(test)
i=0
for i in range(n):
    if test[i] == '\n':
        test[i] = int(0)
    else: 
        test[i] = int(test[i])
    i+=1
if test[n-1]!=0:                            #Append '0' to satify 'else'  
    test.append(0)                          #Condition for last elf


# Parse values to calories carried per elf     

#Initial Values
n=len(test)   
i=0             #loop iterator
j=0             #elf number counter 
cal=0           #calories carried counter


#Define Elf Attributes
from collections import namedtuple
elf = namedtuple('elf', ['elfNo','calCarried'])
testElves = []


#Generate instantiates 
for i in range(n):                          #repeat loop 'n' number of times
    if test[i]>0:                           #IF list item > 0 
        cal+=test[i]                        #THEN add val to 'cal' sum
    else:                                   #ELSE 
        testElves.append(elf(str(j+1),cal)) #Append 'elfNo' and 'calCarried'      
        j+=1                                #Add 1 to elf counter
        cal=0                               #Reset calorie counter to 0
    i+=1                                    #Add 1 to loop iterator

#Sort and Display Results
testElves.sort(key=lambda x: getattr(x,'calCarried'), reverse=True)
testMaxCalCarried = testElves[0]
print('TEST PART 1:',testMaxCalCarried)


# PART 2: Summing Calories Carried For Top Three Elves
testMaxCal=[]
testElfNo=[]
testMaxCalCarried = testElves[:3]
m=len(testMaxCalCarried)
for i in range (m):
    elf = testMaxCalCarried[i]
    testMaxCal.append(elf.calCarried)
    testElfNo.append(elf.elfNo)
print('TEST PART 2:',sum(testMaxCal),'cal, Elf No',testElfNo)
    

# //SOLUTION WITH PUZZLE DATA//

data=[]
with open('day1data22.txt') as f: 
    for lines in f:
        data.append(lines)

# Read data and convert lines to int
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


#Generate instantiates 
for i in range(n):                          #repeat loop 'n' number of times
    if data[i]>0:                           #IF list item > 0 
        cal+=data[i]                        #THEN add val to 'cal' sum
    else:                                   #ELSE 
        elves.append(elf(str(j+1),cal))     #Append 'elfNo' and 'calCarried'      
        j+=1                                #Add 1 to elf counter
        cal=0                               #Reset calorie counter to 0
    i+=1                                    #Add 1 to loop iterator

#Sort and Display Results
elves.sort(key=lambda x: getattr(x,'calCarried'), reverse=True)
maxCalCarried = elves[0]
print('SOLUTION PART 1:',maxCalCarried)                         #Result: 69177


# PART 2: Summing Calories Carried For Top Three Elves
maxCal=[]
elfNo=[]
maxCalCarried = elves[:3]
m=len(maxCalCarried)
for i in range (m):
    elf = maxCalCarried[i]
    maxCal.append(elf.calCarried)
    elfNo.append(elf.elfNo)
print('SOLUTION PART 2:',sum(maxCal),'cal, Elf No',elfNo)      #Result: 207456

