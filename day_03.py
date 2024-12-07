input = '''xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'''

# The given input code is corrupted. 
# Task 1: Check the code for correct mul(X,Y) 
# Task 2: Add up the results of mul(X,Y)

# 1. Step: Make a list only with the correct mul(X,Y)

mul_list = []

# the first loop collects all mul(,) in a list 
for i in range(len(input)):
    if input[i] == "m" and input[i+1] == "u" and input[i+2] == "l" and input[i+3] == "(" and input[i+5] == "," and input[i+7] == ")": 
        correct_mul = input[i:i+8]  
        mul_list.append(correct_mul)    

print(mul_list)  

# OH NO! mul_list is not complete jet. We also have to think about two-digit and three-digit numbers
for i in range(len(input)):
    rule = input[i] == "m" and input[i+1] == "u" and input[i+2] == "l" and input[i+3] == "("
    # if x is one-digit and y is one-digit
    if rule and input[i+4].isdigit() and input[i+5] == "," and input[i+6].isdigit() and input[i+7] == ")":
        correct_mul = input[i:i+8]
        mul_list.append(correct_mul)

    # if x is one-digit and y is two-digit
    if rule and input[i+4].isdigit() and input[i+5] == "," and input[i+6].isdigit() and input[i+7].isdigit() and input[i+8] == ")":
        correct_mul = input[i:i+9]
        mul_list.append(correct_mul)

    # if x is one-digit and y is three-digit
    if rule and input[i+4].isdigit() and input[i+5] == "," and input[i+6].isdigit() and input[i+7].isdigit() and input[i+8].isdigit() and input[i+9] == ")":
        correct_mul = input[i:i+10]
        mul_list.append(correct_mul)

    # if x is two-digit and y is one-digit
    if rule and input[i+4].isdigit() and input[i+5].isdigit() and input[i+6] == "," and input[i+7].isdigit() and input[i+8] == ")":
        correct_mul = input[i:i+9]
        mul_list.append(correct_mul)

    # if x is two-digit and y is two-digit
    if rule and input[i+4].isdigit() and input[i+5].isdigit() and input[i+6] == "," and input[i+7].isdigit() and input[i+8].isdigit() and input[i+9] == ")":
        correct_mul = input[i:i+10]
        mul_list.append(correct_mul)

    # if x is two-digit and y is three-digit
    if rule and input[i+4].isdigit() and input[i+5].isdigit() and input[i+6] == "," and input[i+7].isdigit() and input[i+8].isdigit() and input[i+9].isdigit() and input[i+10] == ")":
        correct_mul = input[i:i+11]
        mul_list.append(correct_mul)

    # if x is three-digit and y is one-digit
    if rule and input[i+4].isdigit() and input[i+5].isdigit() and input[i+6].isdigit() and input[i+7] == "," and input[i+8].isdigit() and input[i+9] == ")":
        correct_mul = input[i:i+10]
        mul_list.append(correct_mul)

    # if x is three-digit and y is two-digit
    if rule and input[i+4].isdigit() and input[i+5].isdigit() and input[i+6].isdigit() and input[i+7] == "," and input[i+8].isdigit() and input[i+9].isdigit() and input[i+10] == ")":
        correct_mul = input[i:i+11]
        mul_list.append(correct_mul)

    # if x is three-digit and y is three-digit
    if rule and input[i+4].isdigit() and input[i+5].isdigit() and input[i+6].isdigit() and input[i+7] == "," and input[i+8].isdigit() and input[i+9].isdigit() and input[i+10].isdigit() and input[i+11] == ")":
        correct_mul = input[i:i+12]
        mul_list.append(correct_mul)


x_and_y_list = []

# we only need the X,Y -> mul(,) can be removed   
for i in range(len(mul_list)):
    print(mul_list[i])
    cleanup = mul_list[i].replace("m", "").replace("u", "").replace("l", "").replace("(", "").replace(",", " ").replace(")", "").split()
    x_and_y_list.append(cleanup)

print(x_and_y_list)

# now we check if the X and Y are digits

only_digits = []

for i in range(len(x_and_y_list)):
    print(x_and_y_list[i])
    for j in range(len(x_and_y_list[i]) - 1):
        print(x_and_y_list[i][j])
        digits = []
        if x_and_y_list[i][j].isdigit() and x_and_y_list[i][j + 1].isdigit():
            x = x_and_y_list[i][j] 
            y = x_and_y_list[i][j+1]
            digits.append(x)
            digits.append(y)
    only_digits.append(digits)

print(only_digits)

# to be able to multiply X and Y we have to convert them to int

x_and_y_int = []

for i in range(len(only_digits)):
    print(only_digits[i])
    integer_list = []
    for j in range(len(only_digits[i])):
        integer = only_digits[i][j]
        integer_list.append(integer)
    x_and_y_int.append(integer_list)

print(x_and_y_int)

# let's multiply X * Y

def multiply(list):
    return int(list[0]) * int(list[1])

multiply_list = []

for i in range(len(x_and_y_int)):
    print(x_and_y_int[i])
    multiply_list.append(multiply(x_and_y_int[i]))

print(multiply_list)

# now we have to add up all numbers

final_result = sum(multiply_list)

print(final_result)
