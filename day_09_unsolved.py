data = "233313312141413140233"

print()

data_lst = []
for i in range(len(data)):
    data_lst.append(int(data[i]))

print(data_lst)

# Step 1: make a few lists and a dict

file_id_dict = {}
dot_lst = []

id_counter = 0
for i in range(len(data_lst)):
    if i % 2 == 0:
        file_id_dict[id_counter] = data_lst[i]
        id_counter = id_counter + 1

    if i % 2 != 0:
        converted_entry = "." * data_lst[i]
        dot_lst.append(converted_entry)

convert_file_lst = []

for key, value in file_id_dict.items():

    converted_entry = str(key) * value
    convert_file_lst.append(converted_entry)

print(f"This is the ID dict: {file_id_dict}")
print(f"This is the convert file list: {convert_file_lst}")
print(f"This is the dot list: {dot_lst}")

convert_data_lst = [] # bring convert file list und dot list together

for i in range(len(convert_file_lst)):
    convert_data_lst.append(convert_file_lst[i])
    if i < len(dot_lst):
        convert_data_lst.append(dot_lst[i])

print(f"This is the final converted list: {convert_data_lst}")

# I want one single string, instead of a list

convert_data_str = "".join(convert_data_lst)
dots = convert_data_str.count(".")
str_length = len(convert_data_str)

print()
print(f"This is the converted data string: {convert_data_str}")
print(f"This is its length: {str_length}")
print(f"This is the number of dots in it: {dots}")

# now I want to create a reversed list of the files, to fill it in later

reversed_file_lst = list(reversed(convert_file_lst))
reversed_string = "".join(reversed_file_lst)
print()
print(f"This is the convert file list: {convert_file_lst}")
print(f"This is the reversed convert file list: {reversed_file_lst}")
print(f"This is the reversed string which I will use to fill the dots: {reversed_string}")

print()

# let's compress the data string, so the dots are at the end and the reversed string is filled in

compressed_data_lst = []

count_fill = 0
for i in range(str_length):
    entry = convert_data_str[i]

    if convert_data_str[i] != ".":
        compressed_data_lst.append(entry)

    else:
        entry = reversed_string[count_fill]
        compressed_data_lst.append(entry)
        count_fill += 1

print(f"This is the compressed data list: {compressed_data_lst} BUT we need to add the dots.")
print(f"This list has the length: {len(compressed_data_lst)}")

compressed_data_with_dots_lst = []

for i in range(len(compressed_data_lst)):
    if i < (str_length - dots):
        compressed_data_with_dots_lst.append(compressed_data_lst[i])
    else:
        compressed_data_with_dots_lst.append(".")

compressed_data_with_dots_str = "".join(compressed_data_with_dots_lst)

print(f"This is the final compressed data: {compressed_data_with_dots_lst}")
print(f"This is the final compressed string: {compressed_data_with_dots_str}")
print(f"This is the number of dots: {compressed_data_with_dots_str.count(".")} ")

if compressed_data_with_dots_str.count(".") == dots:
    print("The amount of dots is still the same.")

if compressed_data_with_dots_str == "0099811188827773336446555566..............":
    print("So far it is right.")

# multiply each number in the final string with its position 

multiply_lst = []

for i in range(len(compressed_data_with_dots_lst)): # check each position in the string
    if compressed_data_with_dots_lst[i] != ".":
        entry = int(compressed_data_with_dots_lst[i]) * i
        multiply_lst.append(entry)

print(multiply_lst)
print(sum(multiply_lst))
