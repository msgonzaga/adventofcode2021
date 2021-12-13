import numpy as np


def parse_input(input_data):
    input_data = input_data.strip().split('\n')
    empty_line = input_data.index('')
    dots = input_data[:empty_line]
    instructions = input_data[empty_line+1:]
    dots = [tuple(map(lambda x: int(x), d.split(','))) for d in dots]
    instructions = [inst.replace('fold along ', '').split('=')
                    for inst in instructions]
    instructions = [[inst[0], int(inst[1])] for inst in instructions]

    return dots, instructions


def fold_up(dots, y):
    new_dots = []

    for dot in dots:
        if dot[1] > y:
            new_y = y - (dot[1] - y)
            folded_dot = (dot[0], new_y)
            new_dots.append(folded_dot)
        else:
            new_dots.append(dot)
    new_dots = list(set(new_dots))
    return new_dots


def fold_left(dots, x):
    new_dots = []

    for dot in dots:
        if dot[0] > x:
            new_x = x - (dot[0] - x)
            folded_dot = (new_x, dot[1])
            new_dots.append(folded_dot)
        else:
            new_dots.append(dot)
    new_dots = list(set(new_dots))
    return new_dots


def fold(dots, instruction):
    if instruction[0] == 'x':
        dots = fold_left(dots, instruction[1])
    elif instruction[0] == 'y':
        dots = fold_up(dots, instruction[1])
    return dots


def print_paper(dots):
    max_x = max([dot[0] for dot in dots])
    max_y = max([dot[1] for dot in dots])
    paper = np.zeros(shape=(max_x+1, max_y+1), dtype=np.object)
    paper[:] = '.'

    for dot in dots:
        paper[dot[0], dot[1]] = '#'

    for x in range(paper.shape[0]):
        print(''.join(list(paper[x, :])))


def solution(input_data):
    dots, instructions = parse_input(input_data)

    for inst in instructions:
        dots = fold(dots, inst)

    print_paper(dots)


if __name__ == '__main__':
    example = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

    solution(example)

    with open('input.txt') as f:
        input_data = f.read()

    solution(input_data)
