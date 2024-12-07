import math

# page ordering rules:
data = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13'''

# pages to produce in each update:
pages = '''75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''

def data_cleanup(data_list, delimiter): # delimiter="," -> default (named parameter)
    rules = []
    for entry in data_list:
        rule = entry.split(delimiter) 
        rules.append(rule)
    return rules

def string_to_int(lst):
    int_lst = []
    for i in range(len(lst)):
        integer_line = []
        for j in range(len(lst[i])):
            j = int(lst[i][j])
            integer_line.append(j)
        int_lst.append(integer_line)
    return int_lst

# Clean up the given input 
data = data.splitlines()  
data = data_cleanup(data, "|")  # [['47', '53'], ['97', '13'], ['97', '61'], ...]
rules = string_to_int(data) # Create a list of rules from "data" and convert String to Int

pages = pages.splitlines()  
pages = data_cleanup(pages, ",")
pages = string_to_int(pages)

# Merge rules lists with the same first number

dict_grouped_rules = {}

# Process each rule
for rule in rules:
    first_page = rule[0]
    if first_page not in dict_grouped_rules:
        dict_grouped_rules[first_page] = []
    dict_grouped_rules[first_page].append(rule[1])

# Check if pages follow rules

correct_pages = []

for page in pages:
    #print(f"Checking page sequence: {page}")
    state = "Correct"

    for i in range(len(page)-1):
        # For the current page, check if the next page is in the rule
        if page[i+1] in dict_grouped_rules.get(page[i], []):
            pass
        else:
            state = "Incorrect"

    if state == "Correct":
        correct_pages.append(page)

# print(correct_pages)

# Problem: the last entry in the sublists of correct_pages is not printet -> we are of by one

# find the middle entry of each sublist

def find_middle(lst):
    lst_len = len(lst)+1 # because correct_pages (lst) is of by one
    middle = lst_len / 2
    return math.ceil(middle) # this is the middle of the sublist


middle_numbers_lst = []

for i in range(len(correct_pages)):
    location = find_middle(correct_pages[i]) - 1 # because of by one when counting through list
    middle_number = correct_pages[i][location]
    middle_numbers_lst.append(middle_number)

print(sum(middle_numbers_lst))

