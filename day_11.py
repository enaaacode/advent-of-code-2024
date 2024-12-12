data = "64599 31 674832 2659361 1 0 8867 321"

data = data.split()


# - - - - - - - functions - - - - - - -

def rule_for_zero(n):
    return 1

def rule_for_even_digits(n):
    number_as_string = str(n)
    digits = len(number_as_string) 
    devided_n = int(digits / 2) 
    new_number_one = number_as_string[0:devided_n]
    new_number_two = number_as_string[-devided_n:]
    return new_number_one, new_number_two

def rule_for_rest(n):
    new_number = n * 2024
    return new_number

# - - - - - - - let's code - - - - - - -

counter = 0

while counter < 25:

    new_lst = []

    for i in range(len(data)):

        if data[i] == "0":
            new_number = "1"
            new_lst.append(new_number)

        if len(data[i]) % 2 == 0:
            number = data[i]
            digits = len(number) 
            devided_n = int(digits / 2) 
            new_number_one = number[0:devided_n]
            new_lst.append(new_number_one)
            new_number_two = number[-devided_n:]

            if new_number_two[0] == "0":

                zero_counts = 0
                is_zero = True

                while is_zero:
                    for j in range(len(new_number_two)):
                        if (new_number_two[j]) == "0":
                            zero_counts += 1
                        if (new_number_two[j]) != "0":
                            is_zero = False 
                            break  
                        if j == len(new_number_two) - 1:
                            is_zero = False

                # this would be a problem: if zero_counts = 3 and new_number_two = 000
                # the solution:
                if zero_counts == len(new_number_two):
                    new_lst.append("0")
                else:
                    new_lst.append(new_number_two[zero_counts:])

            if new_number_two[0] != "0":
                new_lst.append(new_number_two)

        if data[i] != "0" and len(data[i]) % 2 != 0:
            new_number = str(int(data[i]) * 2024)
            new_lst.append(new_number)

    counter += 1
    data = new_lst

print(len(new_lst))

# - - - - - - - Part Two - - - - - - -

# While counter < 75 -> my code takes to long to process all the data
# idea: outsource all the zeros, because for the zeros I know what is happening. Tbd.
