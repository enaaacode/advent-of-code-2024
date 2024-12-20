data = '''Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0'''
 
# process data

data = data.splitlines()
print(data)

registers = []
programm = []

for line in data:
    if line.startswith("Register"):
        registers.append(line)  
    elif line.startswith("Program"):
        programm.append(line[9::].split(","))  

for n in programm:
    print("Register:", registers)
    print("Programm:", programm)


# if opcode = 0
def adv(register, operand):
    return register // 2**operand

# if opcode = 1
def bxl(register, operand):
    # Mache ein XOR zwischen B und dem Operand und speichere das Ergebnis in B.
    pass

# if opcode = 2
def adv(register, operand):
    # bst	Berechne den Wert des Operanden modulo 8 und speichere ihn in B.
    pass

# if opcode = 3
def adv(register, operand):
    # jnz	Springe zur Position des Operanden, wenn A nicht 0 ist.
    pass

# if opcode = 4
def adv(register, operand):
    # bxc	Mache ein XOR zwischen B und C und speichere das Ergebnis in B.
    pass

# if opcode = 5
def adv(register, operand):
    # out	Gib den Wert des Operanden modulo 8 aus.
    pass

# if opcode = 6
def adv(register, operand):
    # bdv	Teile Register A durch 2**Operand (ganzzahlig) und speichere das Ergebnis in B.
    pass

# if opcode = 7
def adv(register, operand):
    # cdv	Teile Register A durch 2**Operand (ganzzahlig) und speichere das Ergebnis in C.
    pass
