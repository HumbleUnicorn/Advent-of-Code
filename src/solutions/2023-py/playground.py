import re

def find_consecutive_digits(text):
    matches = re.finditer(r'\d+', text); print(matches)
    return [(match.group(), match.start(), match.end()) for match in matches]

text = "Hello123World456"
digits = find_consecutive_digits(text)
print(digits) # Output: [('123', 5, 8), ('456', 13, 16)]

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

# import keyword

# print(keyword.kwlist)


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