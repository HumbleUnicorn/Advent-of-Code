# # ============================================
# # find consecutive digits in a string

# import re

# def find_consecutive_digits(text):
#     matches = re.finditer(r'\d+', text); print(matches)
#     return [(match.group(), match.start(), match.end()) for match in matches]

# text = "Hello123World456"
# digits = find_consecutive_digits(text)
# print(digits) # Output: [('123', 5, 8), ('456', 13, 16)]

# # ============================================
# # find non-alphanumeric characters in a string
# import re

# def find_non_alphanumeric(text):
#     # The pattern \W matches any non-alphanumeric character
#     matches = re.finditer(r'\W', text)
#     return [(match.group(), match.start()) for match in matches]

# text = "Hello...W@rld...123"
# symbols = find_non_alphanumeric(text)
# for sym in symbols:
#     if sym[0] != '.':
#         print(sym[1])

# print(symbols)  # Output: [(',', 5,), (' ', 6), (' ', 13), ('!', 18)]

# # ============================================
# # check python keywords

# import keyword
# print(keyword.kwlist)

# # ============================================
# # find the common values between two lists

# from collections import Counter

# def find_common_values(list1, list2):
#     counter1 = Counter(list1)
#     counter2 = Counter(list2)
#     common = counter1 & counter2
#     return list(common.elements())

# set1 = [0, 1, 2, 4, 5]
# set2 = [2, 3, 4]
# common_values = find_common_values(set1, set2)
# print(common_values)  # Output: [2, 4]

# score = (len(common_values)) ** 2; print(score)

# # ============================================
# # create a dictionary from two lists
# test = [[50,98,2],[52,50,48]]
# src = []
# dst = []
# for line in test:
#     src += list(range(line[1],line[1]+line[2]))
#     dst += list(range(line[0],line[0]+line[2]))

# map1 = dict(zip(src, dst))
# print(map1) 

# # ============================================
# # check id a string contains a digit
# def contains_digits(s):
#     return any(character.isdigit() for character in s)

# s = "Hello123"
# print(contains_digits(s)) 


str_list = ['1', '2', '3']
int_list = list(map(int, str_list))
print(int_list)  # Output: [1, 2, 3]

s = "Hello\nWorld\n"
s = s.replace('\n', '')
print(s)  # Output: HelloWorld

s = 'seeds: 79 14 55 13\n, \n, seed-to-soil map:\n, 50 98 2\n, 52 50 48\n, \n, soil-to-fertilizer map:\n, 0 15 37\n, 37 52 2\n, 39 0 15\n, \n, fertilizer-to-water map:\n, 49 53 8\n, 0 11 42\n, 42 0 7\n, 57 7 4\n, \n, water-to-light map:\n, 88 18 7\n, 18 25 70\n, \n, light-to-temperature map:\n, 45 77 23\n, 81 45 19\n, 68 64 13\n, \n, temperature-to-humidity map:\n, 0 69 1\n, 1 0 69\n, \n, humidity-to-location map:\n, 60 56 37\n, 56 93 4'
s = s.replace(', \n,', '*')
print(s)
