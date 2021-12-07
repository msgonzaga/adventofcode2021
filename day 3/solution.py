

def get_most_least_common_bits(diagnostic):
    positions = [0] * len(diagnostic[0])

    for diag in diagnostic:
        for bit_idx in range(len(diagnostic[0])):
            positions[bit_idx] += int(diag[bit_idx])
    
    most_common = []
    least_common = []
    for count in positions:
        if count >= len(diagnostic) / 2:
            most_common.append(1)
            least_common.append(0)
        else:
            most_common.append(0)
            least_common.append(1)
    return most_common, least_common

def solution(input_data):
    most_common, least_common = get_most_least_common_bits(input_data)

    # find oxygen gen rating
    oxygen_input = input_data.copy()
    for bit_idx in range(len(input_data[0])):
        oxygen_input = [d for d in oxygen_input if int(d[bit_idx]) == most_common[bit_idx]]
        if len(oxygen_input) == 1:
            break
    
    # find co2 scrubber rating
    co2_input = input_data.copy()
    for bit_idx in range(len(input_data[0])):
        co2_input = [d for d in co2_input if int(d[bit_idx]) == least_common[bit_idx]]
        if len(co2_input) == 1:
            break
    
    oxygen_input = oxygen_input[0][::-1]
    co2_input = co2_input[0][::-1]

    oxygen_num = sum([int(oxygen_input[i])*2**i for i in range(len(input_data[0]))])
    co2_num = sum([int(co2_input[i])*2**i for i in range(len(input_data[0]))])

    return oxygen_num * co2_num

if __name__ == '__main__':
    example = ['00100',
               '11110',
               '10110',
               '10111',
               '10101',
               '01111',
               '00111',
               '11100',
               '10000',
               '11001',
               '00010',
               '01010']
    print(solution(example))

    with open('input.txt') as f:
        input_data = f.readlines()
        input_data = [s.strip() for s in input_data]
    
    print(solution(input_data))
