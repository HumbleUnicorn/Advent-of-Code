# Ruth Wertz
# AOC 2022 - Day 1
# https://adventofcode.com/2022/day/1


# //READ TEST DATA//
data=[]
with open('day1test22.txt') as f: 
    for lines in f:
        data.append(lines)

# //TRANSFORM TEST DATA FROM STRINGS TO INTEGERS//
n=len(data)
i=0
while i<n:
    if data[i] == '\n':
        data[i] = int(0)
    else: 
        data[i] = int(data[i])
    i+=1

# //PARSING TEST VALUES BY ELF//            
n=len(data) 
i=0         #loop iterator
j=0         #elf counter where 'Elf No. 1' = print('Elf No.',j+1)
cal=0       #calorie counter
elf=[]      #create empty list that will contain the calories carried per elf

while i<n:                          #repeat loop 'n' times         
    if data[i]>0:                   #when list item >0            
        cal+=data[i]                #sum item with stored 'cal' value 
    else:                           #when list item == 0
        elf.append(cal)             #append stored value of 'cal' to list 'elf' 
        if elf[j]==max(elf):        #when 'cal' value is the list maximum
            elfNo = j+1             #store elfID      
            maxCal = cal            #store 'cal' value    
        j+=1                        #add 1 to elf counter
        cal=0                       #reset cal counter
    i+=1                            #add 1 to loop iterator
     
print('TEST:',maxCal,'calories is carried by Elf No.',elfNo)
      

# //READ PUZZLE DATA//
data=[]
with open('day1data22.txt') as f: 
    for lines in f:
        data.append(lines)

# //TRANSFORM PUZZLE DATA FROM STRINGS TO INTEGERS//
n=len(data)
i=0
while i<n:
    if data[i] == '\n':
        data[i] = int(0)
    else: 
        data[i] = int(data[i])
    i+=1

# //PARSING PUZZLE VALUES BY ELF//            
n=len(data) 
i=0         #loop iterator
j=0         #elf counter where 'Elf No. 1' = print('Elf No.',j+1)
cal=0       #calorie counter
elf=[]      #create empty list that will contain the calories carried per elf

while i<n:                          #repeat loop 'n' times         
    if data[i]>0:                   #when list item >0            
        cal+=data[i]                #sum item with stored 'cal' value 
    else:                           #when list item == 0
        elf.append(cal)             #append stored value of 'cal' to list 'elf' 
        if elf[j]==max(elf):        #when 'cal' value is the list maximum
            elfNo = j+1             #store elfID      
            maxCal = cal            #store 'cal' value    
        j+=1                        #add 1 to elf counter
        cal=0                       #reset cal counter
    i+=1                            #add 1 to loop iterator 
     
print('PART 1:',maxCal,'calories is carried by Elf No.',elfNo)     

# //PART 2//
m=len(elf)
elf.sort()
max3cal=(elf[m-1],elf[m-2],elf[m-3])
print('PART 2:',sum(max3cal),'calories is carreid by the top 3 elves')

    

  

        
        
        



