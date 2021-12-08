from collections import Counter
import numpy as np


UNIQUE_SEGMENTS_NUMBERS = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

DIGITS = {
    0: [1, 1, 1, 1, 1, 1, 0],
    1: [0, 1, 1, 0, 0, 0, 0],
    2: [1, 1, 0, 1, 1, 0, 1],
    3: [1, 1, 1, 1, 0, 0, 1],
    4: [0, 1, 1, 0, 0, 1, 1],
    5: [1, 0, 1, 1, 0, 1, 1],
    6: [1, 0, 1, 1, 1, 1, 1],
    7: [1, 1, 1, 0, 0, 0, 0],
    8: [1, 1, 1, 1, 1, 1, 1],
    9: [1, 1, 1, 1, 0, 1, 1],
}

SEGMENTS = list('abcdefg')

def decipher_pattern(patterns):
    unique_segment_nums = sorted(list(set([l for l in patterns if len(l) in UNIQUE_SEGMENTS_NUMBERS.keys()])), key=lambda x: len(x))
    unique_digits_order = [1, 7, 4, 8]

    solution_map = np.zeros(shape=(7, len(SEGMENTS)))

    for idx, digit in enumerate(unique_digits_order[:-1]):
        digit_map = unique_segment_nums[idx]
        digit_segments = DIGITS[digit] 
        for c in digit_map:
            letter_idx = SEGMENTS.index(c)
            for idx, bit in enumerate(digit_segments):
                if bit:
                    solution_map[idx, letter_idx] += 1
    
    for letter in SEGMENTS:
        max_count = np.max(solution_map[:, SEGMENTS.index(letter)])
        update_indexes = solution_map[:, SEGMENTS.index(letter)] != max_count
        solution_map[:, SEGMENTS.index(letter)][update_indexes] = 0
    
    for i in range(7):
        max_count = np.max(solution_map[i, :])
        update_indexes = solution_map[i, :] != max_count
        solution_map[i, :][update_indexes] = 0
    
    uncertain_segments = np.sum(solution_map, axis=0) > 1
    uncertain_segments = [SEGMENTS[i] for i in range(len(uncertain_segments)) if uncertain_segments[i]]

    unsolved_patterns = [p for p in patterns if p not in unique_segment_nums]
    
    for pattern in unsolved_patterns:
        if len(set(pattern) & set(uncertain_segments)) == len(uncertain_segments):
            number_9 = pattern
    
    for seg in number_9:
        if np.sum(solution_map[:, SEGMENTS.index(seg)]) == 0:
            solution_map[3, SEGMENTS.index(seg)] += 1
    
    unsolved_patterns = [p for p in unsolved_patterns if p != number_9]

    # remaining digits: 2, 3, 5, 6, 0

    number_1 = unique_segment_nums[0]
    number_4 = unique_segment_nums[2]

    ver_pair = number_1
    l_pair = ''.join([c for c in number_4 if c not in number_1])

    number_6_or_0 = [p for p in unsolved_patterns if len(p) == 6]
    number_3_or_0 = [p for p in unsolved_patterns if len(set(p) & set(l_pair)) == 1 and len(set(p) & set(ver_pair)) == 2]

    number_0 = list(set(number_3_or_0) & set(number_6_or_0))[0]
    number_6 = [n for n in number_6_or_0 if n != number_0][0]
    number_3 = [n for n in number_3_or_0 if n != number_0][0]

    unsolved_patterns = [p for p in unsolved_patterns if p not in [number_0, number_3, number_6]]

    number_2 = [p for p in unsolved_patterns if len(set(p) & set(l_pair)) == 1 and len(set(p) & set(ver_pair)) == 1][0]
    number_5 = [p for p in unsolved_patterns if len(set(p) & set(l_pair)) == 2 and len(set(p) & set(ver_pair)) == 1][0]

    # compare 2 and 5 to find 5
    for seg in l_pair:
        if seg not in number_2 and seg in number_5:
            solution_map[5, SEGMENTS.index(seg)] += 1
    
    # compare 5 and 6 to find 4
    segment_4 = list(set(number_6) - set(number_5))[0]
    solution_map[4, SEGMENTS.index(segment_4)] += 1

    # compare 5 and 4 to find 1
    for seg in ver_pair:
        if seg not in number_5 and seg in number_4:
            solution_map[1, SEGMENTS.index(seg)] += 1

    for letter in SEGMENTS:
        max_count = np.max(solution_map[:, SEGMENTS.index(letter)])
        update_indexes = solution_map[:, SEGMENTS.index(letter)] != max_count
        solution_map[:, SEGMENTS.index(letter)][update_indexes] = 0
    
    for i in range(7):
        max_count = np.max(solution_map[i, :])
        update_indexes = solution_map[i, :] != max_count
        solution_map[i, :][update_indexes] = 0
    
    return solution_map


def translate(pattern, solution_map):
    translated_digit = np.zeros(7)

    if len(pattern) == 7:
        return 8

    for seg in pattern:
        seg_idx =  SEGMENTS.index(seg)
        seg_position = np.argmax(solution_map[:, seg_idx])
        translated_digit[seg_position] = 1

    for items in DIGITS.items():
        if np.all(translated_digit == items[1]):
            return items[0]


def solution(input_data):
    input_data = input_data.strip().split('\n')
    split_values = lambda inp: (inp[0].strip().split(' '), inp[1].strip().split(' '))
    input_data = [split_values(inp.split('|')) for inp in input_data]

    result = 0
    for inp in input_data:
        solution_map = decipher_pattern(inp[0])
        output = []
        for pattern in inp[1]:
            output.append(translate(pattern, solution_map))
        number = int(''.join([str(n) for n in output]))
        result += number
    
    return result
    

if __name__ == '__main__':
    example = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

    print(solution(example))

    with open('input.txt') as f:
        input_data = f.read()
    
    print(solution(input_data))