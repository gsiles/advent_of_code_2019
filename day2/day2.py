# Part1
puzzle_input = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 10, 19, 2, 9, 19, 23, 1, 9, 23, 27, 2,
                27, 9, 31, 1, 31, 5, 35, 2, 35, 9, 39, 1, 39, 10, 43, 2, 43, 13, 47, 1, 47, 6, 51, 2, 51,
                10, 55, 1, 9, 55, 59, 2, 6, 59, 63, 1, 63, 6, 67, 1, 67, 10, 71, 1, 71, 10, 75, 2, 9, 75,
                79, 1, 5, 79, 83, 2, 9, 83, 87, 1, 87, 9, 91, 2, 91, 13, 95, 1, 95, 9, 99, 1, 99, 6, 103,
                2, 103, 6, 107, 1, 107, 5, 111, 1, 13, 111, 115, 2, 115, 6, 119, 1, 119, 5, 123, 1, 2,
                123, 127, 1, 6, 127, 0, 99, 2, 14, 0, 0]


def one(program, store_position, num1_position, num2_position):
    program[store_position] = program[num1_position] + program[num2_position]


def two(program,  store_position, num1_position, num2_position):
    program[store_position] = program[num1_position] * program[num2_position]


def run_intcode(program):
    switcher = {
        1: one,
        2: two
    }
    for i in range(0, len(program), 4):
        opcode = program[i]
        if opcode == 99:
            break

        num1_position = program[i+1]
        num2_position = program[i+2]
        store_position = program[i+3]
        func = switcher.get(opcode, lambda: "unknown code")
        func(program, store_position, num1_position, num2_position)


def part_one():
    program = puzzle_input.copy()
    program[1] = 12
    program[2] = 2
    run_intcode(program)
    return program


print("Solution Part One")

print(part_one()[0])

# Part 2


def part_two():
    for noun in range(100):
        for verb in range(100):
            program = puzzle_input.copy()
            program[1] = noun
            program[2] = verb
            run_intcode(program)
            if program[0] == 19690720:
                return 100 * noun + verb


print("Solution Part Two")
print(part_two())
