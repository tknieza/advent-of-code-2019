input = "1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,2,19,6,23,1,23,5,27,1,9,27,31,1,31,10,35,2,35,9,39,1,5,39,43,2,43,9,47,1,5,47,51,2,51,13,55,1,55,10,59,1,59,10,63,2,9,63,67,1,67,5,71,2,13,71,75,1,75,10,79,1,79,6,83,2,13,83,87,1,87,6,91,1,6,91,95,1,10,95,99,2,99,6,103,1,103,5,107,2,6,107,111,1,10,111,115,1,115,5,119,2,6,119,123,1,123,5,127,2,127,6,131,1,131,5,135,1,2,135,139,1,139,13,0,99,2,0,14,0"

intcode_data = [int(x) for x in input.split(',')]

def test(noun, verb):
    intcode = [x for x in intcode_data]
    index = 0
    intcode[1] = noun
    intcode[2] = verb

    while True:
        opcode = intcode[index]
        value_1 = intcode[index + 1]
        value_2 = intcode[index + 2]
        position = intcode[index + 3]
        if opcode == 1:
            intcode[position] = intcode[value_1] + intcode[value_2]
            index += 4
        elif opcode == 2:
            intcode[position] = intcode[value_1] * intcode[value_2]
            index += 4
        else:
            break

    return intcode[0]

for noun in range(100):
    for verb in range(100):
        if test(noun, verb) == 19690720:
            print(100 * noun + verb)
            break