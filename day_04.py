data = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''

    # Step 1: define what we are searching for

word = "XMAS"
word_backward = word[::-1]

    # Step 2: count horizontal

horizontal_count = data.count(word) + data.count(word_backward)

    # Step 3: count vertical and diagonal

data = data.splitlines()

counter = []

print("- - - The search - - -")

for i in range(len(data)):
    
    for j in range(len(data[i])): 

        # - - - count XMAS - - -

        # diagonal to the right 
        if j + 3 < len(data[i]) and i + 3 < len(data):
            if data[i][j] == "X" and data[i+1][j+1] == "M" and data[i+2][j+2] == "A" and data[i+3][j+3] == "S":
                counter.append("Found one")
                print("Found on XMAS diagonal the the right.")
        
        # diagonal to the left 
        if j - 3 >= 0 and i + 3 < len(data): # Ensure j-3 is within bounds
            if data[i][j] == "X" and data[i+1][j-1] == "M" and data[i+2][j-2] == "A" and data[i+3][j-3] == "S":
                counter.append("Found one")
                print("Found on XMAS diagonal the the left.")

        # vertical
        if i + 3 < len(data):  # Ensure i+3 is within bounds
            if data[i][j] == "X" and data[i+1][j] == "M" and data[i+2][j] == "A" and data[i+3][j] == "S":
                counter.append("Found one")
                print("Found on XMAS vertical.")

        # - - - count SAMX - - -

        # diagonal to the right 
        if j + 3 < len(data[i]) and i + 3 < len(data):
            if data[i][j] == "S" and data[i+1][j+1] == "A" and data[i+2][j+2] == "M" and data[i+3][j+3] == "X":
                counter.append("Found one")
                print("Found on SAMX diagonal the the right.")
        
        # diagonal to the left 
        if j - 3 >= 0 and i + 3 < len(data):
            if data[i][j] == "S" and data[i+1][j-1] == "A" and data[i+2][j-2] == "M" and data[i+3][j-3] == "X":
                counter.append("Found one")
                print("Found on SAMX diagonal the the left.")

        # vertical
        if i + 3 < len(data):  # Ensure i+3 is within bounds
            if data[i][j] == "S" and data[i+1][j] == "A" and data[i+2][j] == "M" and data[i+3][j] == "X":
                counter.append("Found one")
                print("Found on SAMX vertical.")


rest_count = len(counter)
complete_count = horizontal_count + rest_count

print("- - - The results - - -")
print("Horizontal there are", horizontal_count, "counts.")
print("Vertical and diagonal there are", rest_count, "counts.")

print ("The total count is:", complete_count)

# - - - Part Two: count X-MAS shape - - -

counter = []

print("- - - Part Two: The search - - -")

for i in range(len(data)):
    
    for j in range(len(data[i])): 

        if j + 2 < len(data[i]) and i + 2 < len(data):

            # MAS SAM
            if data[i+1][j+1] == "A" and data[i][j] == "M" and data[i][j+2] == "S" and data[i+2][j] == "M"  and data[i+2][j+2] == "S":
                counter.append("Found one.")

            # MAS MAS
            if data[i+1][j+1] == "A" and data[i][j] == "M" and data[i][j+2] == "M" and data[i+2][j] == "S"  and data[i+2][j+2] == "S":
                counter.append("Found one.")

            # SAM SAM
            if data[i+1][j+1] == "A" and data[i][j] == "S" and data[i][j+2] == "S" and data[i+2][j] == "M"  and data[i+2][j+2] == "M":
                counter.append("Found one.")

            # SAM MAS
            if data[i+1][j+1] == "A" and data[i][j] == "S" and data[i][j+2] == "M" and data[i+2][j] == "S"  and data[i+2][j+2] == "M":
                counter.append("Found one.")


complete_count = len(counter)

print ("The total count of X-MAS shape is:", complete_count)
