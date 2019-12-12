# Part1
puzzle_input = {"start": 172930, "end": 683082}
#puzzle_input = {"start": 172930, "end": 172932}

def check_password(password):
    psw = str(password)
    prev_digit = ""
    adjacent = False
    decrease = True

    for digit in psw:
        # Check adjacent digit
        if digit == prev_digit:
            #Part1
            adjacent = True

        # Check decrease
        if digit < prev_digit:
            decrease = False
        if adjacent and not decrease:
            break
        prev_digit = digit
    return adjacent and decrease

#Part 2
def check_adjacent(password):
    psw = str(password)
    prev_digit = ""
    start = middle = False
    adjacent = False

    for digit in psw:
        if digit == prev_digit:
            if middle:
                start = False
            middle = True
        else:
            if start and middle:
                break
            start = True
            middle = False
        prev_digit = digit
    if start and middle:
        adjacent = True
    return adjacent

def check_decrease(password):
    psw = str(password)
    prev_digit = ""
    increase = True

    for digit in psw:
        # Check decrease
        if digit < prev_digit:
            increase = False
            break
        prev_digit = digit
    return increase


def count_passwords():
    count = 0
    for value in range(puzzle_input["start"], puzzle_input["end"]+1):
        #if check_password(value):
        if  check_decrease(value):
            if check_adjacent(value):
                print(value)
                count +=1
    return count

print(count_passwords())
