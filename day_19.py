data = '''r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
'''

data = data.splitlines()

# available towel patterns
towels_raw = data[0].split(",")  
towels_lst = []

for item in towels_raw:
    towels_lst.append(item.strip())

# the list of desired designs
designs_lst = data[2::]

# not all designs will be possible with the available towels
# how many designs are possible?

# - - - - - - - function - - - - - - -

def can_build_design(design, towels):
    if len(design) == 0:
        return True 

    for towel in towels:  
        if design.startswith(towel): 
            result = can_build_design(design[len(towel):], towels)  
            if result:  
                return True  
    return False  

# - - - - - - - let's do it - - - - - - -

possible_designs_lst = []

for design in designs_lst:
    if can_build_design(design, towels_lst):
        possible_designs_lst.append(design)

print(f"{len(possible_designs_lst)} designs are possible.") 
