import copy 

data = '''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3  
'''
# p = position, v = velocity/speed
data = data.splitlines()

data_split = []
position = []
velocity = []

for i in range(len(data)):
    data_split_entry = data[i].split()
    data_split.append(data_split_entry)

# fill position = [] and velocity = []
for i in range(len(data_split)):
    for j in range(len(data_split[i])):
        if data_split[i][j][0] == "p":
            position_entry = data_split[i][j][2:]
            position_entry = position_entry.split(",")
            position.append(position_entry)
        else:
            velocity_entry = data_split[i][j][2:]
            velocity_entry = velocity_entry.split(",")
            velocity.append(velocity_entry)

for i in range(len(position)):
    for j in range(len(position[i])):
        position[i][j] = int(position[i][j])
        velocity[i][j] = int(velocity[i][j])

# - - - - - - - functions - - - - - - -

def to_big(number, len):
    diff = number - len
    return 0 + diff - 1     

def to_small(number, len):
    diff = abs(number)
    return len - diff + 1

# - - - - - - - let's do it! - - - - - - -

startposition = copy.deepcopy(position)

x_len = 100
y_len = 102

duration = 100 

seconds = 0

while seconds < duration:

    for i in range(len(position)):

        # check X position -> position[i][0]
        position[i][0] = position[i][0] + velocity[i][0]

        if position[i][0] > x_len:
            position[i][0] = to_big(position[i][0], x_len)

        if position[i][0] < 0:
            position[i][0] = to_small(position[i][0], x_len)
        
        # check Y position -> position[i][1]
        position[i][1] = position[i][1] + velocity[i][1]

        if position[i][1] > y_len:
            position[i][1] = to_big(position[i][1], y_len)

        if position[i][1] < 0:
            position[i][1] = to_small(position[i][1], y_len)
            
    seconds +=1

'''for i in range(len(position)):
    print(f"{startposition[i]} and {velocity[i]} = {position[i]}")'''

one = []
two = []
three = []
four = []

for i in range(len(position)):
        
        if position[i][0] < x_len/2 and position[i][1] < y_len/2:
            one.append(position[i])

        if position[i][0] < x_len/2 and position[i][1] > y_len/2:
            two.append(position[i])

        if position[i][0] > x_len/2 and position[i][1] < y_len/2:
            three.append(position[i])

        if position[i][0] > x_len/2 and position[i][1] > y_len/2:
            four.append(position[i])

'''print()
print(f"1 {one}")
print(f"2 {two}")
print(f"3 {three}")
print(f"4 {four}")'''

print(len(one) * len(two) * len(three) * len(four))
