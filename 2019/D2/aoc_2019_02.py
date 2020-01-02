with open(r'aoc_2019_02_input.txt', 'r') as f:
    intcodes = [int(v) for v in f.read().strip().split(',')]

def intCompute(input):
    for i in range(0, len(input), 4):
        if input[i] == 1:
            input[input[i+3]] = input[input[i+1]] + input[input[i+2]]
        elif input[i] == 2:
            input[input[i+3]] = input[input[i+1]] * input[input[i+2]]
        elif input[i] == 99:
            break
        else:
            break
    
    return input

intcodes[1] = 49
intcodes[2] = 67
result = intCompute(intcodes)

print(f"Value at Index 0 = {result[0]}")