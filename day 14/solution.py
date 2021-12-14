from collections import Counter


def parse_input(input_data):
    input_data = input_data.strip().split('\n')
    empty_line = input_data.index('')
    template = input_data[:empty_line][0]
    rules = [r.split(' -> ') for r in input_data[empty_line + 1:]]
    rule_dict = {r[0]: r[1] for r in rules}
    return template, rule_dict


def solution(input_data, steps=10):
    template, rules = parse_input(input_data)

    polymer = template
    pairs = Counter({polymer[i:i + 2]: 1 for i in range(len(polymer) - 1)})
    first_letter = template[0]

    for _ in range(steps):
        new_pairs = Counter()
        for pair in pairs.keys():
            insert_char = rules[pair]
            new_pairs[pair[0] + insert_char] += pairs[pair]
            new_pairs[insert_char + pair[1]] += pairs[pair]
        pairs = new_pairs

    letter_count = Counter()
    letter_count[first_letter] += 1
    for pair, count in pairs.items():
        letter_count[pair[1]] += count

    return max(letter_count.values()) - min(letter_count.values())


if __name__ == '__main__':
    example = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

    print(solution(example, 40))

    with open('input.txt') as f:
        input_data = f.read()

    print(solution(input_data, 40))
