import numpy as np
from collections import defaultdict
import heapq


def parse_input(input_data):
    cave_map = input_data.strip().split('\n')
    cave_map = np.array([list(l.strip()) for l in cave_map], dtype=np.int)
    return cave_map


def build_bigger_map(cave_map):

    # expand horizontally
    map_unit = cave_map.copy()
    for _ in range(1, 5):
        map_unit = map_unit + 1
        map_unit[map_unit > 9] = 1
        cave_map = np.concatenate([cave_map, map_unit], axis=1)

    # expand vertically
    map_unit = cave_map.copy()
    for _ in range(1, 5):
        map_unit = map_unit + 1
        map_unit[map_unit > 9] = 1
        cave_map = np.concatenate([cave_map, map_unit], axis=0)

    return cave_map


def get_adjacents(i, j, cave_map):
    up = (i - 1, j)
    right = (i, j + 1)
    down = (i + 1, j)
    left = (i, j - 1)

    adjacents = [up, right, down, left]
    adjacents = [pos for pos in adjacents if pos[0] >= 0 and pos[1] >= 0]
    adjacents = [pos for pos in adjacents if pos[0] <
                 cave_map.shape[0] and pos[1] < cave_map.shape[1]]

    return adjacents


def update_risk(i, j, risk_dict,  current_risk, cave_map):
    if risk_dict[(i, j)] > current_risk + cave_map[i, j]:
        risk_dict[(i, j)] = current_risk + cave_map[i, j]
    return risk_dict


def solution(input_data):
    cave_map = parse_input(input_data)

    cave_map = build_bigger_map(cave_map)

    risk_dict = defaultdict(lambda: np.inf)
    min_risk = [(0, (0, 0))]  # heap to optimize getting the min risk value
    risk_dict[(0, 0)] = 0
    nodes = {(i, j): 0 for i in range(
        cave_map.shape[0]) for j in range(cave_map.shape[1])}

    while nodes:
        min_v = heapq.heappop(min_risk)

        i, j = min_v[1]
        try:
            # visited node
            del nodes[(i, j)]
        except:
            continue
        current_risk = risk_dict[(i, j)]

        adjacents = get_adjacents(i, j, cave_map)

        for adj in adjacents:
            if (adj[0], adj[1]) in nodes:
                risk_dict = update_risk(
                    adj[0], adj[1], risk_dict, current_risk, cave_map)
                heapq.heappush(
                    min_risk, (risk_dict[(adj[0], adj[1])], (adj[0], adj[1])))

    return risk_dict[(cave_map.shape[0] - 1, cave_map.shape[1] - 1)]


if __name__ == '__main__':
    example = """1163751742
                 1381373672
                 2136511328
                 3694931569
                 7463417111
                 1319128137
                 1359912421
                 3125421639
                 1293138521
                 2311944581"""

    print(solution(example))

    with open('input.txt') as f:
        input_data = f.read()

    print(solution(input_data))
