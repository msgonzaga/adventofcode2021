import numpy as np


def score_board(board, bitmap, last_called_number):
    board = board.astype(np.int)
    last_called_number = int(last_called_number)
    indexes = np.where(bitmap == 0)
    unmarked_sum = np.sum(board[indexes])
    return unmarked_sum * last_called_number


def check_winner(board):
    """ Return true if the board has a row or column of marked numbers"""
    # perform sum along both axis and check whether at least one sum element is equal
    # to the board's dimension
    dim = board.shape[0]
    return np.any(np.sum(board, axis=0) == dim) or np.any(np.sum(board, axis=1) == dim)


def parse_bingo_input(text):
    """ Return the bingo board and the called numbers"""
    text = text.split('\n')
    called_numbers = text[0].split(',')
    boards = []

    for i in range(2, len(text[2:]), 6):
        new_board = text[i:i+5]
        new_board = np.array([r.lstrip(' ').replace(
            '  ', ' ').split(' ') for r in new_board])
        assert new_board.shape == (5, 5)
        boards.append(new_board)

    return called_numbers, boards


def solution(input):
    called_numbers, boards = parse_bingo_input(input)

    bitmaps = []
    for board in boards:
        bitmaps.append(np.zeros_like(board, dtype=np.int))

    winners = [0]*len(boards)

    last_winner_found = False
    for number in called_numbers:
        for i, board in enumerate(boards):
            if winners[i]:
                # this board already won
                continue
            number_index = np.where(board == number)
            if number_index[0].size == 0:
                continue
            else:
                bitmaps[i][number_index] = 1
                if check_winner(bitmaps[i]):
                    winners[i] = 1
                    if sum(winners) == len(winners):
                        last_winner_found = True
                        break
        if last_winner_found:
            break

    return score_board(board, bitmaps[i], number)


if __name__ == '__main__':

    example = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

    print(solution(example))

    with open('input.txt') as f:
        input = f.read()

    print(solution(input))
