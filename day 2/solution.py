

def solution(input):
    position = 0
    depth = 0
    aim = 0

    for command in input:
        command = command.split(' ')
        if command[0] == 'forward':
            position += int(command[1])
            depth += aim * int(command[1])
        elif command[0] == 'up':
            aim -= int(command[1])
        elif command[0] == 'down':
            aim += int(command[1])

    return position * depth


if __name__ == '__main__':
    example = ['forward 5',
               'down 5',
               'forward 8',
               'up 3',
               'down 8',
               'forward 2']
    print(solution(example))

    with open('input.txt') as f:
        input = f.readlines()
    print(solution(input))
