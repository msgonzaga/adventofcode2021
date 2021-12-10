
SYMBOL_MAP = {
    '{': '}',
    '(': ')',
    '[': ']',
    '<': '>'
}

SCORE_MAP = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

COMPLETE_SCORE = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

def solution(input_data):
    lines = input_data.strip().split('\n')
    error_score = 0
    completion_scores = []
    for l in lines:
        symbol_stack = []
        corrupted = False
        for s in l:
            if s in SYMBOL_MAP:
                symbol_stack.append(s)
            else:
                opening_symbol = symbol_stack.pop()
                if SYMBOL_MAP[opening_symbol] == s:
                    continue
                else:
                    corrupted = True
                    error_score += SCORE_MAP[s]
                    break

        if not corrupted:
            completion_score = 0
            completion_string = [SYMBOL_MAP[c] for c in symbol_stack[::-1]]
            for c in completion_string:
                completion_score = (completion_score * 5) + COMPLETE_SCORE[c]
            completion_scores.append(completion_score)
    
    final_completion_score = sorted(completion_scores)[(len(completion_scores)//2)]

    return error_score, final_completion_score


if __name__ == '__main__':
    example = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

    print(solution(example))

    with open('input.txt') as f:
        input_data = f.read()

    print(solution(input_data)) 