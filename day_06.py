data = '''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
'''

# split lines and create list containing sublists
data = data.splitlines()

data_lst = []
for line in data:
    line = list(line)
    data_lst.append(line)

data = data_lst 

# Step 1: find starting point at "^"

start_line = 0
start_col = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "^":
            start_line = i
            start_col = j 
            data[i][j] = "X"
            
#print(f"We start in line {start_line}, column {start_col} (if we start counting at 0.)")

# - - - - - - - functions - - - - - - - 

def move_up(lst):
    global start_line, start_col, direction, i
    start_line = start_line - i + 1
    direction = "right"

def move_right(lst):
    global start_line, start_col, direction, i
    start_col = start_col + j - 1
    direction = "down"

def move_down(lst):
    global start_line, start_col, direction, i
    start_line = start_line + i - 1
    direction = "left"

def move_left(lst):
    global start_line, start_col, direction, i
    start_col = start_col - j + 1
    direction = "up"

# - - - - - - - let's move! - - - - - - - 

visit = "X"

direction = "up"

running = True

while running:
   
    # move up
    for i in range(len(data)):
        for j in range(len(data[i])):

            if direction == "up":

                if data[start_line - i][start_col] == ".":
                    data[start_line - i][start_col] = visit

                if data[start_line - i][start_col] == "#":
                    move_up(data)
                    break

                # check if done    
                if start_line - i == 0 and data[start_line][start_col] == "X":
                    running = False

    # move right
    for i in range(len(data)):
        for j in range(len(data[i])):

            if direction == "right":

                if start_col + j < len(data[start_line]) and data[start_line][start_col + j] == ".":
                    data[start_line][start_col + j] = visit

                if start_col + j < len(data[start_line]) and data[start_line][start_col + j] == "#":
                    move_right(data)
                    break    

                # check if done    
                if start_col + j == len(data[start_line]) and data[start_line][start_col] == "X":
                    running = False

    # move down
    for i in range(len(data)):
        for j in range(len(data[i])):

            if direction == "down":

                if start_line + i < len(data) and data[start_line + i][start_col] == ".":
                    data[start_line + i][start_col] = visit

                if start_line + i < len(data) and data[start_line + i][start_col] == "#":
                    move_down(data)
                    break

                # check if done    
                if start_line + i == len(data) and data[start_line][start_col] == "X":
                    running = False

    # move left
    for i in range(len(data)):
        for j in range(len(data[i])):

            if direction == "left":

                if start_col - j >= 0 and data[start_line][start_col - j] == ".":
                    data[start_line][start_col - j] = visit

                if start_col - j >= 0 and data[start_line][start_col - j] == "#":
                    move_left(data)
                    break
                
                # check if done  
                if start_col - j == 0 and data[start_line][start_col] == "X":
                    running = False

 #   for i in range(len(data)):
 #       print(data[i])
 #   print()

counter = 0

for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == "X":
            counter = counter + 1

print(counter)

