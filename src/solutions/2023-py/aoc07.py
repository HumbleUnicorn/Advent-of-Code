# =============================================================================
# Ruth Wertz
# AOC 2023 - Day 7
# https://github.com/HumbleUnicorn/Advent-of-Code/blob/main/src/solutions/2023-py/aoc07.py
# =============================================================================

# =============================================================================
#  // SOLUTION OUTLINE //
# =============================================================================
#
# // PART 1 //
#
# Format data into dictionary {hand: bid}
# 
# Function to read card values
#    for hand in hands:
#        Counter: ---> return sorted counts [5], [4,1], [3,2], [3,1,1], etc.
#        Types: 5: 5K, 4: 4K, 3: FH or 3K 2: 2P or 1P, 1: HC ---> store value
#        Cards in hand: ---> store value of each caed in hane (as they appear)
#        Append list as [h, c1, c2, c3, c4, c5, key] 
#    return sorted list (by h, then c1, etc., lowest to highest)
#
# Function to calculate hand rank
#    muliplier = 1
#    for each line of values:
#        p = bid * multiplier 
#        increase multiplier by 1
#    return list of priducts    
#
# // PART 2 //
# 
# Update cLib with new card values
# 
# Update function to read card values 
#    Hand types: 
#        [5]: 5K
#        [4,1]: J>0: 5K; else 4K
#        [3,2]: J>0: 5K; else FH
#        [3,1,1]: J>0: 4K; else 3K 
#        [2,2,1]: J=2: 4K; J=1: FH; else 2P
#        [2,1,1,1]: J=>0: 3K; else 1P
#        [1,1,1,1,1]: J>0: 1P; else HC
#        
# =============================================================================

# =============================================================================
#  //INPUT DATA//
# =============================================================================

test7=[]
with open('inputs/t07.txt') as f: 
    for lines in f:
        test7.append(lines)  

day7=[]
with open('inputs/d07.txt') as f: 
    for lines in f:
        day7.append(lines) 

cLib = {'2':1, '3':2, '4':3, '5':4, '6':5, '7':6, '8':7, '9':8, 'T':9, 'J':10, 'Q':11, 'K':12, 'A':13}
wLib = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':1, 'Q':11, 'K':12, 'A':13}
hLib = {'HC':1, '1P':2, '2P':3, '3K':4, 'FH':5, '4K':6, '5K':7}

# =============================================================================
#  // DEFINE FUNCTIONS // 
# =============================================================================

from collections import Counter

def handBid(data):
    hb={}
    for lines in data:
        lines = lines.split(" ")
        hb.update({lines[0]:int(lines[1])})
    return(hb)

def handValue(hands,cLib,hLib):        
    results=[]
    for hand in hands:
        a = Counter(hand)
        c = list(a.values())
        c = sorted(c, reverse=True)
        if c[0] == 5: 
            h = hLib.get('5K')
        elif c[0] == 4:
            h = hLib.get('4K')
        elif c[0] == 3:
            if c[1] == 2:
                h = hLib.get('FH')
            else:
                h = hLib.get('3K')
        elif c[0] == 2:
            if c[1] == 2:
                h = hLib.get('2P')
            else:
                h = hLib.get('1P')
        else:
            h = hLib.get('HC')
        handVal=[h]
        for each in hand: 
            handVal.append(cLib.get(each))
        handVal.append(hand)
        results.append(handVal)
        r = sorted(results)
    return(r)

def wildValue(hands,wLib,hLib):        
    results=[]
    for hand in hands:
        a = Counter(hand)
        c = list(a.values())
        c = sorted(c, reverse=True)
        j = hand.count('J')
        if c[0] == 5:                   # [5]
            h = hLib.get('5K')
        elif c[0] == 4:                 # [4,1] J=4, J=1, J=0
            if j > 0:
                h = hLib.get('5K')
            else: 
                h = hLib.get('4K')
        elif c[0] == 3 and c[1]== 2:    # [3,2] J=3, J=2, J=0
            if j > 0:
                h = hLib.get('5K')
            else:
                h = hLib.get('FH')
        elif c[0] == 3 and c[1]== 1:    # [3,1,1] J=3, J=1, J=0
            if j > 0:
                h = hLib.get('4K')         
            else: 
                h = hLib.get('3K')  
        elif c[0] == 2 and c[1]== 2:    # [2,2,1] J=2, J=1, J=0
            if j == 2:
                h = hLib.get('4K')
            elif j == 1:
                h = hLib.get('FH')
            else:
                h = hLib.get('2P')
        elif c[0] == 2 and c[1]== 1:    # [2,1,1,1] J=2, J=1, J=0
                if j > 0:
                    h = hLib.get('3K')
                else:
                    h = hLib.get('1P')
        else:                           # [1,1,1,1,1] J=1, J=0
            if j > 0:
                h = hLib.get('1P')
            else:
                h = hLib.get('HC')
        handVal=[h]
        for each in hand: 
            handVal.append(wLib.get(each))
        handVal.append(hand)
        results.append(handVal)
        r = sorted(results)
    return(r)

def handRank(values,bids):
    w=[]
    i=1
    for line in values:
        bid = bids.get(line[6])
        w.append(i*bid)
        i+=1
    return(w)


# =============================================================================
#  // TEST OUTPUT //
# =============================================================================

bids = handBid(test7)
hands = bids.keys()

values = handValue(hands,cLib,hLib); 
ranks = handRank(values,bids)
print(sum(ranks))  
           
wValues = wildValue(hands,wLib,hLib)
wRanks = handRank(wValues,bids)  
print(sum(wRanks)) 
   
   
# =============================================================================
#   // PUZZLE OUTPUT //
# =============================================================================

bids = handBid(day7)
hands = bids.keys()

values = handValue(hands,cLib,hLib); 
ranks = handRank(values,bids)
print(sum(ranks))  

wValues = wildValue(hands,wLib,hLib)
wRanks = handRank(wValues,bids)  
print(sum(wRanks)) 