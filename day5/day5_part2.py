puzzle_input = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,89,49,225,1102,35,88,224,101,-3080,224,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,1101,25,33,224,1001,224,-58,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1102,78,23,225,1,165,169,224,101,-80,224,224,4,224,102,8,223,223,101,7,224,224,1,224,223,223,101,55,173,224,1001,224,-65,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,2,161,14,224,101,-3528,224,224,4,224,1002,223,8,223,1001,224,7,224,1,224,223,223,1002,61,54,224,1001,224,-4212,224,4,224,102,8,223,223,1001,224,1,224,1,223,224,223,1101,14,71,225,1101,85,17,225,1102,72,50,225,1102,9,69,225,1102,71,53,225,1101,10,27,225,1001,158,34,224,101,-51,224,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,102,9,154,224,101,-639,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,226,226,224,102,2,223,223,1006,224,329,101,1,223,223,1007,677,677,224,1002,223,2,223,1005,224,344,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,359,1001,223,1,223,108,226,677,224,1002,223,2,223,1005,224,374,1001,223,1,223,107,226,677,224,102,2,223,223,1006,224,389,101,1,223,223,1107,226,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,419,101,1,223,223,1007,226,226,224,102,2,223,223,1006,224,434,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,449,101,1,223,223,1008,226,226,224,102,2,223,223,1005,224,464,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,479,101,1,223,223,1008,226,677,224,1002,223,2,223,1006,224,494,101,1,223,223,1107,226,677,224,1002,223,2,223,1005,224,509,1001,223,1,223,1108,226,226,224,1002,223,2,223,1006,224,524,101,1,223,223,7,226,226,224,102,2,223,223,1006,224,539,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,554,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,569,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,584,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,599,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,614,101,1,223,223,108,677,677,224,102,2,223,223,1005,224,629,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,644,1001,223,1,223,7,677,226,224,102,2,223,223,1006,224,659,1001,223,1,223,1007,226,677,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226]

def decode(operator):
    values = [0,0,0,0] #[opcode, mode_param1, mode_param2, mode_param3]
    aux = divmod(operator,100)
    operator = aux[0]
    values[0] = aux[1]
    for i in range(1,4):
        aux = divmod(operator,10)
        operator = aux[0]
        values[i] = aux[1]
    return values

def get_instruction_len(opcode):
    if opcode in [1,2,7,8]:
        return 4
    if opcode in [5,6]:
        return 3
    return 2

def one(program, operator, params):
    if operator[1]:
        num1 = params[0]
    else:
        num1 = program[params[0]]
    if operator[2]:
        num2 = params[1]
    else:
        num2 = program[params[1]]

    program[params[2]] = num1 + num2

def two(program, operator, params):
    if operator[1]:
        num1 = params[0]
    else:
        num1 = program[params[0]]
    if operator[2]:
        num2 = params[1]
    else:
        num2 = program[params[1]]

    program[params[2]] = num1 * num2

def three(program, params):
    program[params[0]] = int(input())

def four(program, operator, params):
    if operator[1]:
        print(params[0])
    else:
        print(program[params[0]])

def five(program, operator, params):
    if operator[1]:
        num1 = params[0]
    else:
        num1 = program[params[0]]
    if operator[2]:
        pointer = params[1]
    else:
        pointer = program[params[1]]
    if num1:
        return pointer
    return None

def six(program, operator, params):
    if operator[1]:
        num1 = params[0]
    else:
        num1 = program[params[0]]
    if operator[2]:
        pointer = params[1]
    else:
        pointer = program[params[1]]
    if not num1:
        return pointer
    return None

def seven(program, operator, params):
    if operator[1]:
        num1 = params[0]
    else:
        num1 = program[params[0]]
    if operator[2]:
        num2 = params[1]
    else:
        num2 = program[params[1]]
    if num1 < num2:
        program[params[2]] = 1
    else:
        program[params[2]] = 0

def eight(program, operator, params):
    if operator[1]:
        num1 = params[0]
    else:
        num1 = program[params[0]]
    if operator[2]:
        num2 = params[1]
    else:
        num2 = program[params[1]]
    if num1 == num2:
        program[params[2]] = 1
    else:
        program[params[2]] = 0

def run_intcode(program):
    program_len = len(program)
    pc = 0
    while pc < program_len:
        #pc always point to the start of the instruction
        operator = decode(program[pc]) #[opcode, mode_param1, mode_param2, mode_param3]
        instruction_len = get_instruction_len(operator[0])
        increment = None

        #get params of instruction
        params = [0,0,0]
        for j in range(1,instruction_len):
            params[j-1] = program[pc+j]

        #print(pc)
        if operator[0] == 1:
            one(program, operator, params)

        if operator[0] == 2:
            two(program, operator, params)

        if operator[0] == 3:
            three(program, params)

        if operator[0] == 4:
            four(program, operator, params)

        if operator[0] == 5:
            increment = five(program, operator, params)


        if operator[0] == 6:
            increment = six(program, operator, params)


        if operator[0] == 7:
            seven(program, operator, params)

        if operator[0] == 8:
            eight(program, operator, params)

        if increment == None:
            pc+=instruction_len
        else:
            pc = increment


run_intcode(puzzle_input)
