import copy

data_org = '''AAAA
BBCD
BBCC
EEEC'''

data_org = data_org.splitlines()

data = []

for line in data_org:
    line_lst = []
    for entry in line:
        line_lst.append(entry)
    data.append(line_lst)

# print it nice
print()
print("This is my garden:")
for sublist in data:
    print(sublist)
print("-" * 30)

# first i want to check how big each area is

area_size_lst = []
area_lst = {}
garden = copy.deepcopy(data)

# use flood-fill algorithm

    
# print it nice
print()
print("This is my checked garden:")
for sublist in garden:
    print(sublist)
print("-" * 30)

