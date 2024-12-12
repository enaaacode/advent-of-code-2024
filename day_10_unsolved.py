from pprint import pprint

data = '''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732'''

print()

# prepare data (splitlines, make list)

data = data.splitlines()

data_lst = []
for i in range(len(data)):
    data_lst.append(data[i])

value_lst = list(range(0, 10)) # not sure if I need this

data_int_lst = []
for i in range(len(data_lst)):
    print(data_lst[i])
    entry = []
    for j in range(len(data_lst[i])):
        entry.append(int(data_lst[i][j]))
    data_int_lst.append(entry)

data_lst = data_int_lst

for entry in data_lst:
    print(entry)

print(f"0 is the start, 9 the highest point: {value_lst}")

# check data_lst

for i in range(len(data_lst)):
    #print(data_lst[i])
    for j in range(len(data_lst[i])):
        if data_lst[i][j] == 0:
            print(f"there is a 0 in line {i}, column {j}")
            # check right side
            print()
            print(data_lst[i][j+1])
            print(data_lst[i][j]+1)
            print()
            if data_lst[i][j+1] == data_lst[i][j]+1:
                print("continue")

# ufff... no idea how to continue
