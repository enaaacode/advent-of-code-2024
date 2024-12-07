# - - - - - - - - - - - - - - PART ONE (of two) - - - - - - - - - - - - - - 

input = '''3   4
4   3
2   5
1   3
3   9
3   3
'''
input = input.split()

# Convert String to Int
integer_list = []

for s in input:
    integer_list.append(int(s))

# Make two new lists

input_list_one = integer_list[0::2] # every 2th item, starting from the 1rd item
input_list_two = integer_list[1::2] # every 2th item starting from the 2th item

list_len = len(input_list_one)

# Sort lists in ascending order

list_one = sorted(input_list_one)
list_two = sorted(input_list_two)

# Form pairs of the smallest numbers from both lists

paired_list = []

for i in range(list_len):
    pair = list_one[i], list_two[i];
    paired_list.append(pair)

# Calculate the difference between the pairs

def distance(x,y):
    return abs(x-y)
# not mine, source: stackoverflow

calc_differences = []

for i in range(list_len):
    calc = distance(paired_list[i][0], paired_list[i][1]);
    calc_differences.append(calc)

# Form the sum 

sum_list = sum(calc_differences)

print(sum_list)

# - - - - - - - - - - - - - - PART TWO - - - - - - - - - - - - - - 

# Figure out how often each number from the left list appears in the right list

import math

# Find out frequency of entries

freq_list = []

for i in range(len(list_two)):
    count = list_two.count(list_one[i])
    freq_list.append(count)

# Form pairs: entry and frequency of entry

paired_freq_list = []

for i in range(len(list_two)):
    pair = list_one[i], freq_list[i];
    paired_freq_list.append(pair)

# Multiply entry and frequency of entry (similarity score)

sim_score_list = []

for entry in paired_freq_list:
    #calc = math.prod([entry[0], entry[1]])
    calc = entry[0] * entry[1]
    sim_score_list.append(calc)

# Form the sum 

sum_score = sum(sim_score_list)

print(sum_score)
