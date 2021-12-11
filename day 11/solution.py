from functools import total_ordering
import numpy as np


def parse_input(input_data):
    lines = input_data.strip().split('\n')
    lines = [list(l) for l in lines]
    matrix = np.array(lines, dtype=np.int)
    return matrix

def get_adjacents(x, y, map_shape):
    adjacents = []
    x_mods = [-1, 0, 1]
    y_mods = [-1, 0, 1]

    for xm in x_mods:
        for ym in y_mods:
            new_x = x + xm
            new_y = y + ym

            if new_x < 0 or new_y < 0:
                continue

            if new_x >= map_shape[0] or new_y >= map_shape[1]:
                continue

            adjacents.append((new_x, new_y))

    return adjacents

def perform_flash_chain(octopus_map):
    over_9_x, over_9_y = np.where(octopus_map > 9)
    flashing_octs = (list(over_9_x), list(over_9_y))

    while len(over_9_x) > 0:
        for x, y in zip(over_9_x, over_9_y):
            adj_x, adj_y = zip(*get_adjacents(x, y, octopus_map.shape))
            octopus_map[adj_x, adj_y] += 1
        
        octopus_map[flashing_octs[0], flashing_octs[1]] = 0
        over_9_x, over_9_y = np.where(octopus_map > 9)
        flashing_octs[0].extend(list(over_9_x))
        flashing_octs[1].extend(list(over_9_y))
        
    return octopus_map, flashing_octs


def solution(input_data, steps_to_run=500):
    octopus_map = parse_input(input_data)
    total_flashes = 0
    first_sync_flash = 0
    
    for step in range(steps_to_run):
        octopus_map += 1
        octopus_map, flashes = perform_flash_chain(octopus_map)
        total_flashes += len(flashes[0])

        if first_sync_flash == 0 and len(flashes[0]) == octopus_map.size:
            first_sync_flash = step + 1
    
    return total_flashes, first_sync_flash
    


if __name__ == '__main__':
    example = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

    print(solution(example))

    with open('input.txt') as f:
        input_data = f.read()
    
    print(solution(input_data))