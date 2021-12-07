import numpy as np


def parse_input(input):
    input = input.split('\n')
    input = [s.split(' -> ') for s in input]
    int_input = []
    for line in input:
        if line != ['']:
            line = np.array([l.split(',') for l in line], dtype=np.int)
            int_input.append(line)
    return np.array(int_input, dtype=np.int)


def sep_ver_hor_diag_lines(input):
    ver_hor_lines = []
    diag_lines = []
    for line in input:
        if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
            ver_hor_lines.append(line)
        else:
            diag_lines.append(line)
    ver_hor_lines = np.array(ver_hor_lines, dtype=np.int)
    diag_lines = np.array(diag_lines, dtype=np.int)
    return ver_hor_lines, diag_lines


def apply_hor_ver_lines(lines, bitmap):
    for line_idx in range(lines.shape[0]):
        line = lines[line_idx, :, :]
        x1 = line[0, 0]
        x2 = line[1, 0]
        y1 = line[0, 1]
        y2 = line[1, 1]

        if x1 > x2:
            x1, x2 = x2, x1
        
        if y1 > y2:
            y1, y2 = y2, y1

        bitmap[y1:y2+1, x1:x2+1] += 1
    return bitmap


def linear_interp(x, point1, point2):
    slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
    return int(point1[1] + slope * (x - point1[0]))


def apply_diag_lines(lines, bitmap):
    for line_idx in range(lines.shape[0]):
        line = lines[line_idx, :, :]
        x1 = line[0, 0]
        x2 = line[1, 0]
        y1 = line[0, 1]
        y2 = line[1, 1]

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2+1):
            y = linear_interp(x, (x1, y1), (x2, y2))
            bitmap[y, x] += 1
    
    return bitmap


def solution(input_data):
    input_data = parse_input(input_data)
    max_row = np.max(input_data[:, 0, :])
    max_col = np.max(input_data[:, 1, :])
    bitmap = np.zeros(shape=(max_row+1, max_col+1))

    ver_hor_lines, diag_lines = sep_ver_hor_diag_lines(input_data)
    bitmap = apply_hor_ver_lines(ver_hor_lines, bitmap)
    bitmap = apply_diag_lines(diag_lines, bitmap)
    
    return len(bitmap[bitmap >= 2])


if __name__ == '__main__':
    example = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

    print(solution(example))

    with open('input.txt') as f:
        input_data = f.read()
    
    print(solution(input_data))