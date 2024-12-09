from pprint import pprint
from itertools import product

data_original = '''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
'''

# prepare data 

data = data_original.splitlines()

data_lst = []
for line in data:
    line_lst = []
    for i in range(len(line)):
        entry = line[i]
        line_lst.append(entry)
    data_lst.append(line_lst)
data = data_lst

# create a list of antennas

antennas_lst = []

for line in data:
    for position in line:
        if position != "." and position not in antennas_lst:
            antennas_lst.append(position)

count_of_antennas = len(antennas_lst)

print()
print(f"This are our antenna types: {antennas_lst}")
print(f"It are {count_of_antennas} types")

# how many antennas of each type are there?

antennas_count_dict = {}

for antenna in antennas_lst:
    antennas_count_dict[antenna] = data_original.count(antenna)

print(f"This is our dictionary: {antennas_count_dict}")

# find all antenna positions

#pprint(data)

positions_dict = {}

for antenna in antennas_lst: # check each antenna type

    antenna_positions_lst = []

    for i in range(len(data)): # check complete data

        for j in range(len(data[i])): # check line
            
            position = []

            if antenna == data[i][j]: # find the line containing antenna type
                print()
                print(f"There is a antenna '{antenna}' at:")
                print(f"Line: {i}") 
                position.append(i)

                for j in range(len(data[i])): # find the column
                    if antenna == data[i][j]:
                        print(f"Column: {j}")
                        position.append(j)

                antenna_positions_lst.append(position)

                print("-" * 30)

    positions_dict[antenna] = antenna_positions_lst    
    print(f"This are the positions of antenna '{antenna}': {antenna_positions_lst}")
    print()

print(positions_dict)

# find positions of antinodes

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def binomial_coefficient(n, k): # k will be 2 because we build pairs 
    if k < 0 or k > n:
        return 0  # the binomial coefficient is not defined for these values
    return factorial(n) // (factorial(k) * factorial(n - k))

def get_all_combinations(value): 
    n = len(value) - 1  
    return list(product("+*", repeat=n))

# - - - - - - - test with one list only - - - - - - - 

print(antennas_count_dict)

n = binomial_coefficient(antennas_count_dict["A"], 2)

test = positions_dict["A"]
print("-" * 30)
print()
print(f"This is my test list: {test}")
print(f"There are {n} ways to build different pairs.")
print()

pairs_lst = []

def create_combinations(lst):
    result = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j: 
                result.append([lst[i], lst[j]])
    return result

def create_unique_combinations(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):  
            result.append([lst[i], lst[j]])
    return result

input_list = test
output_list = create_unique_combinations(input_list)
print("This are the unique combinations:")
for unique_combination in output_list:
    print(unique_combination)


