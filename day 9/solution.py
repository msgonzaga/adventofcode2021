import numpy as np


def get_adjacents(row, col, floor_map):
    try:
        assert row - 1 >= 0
        up = floor_map[row - 1, col]
    except:
        up = 10

    try:
        right = floor_map[row, col + 1]
    except:
        right = 10

    try:
        down = floor_map[row + 1, col]
    except:
        down = 10

    try:
        assert col - 1 >= 0
        left = floor_map[row, col - 1]
    except:
        left = 10

    return np.array([up, right, down, left])


def get_basin(low_point_row, low_point_col, floor_map, basin=[]):

    limits = floor_map.shape
    if low_point_row < 0 or low_point_row >= limits[0]:
        return

    if low_point_col < 0 or low_point_col >= limits[1]:
        return

    if (low_point_row, low_point_col) in basin:
        return

    if floor_map[low_point_row, low_point_col] == 9:
        return

    basin.append((low_point_row, low_point_col))

    get_basin(low_point_row - 1, low_point_col, floor_map, basin)
    get_basin(low_point_row, low_point_col + 1, floor_map, basin)
    get_basin(low_point_row + 1, low_point_col, floor_map, basin)
    get_basin(low_point_row, low_point_col - 1, floor_map, basin)


def solution(input_data):
    input_data = input_data.strip()
    floor_map = np.array([list(l)
                         for l in input_data.split('\n')], dtype=np.int)

    risk_sum = 0
    all_basins = []
    for row in range(floor_map.shape[0]):
        for col in range(floor_map.shape[1]):
            adjacents = get_adjacents(row, col, floor_map)
            if np.all(floor_map[row, col] < adjacents):
                risk_sum += 1 + floor_map[row, col]
                basin = []
                get_basin(row, col, floor_map, basin)
                all_basins.append(basin)

    all_basins = sorted(all_basins, key=lambda x: len(x), reverse=True)
    largest_3 = all_basins[0:3]

    return np.prod([len(b) for b in largest_3])


if __name__ == '__main__':
    example = """2199943210
3987894921
9856789892
8767896789
9899965678"""

    print(solution(example))

    with open('input.txt') as f:
        input_data = f.read()

    print(solution(input_data))
