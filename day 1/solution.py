import numpy as np


def solution(input):
    diff = np.diff(input)
    answer = np.sum(diff > 0)
    return answer


def apply_sum_window(input, window_len=3):
    cur_idx = 0
    new_input = []
    while cur_idx + window_len <= len(input):
        new_input.append(np.sum(input[cur_idx:cur_idx + window_len]))
        cur_idx += 1
    return new_input


if __name__ == '__main__':
    example = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    sum_window_example = apply_sum_window(example)

    print(solution(sum_window_example))

    with open('input.txt') as f:
        input = f.readlines()
        input = np.array(input).astype(np.int)

    sum_window_input = apply_sum_window(input)

    print(solution(sum_window_input))
