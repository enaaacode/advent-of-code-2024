# Input = One report per line. Each report is a list of numbers called levels.
input = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''

# 1. Split lines
# result = ['7 6 4 2 1  ', '1 2 7 8 9  ', '9 7 6 2 1  ', '1 3 2 4 5  ', '8 6 4 4 1  ', '1 3 6 7 9  ']
input = input.splitlines()


# 2. Split levels
# result = [['7', '6', '4', '2', '1'], ['1', '2', '7', '8', '9'], ['9', '7', '6', '2', '1'], ['1', '3', '2', '4', '5'], ['8', '6', '4', '4', '1'], ['1', '3', '6', '7', '9']]
split_levels = []

for i in range(len(input)):
    level = input[i].split()
    split_levels.append(level)

# Convert String to Int
# result = [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]

integer_list = []

for report in split_levels:
    integer_line = []
    for entry in report:
        entry = int(entry)
        integer_line.append(entry)
    integer_list.append(integer_line)

# Check if each report is safe. A report is safe if:
# 1. The levels are either all increasing or all decreasing.
# 2. Two neighboring levels differ by 1–3 

def distance(x,y):
    return (x-y)

def distance_abs(x,y):
    return abs(x-y)

# Create a list with the differences, e.g. [-2, -2, 0, -3]
differ_list = []

for i in range(len(integer_list)):
    differ_single = []

    for j in range(len(integer_list[i]) - 1): 
        calc = distance(integer_list[i][j+1], integer_list[i][j])
        differ_single.append(calc)

    differ_list.append(differ_single)  

# Check rule 2. Two neighboring levels differ by 1–3 

rule2_list = []

for i in range(len(differ_list)):
    rule2_single = []

    for j in range(len(differ_list[i])):
        if abs(differ_list[i][j]) < 4:
            result = "ok"
        else:
            result = "false"
        rule2_single.append(result)

    rule2_list.append(rule2_single)

# Check rule 1: if all numbers in one report are increasing or decreasing

rule1_list = []

for i in range(len(differ_list)):
    rule1_single = []

    for j in range(len(differ_list[i])):
        if differ_list[i][j] < 0:
            result = "decrease"
        elif differ_list[i][j] > 0:
            result = "increase"
        else:
            result = "Zero"

        rule1_single.append(result)

    rule1_list.append(rule1_single)

# Check both lists

safe_list = []

for i in range(len(rule1_list)): 
    single_safe_list = []
    for j in range(len(rule1_list[i])):
        first_entry_rule1 = rule1_list[i][0]
        first_entry_rule2 = "ok"

        if rule1_list[i][j] == first_entry_rule1 and first_entry_rule1 != "Zero" and rule2_list[i][j] == first_entry_rule2:
            result = "safe"
            single_safe_list.append(result)
        else:
            result = "unsafe"
            single_safe_list.append(result)

    safe_list.append(single_safe_list)

final_safe_list = []

for i in range(len(safe_list)): 
    safe_check = True

    for j in range(len(safe_list[i])):
        if safe_list[i][j] != "safe":
            safe_check = False
    
    final_safe_list.append(safe_check)

final_result = final_safe_list.count(True)

print(final_result)
