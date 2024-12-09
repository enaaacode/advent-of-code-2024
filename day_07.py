from pprint import pprint
from itertools import product

data = '''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
'''

# process data
data = data.splitlines()

data_lst = []
for line in data:
    line = line.replace(":", "")
    sublist = line.split(" ")
    integer_lst = [int(number) for number in sublist]
    data_lst.append(integer_lst)
data = data_lst

my_dict = {}
for line in data:
    key = line[0]
    values = line[1:]
    my_dict[key] = values

# - - - - - - - funcition - - - - - - -

def get_all_operators(value): 
    n = len(value) - 1  
    return list(product("+*", repeat=n))

# - - - - - - - code it - - - - - - -

right_results_lst = []

for key, value in my_dict.items():
    operators_list = get_all_operators(value)  

    '''print(f"Key: {key}, Values: {value}")
    print(f"Operators: {operators_list}")
    print(f"This are {len(operators_list)} calculations.")'''

    for operators in operators_list:
        result = value[0]

        for i in range(len(operators)): # for i, op in enumerate(operators):
            op = operators[i]
            
            if op == "+":
                result += value[i+1]
            elif op == "*":
                result *= value[i+1]

        # check if one of the calculated results is right (key). If so put it in the list right_results_lst
        if result == key:
            if key not in right_results_lst:
                right_results_lst.append(key)
            else:
                pass


print(sum(right_results_lst))

# - - - - - - - PART TWO - - - - - - -

def get_all_operators(value): 
    n = len(value) - 1  
    return list(product("+*/", repeat=n))

# - - - - - - - code it - - - - - - -

right_results_lst = []

for key, value in my_dict.items():
    operators_list = get_all_operators(value)  

    for operators in operators_list:
        result = value[0]

        for i in range(len(operators)): 
            op = operators[i]
 
            if op == "+":
                result += value[i+1]
            if op == "*":
                result *= value[i+1]
            if op == "/":
                result = int(str(result)+str(value[i+1]))
                
        # check if one of the calculated results is right (key). If so put it in the list right_results_lst
        if result == key:
            if key not in right_results_lst:
                right_results_lst.append(key)
            else:
                pass

print(sum(right_results_lst))
