import numpy as np


def solution_first_part(input_data):
    input_data = np.array(input_data.split(','), dtype=np.int)
    median = np.median(input_data)
    return np.sum(np.abs(input_data - median))


def solution_second_part(input_data):
    input_data = np.array(input_data.split(','), dtype=np.int)
    max_position = np.max(input_data)
    position_fuel = np.zeros(max_position)
    for i in range(max_position):
        position_fuel[i] = np.sum([sum(range(0, abs(p - i) + 1)) for p in input_data])
    
    return np.min(position_fuel)



if __name__ == "__main__":

    example = '16,1,2,0,4,2,7,1,2,14'

    print(solution_second_part(example))

    with open('input.txt') as f:
        input_data = f.read()
    
    print(solution_second_part(input_data))

