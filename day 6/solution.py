import numpy as np

def solution(input_data):
    input_data = np.array([int(fish) for fish in input_data.strip().split(',')], dtype=np.int)
    unique_fish = np.unique(input_data)
    fish_tank = []
    for fish in unique_fish:
        fish_group = {'amount': 0, 'timer': 0}
        fish_group['amount'] = len(input_data[input_data == fish])
        fish_group['timer'] = fish
        fish_tank.append(fish_group)

    days_to_run = 1000

    for day in range(days_to_run):
        for group in fish_tank:
            if group['timer'] == 0:
                group['timer'] = 6
                new_group = {'amount': group['amount'], 'timer': 9}
                fish_tank.append(new_group)
            else:
                group['timer'] -= 1

        # fish tank optimization
        timers = set([g['timer'] for g in fish_tank])
        new_fish_tank = []
        for timer in timers:
            new_group = {'timer': timer}
            amount = sum([g['amount'] for g in fish_tank if g['timer'] == timer])
            new_group['amount'] = amount
            new_fish_tank.append(new_group)
        fish_tank = new_fish_tank
    
    return sum([g['amount'] for g in fish_tank])


if __name__ == '__main__':
    example = '3,4,3,1,2'

    print(solution(example))

    with open('input.txt') as f:
        input_data = f.read()
    
    print(solution(input_data))